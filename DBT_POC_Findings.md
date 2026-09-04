# DBT POC Findings

## Overview

The CareFlow dbt Proof of Concept (POC) was completed to evaluate whether BigQuery and dbt can support the project's data transformation, data quality, and analytics requirements.

The POC focused on building a staging layer, applying automated data quality tests, and creating analysis-ready analytics tables for downstream reporting and dashboard use.

## Data Quality Results

The complete dbt data quality test suite was executed successfully.

- **15 tests passed**
- **0 warnings**
- **0 errors**
- **0 skipped tests**

The tests validated:

- Required `Case_ID` values
- Required `Activity_Name` values
- Required `Timestamp` values
- Accepted `Activity_Name` values
- Case-level uniqueness
- Accepted conformance status values

This confirms that the staging and analytics models satisfy the current data quality checks defined in the dbt project.

## Analytics Layer Results

Four analysis-ready dbt tables were successfully built in BigQuery:

1. `patient_events`
2. `patient_transitions`
3. `case_summary`
4. `conformance_summary`

The successful builds produced the following row counts:

| Analytics Table | Rows |
|---|---:|
| `patient_events` | 878 |
| `patient_transitions` | 678 |
| `case_summary` | 200 |
| `conformance_summary` | 200 |

All four models completed successfully with dbt.

## Case Summary and Repeated Activity Logic

The `case_summary` model includes the `Has_Repeated_Events` field.

The logic identifies repeated `Activity_Name` values within the same `Case_ID`, regardless of whether the repeated activities occur at the same timestamp or at different timestamps.

For example:

```text
Triage
X-Ray
Triage
Doctor Consult
Discharge
```

This case contains two `Triage` activities at different timestamps and is therefore identified as having repeated activity.

The updated logic is based on comparing the total number of events with the number of distinct activities for each case:

```sql
count(*) > count(distinct Activity_Name) as Has_Repeated_Events
```

This correctly identifies cases where an activity occurs more than once within the patient's journey.

## Cross-Validation

The dbt `case_summary` results were compared with the existing Python-based analysis.

A discrepancy was identified in the number of patients with repeated Triage activity:

- Python CSV analysis: **73 patients**
- BigQuery/dbt analysis: **78 patients**
- Difference: **5 patients**

The dbt and BigQuery pipeline itself is functioning successfully, but the two analyses are currently using different data sources:

- Python reads `../data/hospital_event_log_clean.csv`
- dbt reads `careflow-clinical-analytics.careflow_raw.hospital_event_log`

Therefore, the discrepancy is currently treated as a data-source/version reconciliation issue rather than a dbt build failure.

Further investigation is required before the Python and dbt results can be considered fully cross-validated.

## POC Conclusion

The POC successfully demonstrated that the CareFlow analytics workflow can be implemented using BigQuery and dbt.

The staging model was validated with automated data quality tests, and the four planned analytics tables were successfully created.

The dbt build completed successfully and all 15 configured data quality tests passed.

The repeated-activity analysis also works successfully in BigQuery. However, cross-validation identified a discrepancy between the Python and BigQuery results for repeated Triage patients (Python=73, BigQuery=78).

This discrepancy should be resolved before the Python and dbt implementations are considered fully equivalent.

Overall, the results provide a reproducible and structured foundation for downstream reporting and dashboard development.

## Recommendation

**Recommendation: Proceed with a phased full migration assessment.**

The POC demonstrates that BigQuery and dbt can provide:

- Centralized transformation logic
- Automated data quality testing
- Reproducible analytics tables
- Clear separation between staging and analytics layers
- A scalable foundation for dashboard reporting

A full migration should be carried out incrementally, with the existing Python analysis retained as a validation reference during the transition.

Key metrics should continue to be cross-checked during the migration before the existing workflow is fully replaced.

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
| Python cross-validation | Discrepancy identified: Python=73, BigQuery=78 |
| Migration recommendation | Phased migration assessment |
