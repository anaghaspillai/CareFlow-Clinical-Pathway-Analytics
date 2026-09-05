# DBT POC Findings

## Overview

The CareFlow dbt Proof of Concept (POC) was completed to evaluate whether BigQuery and dbt can support the project's data transformation, data quality, and analytics requirements.

The POC focused on building a staging layer, applying automated data quality tests, and creating analysis-ready analytics tables for downstream reporting and dashboard use.

## Data Quality Results

The complete dbt data quality test suite was executed successfully.

- 15 tests passed
- 0 warnings
- 0 errors
- 0 skipped tests

The tests validated:

- Required Case_ID values
- Required Activity_Name values
- Required Timestamp values
- Accepted Activity_Name values
- Case-level uniqueness
- Accepted conformance status values

This confirms that the staging and analytics models satisfy the current data quality checks defined in the dbt project.

## Analytics Layer Results

Four analysis-ready dbt tables were successfully built in BigQuery:

1. patient_events
2. patient_transitions
3. case_summary
4. conformance_summary

The successful builds produced the following row counts:

| Analytics Table | Rows |
|---|---:|
| patient_events | 878 |
| patient_transitions | 678 |
| case_summary | 200 |
| conformance_summary | 200 |

All four models completed successfully with dbt.

## Case Summary and Repeated Activity Logic

The case_summary model includes the Has_Repeated_Events field.

The logic identifies repeated Activity_Name values within the same Case_ID, regardless of whether the repeated activities occur at the same timestamp or at different timestamps.

For example:

Triage
X-Ray
Triage
Doctor Consult
Discharge

This case contains two Triage activities at different timestamps and is therefore identified as having repeated activity.

The updated logic is:

count(*) > count(distinct Activity_Name) as Has_Repeated_Events

This correctly identifies cases where an activity occurs more than once within the patient's journey.

## Cross-Validation

The dbt case_summary results were independently cross-validated against the Python-based analysis.

The final results match exactly:

- Python repeated-case count: 78
- BigQuery/dbt repeated-case count: 78
- Total cases: 200
- Deviation rate: 39.0%
- Difference: 0

The matching results confirm that the repeated-activity analysis is consistent across the Python and BigQuery/dbt implementations.

The earlier discrepancy between Python and BigQuery was caused by the local Python/CSV analysis being out of date. After the seeded data was corrected and the latest analysis was used, the results matched the dbt case_summary output.

Therefore, there is currently no discrepancy between the Python and BigQuery/dbt results for the repeated-activity metric.

## POC Conclusion

The POC successfully demonstrated that the CareFlow analytics workflow can be implemented using BigQuery and dbt.

The staging model was validated with automated data quality tests, and the four planned analytics tables were successfully created.

The dbt build completed successfully and all 15 configured data quality tests passed.

The repeated-activity analysis was independently cross-validated against the Python analysis, with both implementations producing the same result:

78 repeated cases out of 200 total cases, representing a 39.0% deviation rate.

This confirms that the core analytics results are consistent across the Python and BigQuery/dbt implementations.

Overall, the POC provides a reproducible, tested, and structured foundation for downstream reporting and dashboard development.

## Recommendation

Recommendation: Proceed with a phased full migration.

The POC demonstrates that BigQuery and dbt can provide:

- Centralized transformation logic
- Automated data quality testing
- Reproducible analytics tables
- Clear separation between staging and analytics layers
- Consistent results with the existing Python analysis
- A scalable foundation for dashboard reporting

A phased migration is recommended rather than an immediate full replacement. The existing Python analysis can continue to be used as an independent validation reference while the dbt pipeline is adopted.

Key business metrics should continue to be cross-checked during the migration to ensure consistency and prevent regressions.

Based on the successful POC, passing data quality tests, successfully built analytics layer, and matching Python/BigQuery results, full migration is worth pursuing.

## Final POC Status

| Area | Status |
|---|---|
| Staging model | Complete |
| Data quality tests | Complete |
| Patient Events | Complete |
| Patient Transitions | Complete |
| Case Summary | Complete |
| Conformance Summary | Complete |
| Repeated activity logic | Updated |
| dbt test suite | 15/15 passed |
| Python cross-validation | Complete - Python=78, BigQuery=78 |
| Deviation rate | 39.0% |
| Cross-validation discrepancy | None |
| Migration recommendation | Proceed with phased full migration |