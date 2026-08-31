# CareFlow – Lightweight BigQuery + dbt Migration Plan

## 1. Objective

The goal is to explore a lightweight migration approach for the CareFlow project using BigQuery and dbt.

The purpose is to create a more centralized and scalable data workflow without making the current project unnecessarily complex.

## 2. Proposed Data Flow

**CSV / Event Log → BigQuery → dbt → Analytics Tables → Power BI + PM4Py**

- **BigQuery:** Store the CareFlow event-log data in a centralized data warehouse.
- **dbt:** Clean, transform, and validate the data.
- **Analytics Tables:** Provide analysis-ready data for downstream tools.
- **Power BI:** Use the analytics tables for dashboard reporting.
- **PM4Py:** Continue using the prepared event data for process mining and conformance checking.

## 3. Suggested BigQuery Layers

### Raw Layer
Store the original CareFlow event-log data with minimal changes.

Example table:

`careflow_raw.hospital_event_log`

Main fields:
- `Case_ID`
- `Activity_Name`
- `Timestamp`

### Staging Layer
Use dbt to:
- Standardize column names and data types
- Handle invalid or missing values
- Check duplicate records
- Standardize activity names

### Analytics Layer
Create analysis-ready tables such as:
- Patient Events
- Patient Transitions
- Case Summary
- Conformance Summary

## 4. dbt Data Quality Checks

Basic checks can include:

- `Case_ID` should not be null.
- `Activity_Name` should not be null.
- `Timestamp` should be valid.
- Unexpected duplicate events should be identified.
- Activity names should match the expected activity list.

## 5. Proof of Concept (POC)

Before doing a full migration, start with a small **POC (Proof of Concept)** using the existing CareFlow dataset.

The POC would:

1. Load the existing cleaned event log into BigQuery.
2. Create a simple dbt staging model.
3. Apply basic transformations and data-quality checks.
4. Create a small analytics table.
5. Compare the results with the existing PM4Py and Power BI results.

The goal is to confirm that the migrated workflow produces the same results before expanding it.

## 6. Validation

The migrated data should be checked against the current CareFlow results, including:

- Total Cases: **200**
- Total Events: **873**
- Repeated Triage: **73 cases (36.5%)**
- Conformance results should match the current analysis.

If the results match, the team can consider moving further toward the proposed architecture.

## 7. Future Improvements

If the POC is successful, the project could later add:

- Automated data ingestion
- Scheduled dbt runs
- Incremental models
- Additional data-quality tests
- Production monitoring

These improvements are not required for the initial lightweight migration.

## 8. Recommendation

Start with a small POC rather than immediately performing a full migration.

This approach allows the team to test BigQuery + dbt with the existing CareFlow dataset, verify that the results remain consistent, and then decide whether a complete migration is worthwhile.

**Recommended flow:**

**CSV/Event Log → BigQuery Raw → dbt Transformation → Analytics Tables → Power BI + PM4Py**
