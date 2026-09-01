# BigQuery Setup Notes — CareFlow

## 1. Project Setup

- Google Cloud Project: `careflow-clinical-analytics`
- BigQuery Studio running in free Sandbox mode (no billing required)
- Dataset: `careflow_raw`
- Location: `asia-south1` (Mumbai)

## 2. Table Created

- Table name: `hospital_event_log`
- Source: `hospital_event_log_clean.csv`
- Schema (auto-detected):
  - `Case_ID` — STRING
  - `Activity_Name` — STRING
  - `Timestamp` — TIMESTAMP
  - `Missing_Paperwork` — BOOLEAN

## 3. Data Validation

Ran verification queries against the loaded table:

- Total rows: 882
- No duplicate rows found
- 200 unique patients (Case_ID) — matches simulation
- Events by activity: Triage 282, X-Ray 200, Doctor Consult 200, Discharge 200

## 4. Note on Changed Numbers (873 → 882)

Earlier findings (EDA, PM4Py, conformance checking) were based on a dataset
with 873 events and 73/200 (36.5%) deviating patients. After the Day 11
root-cause fix (`Missing_Paperwork` flag), regenerating the data produces
different totals each run since the loop-back is still probability-based
(40% chance per patient). This run produced 882 events and 82/200 (41%)
deviating patients.

**Important:** these numbers are not fixed and will vary slightly each time
`generate_events.py` is run. A random seed should be added to make results
reproducible for Final Review.

## 5. Known Gap: Dashboard Out of Sync

The Power BI dashboard still reflects the original 873/36.5% figures, since
its source CSV has not been regenerated since Day 11. Needs a refresh once
the team settles on a fixed dataset (ideally after adding a random seed).

## 6. Next Steps

- Add a random seed to `generate_events.py` for reproducible results
- Vaishnavi to build dbt staging model against the `careflow_raw.hospital_event_log` table
- Refresh Power BI dashboard once numbers are finalized
