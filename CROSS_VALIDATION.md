# Cross-Validation — Python vs dbt/BigQuery

**Date:** Sept 4, 2026 
**Author:** Anagha S Pillai

## Purpose

Confirm that the deviation rate found via manual Python analysis matches
the number independently computed by Vaishnavi's dbt pipeline, using a
completely separate tool and codebase against the same underlying BigQuery
data (`careflow_raw.hospital_event_log`, 878 events, seed=42).

## Method

* **Python side:** `notebooks/eda.ipynb` conformance-checking section —
  compares each patient's actual activity sequence against the ideal path
  (Triage → X-Ray → Doctor Consult → Discharge) using pandas.
* **dbt/SQL side:** Queried Vaishnavi's `careflow_dbt.case_summary` table
  (built via dbt from the same raw table) using `Has_Repeated_Events`.

sql

```sql
SELECT 
  COUNT(*) as total_cases,
  COUNTIF(Has_Repeated_Events = true) as deviating_cases,
  ROUND(COUNTIF(Has_Repeated_Events = true) / COUNT(*) * 100, 1) as deviating_percent
FROM `careflow-clinical-analytics.careflow_dbt.case_summary`
```

## Results

| Metric             | Python (eda.ipynb) | dbt/BigQuery (case_summary) | Match? |
| ------------------ | ------------------ | --------------------------- | ------ |
| Total patients     | 200                | 200                         | ✅     |
| Deviating patients | 78                 | 78                          | ✅     |
| Deviation rate     | 39.0%              | 39.0%                       | ✅     |

**Exact match across both tools.**

## Significance

This is now the **fourth independent confirmation** of the same finding,
using four different methods:

1. Manual Python/pandas EDA
2. PM4Py algorithmic process discovery (DFG + Petri net)
3. Formal Python-based conformance checking
4. Independent dbt/SQL pipeline (this check)

All four agree exactly: **78/200 patients (39.0%) deviate** from the ideal
pathway due to the Triage→X-Ray→Triage loop-back, driven by missing intake
paperwork (see `ROOT_CAUSE_FINDINGS.md`).

This cross-tool agreement is strong evidence for Final Review that the
finding is robust and not an artifact of any single analysis method.
