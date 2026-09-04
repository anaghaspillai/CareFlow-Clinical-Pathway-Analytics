# CareFlow – Clinical Pathway Process Mining
# Project Documentation — Updated Through Week 3

---

## 1. Project Overview

**CareFlow – Clinical Pathway Process Mining** is a healthcare process analytics and process mining project designed to understand patient journeys through hospital workflows.

Traditional hospital dashboards can provide numerical metrics such as patient counts, activity counts, and average waiting time. However, these metrics may not clearly reveal the actual sequence of activities experienced by patients, repeated activities, process deviations, or loop-backs.

CareFlow addresses this by using timestamped hospital event logs to:

- Understand patient activity sequences.
- Discover the actual patient workflow.
- Identify repeated activities and process loops.
- Analyze transitions between activities.
- Measure waiting times.
- Identify potential process bottlenecks.
- Compare actual patient journeys with an expected workflow.
- Perform conformance checking.
- Investigate a simulated root-cause hypothesis.
- Validate the data using BigQuery and dbt.
- Present process insights through an interactive Power BI dashboard.

The project has currently progressed through **Week 3**. Week 4 work has **not yet started**.

---

# 2. Project Problem Statement

Hospital workflows involve multiple activities such as triage, diagnostic testing, consultation, and discharge.

Traditional KPI dashboards can report:

- Number of patients.
- Number of events.
- Activity counts.
- Average waiting time.

However, these metrics alone may not explain how patients actually move through the process.

For example, a patient may follow:

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

while another patient may experience:

```text
Triage
   ↓
X-Ray
   ↓
Triage
   ↓
Doctor Consult
   ↓
Discharge
```

The repeated Triage activity represents a process loop-back and a deviation from the expected pathway.

CareFlow uses process mining to identify and quantify this behavior and then investigates a possible explanation for the deviation.

---

# 3. Project Objectives

The main objectives are:

1. Generate realistic simulated hospital event logs.
2. Create chronological patient activity records.
3. Clean and standardize the event data.
4. Perform exploratory data analysis.
5. Identify repeated activities and process loops.
6. Analyze transition and waiting times.
7. Discover the patient workflow using PM4Py.
8. Generate Directly-Follows Graphs and Petri Net models.
9. Perform conformance checking.
10. Identify and investigate process deviations.
11. Test a simulated root-cause hypothesis.
12. Explore a lightweight BigQuery and dbt data-engineering workflow.
13. Build an interactive Power BI dashboard.
14. Add patient-level Drillthrough functionality.
15. Establish a reproducible final dataset.
16. Validate the dashboard against the final dataset.

---

# 4. End-to-End Project Workflow

The implemented workflow is:

```text
Python Event Generator
        ↓
Raw Hospital Event Log
        ↓
Python / Pandas Cleaning
        ↓
Cleaned Event Log
        ↓
Exploratory Data Analysis
        ↓
Bottleneck / Loop Analysis
        ↓
Waiting-Time Analysis
        ↓
PM4Py Process Discovery
        ↓
DFG + Petri Net
        ↓
Conformance Checking
        ↓
Root-Cause Investigation
        ↓
BigQuery Raw Table
        ↓
dbt Staging Model
        ↓
dbt Data Quality Tests
        ↓
Power BI Dashboard
        ↓
Patient Drillthrough
```

---

# 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Event-log generation and processing |
| Pandas | Data cleaning and exploratory analysis |
| Matplotlib | Basic data visualization |
| CSV | Local event-log storage |
| PM4Py | Process discovery and process mining |
| Graphviz | Process-map visualization |
| BigQuery | Cloud data warehouse POC |
| dbt | Data transformation and quality-check POC |
| Power BI | Interactive dashboard and patient drill-down |
| Git / GitHub | Version control and team collaboration |

---

# 6. Dataset

The project uses a simulated hospital event log.

The final stable dataset created during Week 3 contains:

| Metric | Value |
|---|---:|
| Patient cases | **200** |
| Total events | **878** |
| Rows removed during cleaning | **0** |
| Reproducibility seed | **42** |

The main activities are:

```text
Triage
X-Ray
Doctor Consult
Discharge
```

The event-level fields are:

| Field | Description |
|---|---|
| `Case_ID` | Unique identifier for each patient journey |
| `Activity_Name` | Hospital activity performed |
| `Timestamp` | Date and time of the activity |
| `Missing_Paperwork` | Simulated patient-level root-cause indicator |

---

# 7. Week 1 — Data Preparation and Exploratory Analysis

## 7.1 Event Generation

A Python event generator was developed in:

```text
src/generate_events.py
```

The generator creates 200 simulated patient journeys.

Each journey begins with Triage and progresses through X-Ray, Doctor Consult, and Discharge.

The normal process is:

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

The generator also creates a loop-back pattern for selected patients:

```text
Triage
   ↓
X-Ray
   ↓
Triage
   ↓
Doctor Consult
   ↓
Discharge
```

The loop-back was intentionally introduced so that process-mining techniques could be used to identify and analyze a process deviation.

---

## 7.2 Raw Event Log

The generated data is stored in:

```text
data/hospital_event_log.csv
```

The raw log contains event-level records for each patient.

---

## 7.3 Data Cleaning

The cleaning pipeline is implemented in:

```text
src/clean_events.py
```

The cleaning process performs:

- Missing-value checks.
- Removal of records missing `Case_ID`, `Activity_Name`, or `Timestamp`.
- Activity-name standardization.
- Timestamp conversion.
- Invalid timestamp removal.
- Duplicate removal.
- Chronological sorting by patient and timestamp.
- Saving the cleaned event log.

Output:

```text
data/hospital_event_log_clean.csv
```

The final Week 3 dataset was validated as:

```text
Original rows: 878
Final rows:    878
Rows removed:    0
Patients:      200
```

---

## 7.4 Exploratory Data Analysis

EDA was performed using:

```text
notebooks/eda.ipynb
```

The analysis includes:

- Dataset overview.
- Total patients.
- Total events.
- Activity distribution.
- Average events per patient.
- Repeated Triage analysis.
- Triage → X-Ray → Triage loop detection.
- X-Ray → Triage waiting-time analysis.
- Activity visualizations.

The EDA established the initial evidence for the repeated Triage loop.

---

# 8. Week 2 — Process Mining, Conformance and Dashboard

## 8.1 PM4Py Process Discovery

PM4Py was introduced to move from basic Pandas analysis to formal process discovery.

The process discovery workflow is:

```text
Cleaned Event Log
       ↓
PM4Py Event Log
       ↓
Process Discovery
       ↓
DFG
       ↓
Petri Net
```

The implementation is available in:

```text
notebooks/process_map.py
```

The process discovery workflow was successfully tested from a fresh clone of the repository.

---

## 8.2 Directly-Follows Graph

The Directly-Follows Graph represents relationships between consecutive hospital activities.

The main flow is:

```text
Triage → X-Ray → Doctor Consult → Discharge
```

The DFG also reveals the repeated transition:

```text
X-Ray → Triage
```

This provides process-level evidence for the loop-back identified during EDA.

---

## 8.3 Petri Net

A Petri Net process model was generated using PM4Py.

The model provides a structured representation of:

- Activities.
- Transitions.
- Patient-flow paths.
- Repeated behavior.
- Process deviations.

The Petri Net was successfully generated and visually verified.

---

## 8.4 Waiting-Time Analysis

Waiting-time analysis examines the time between consecutive activities for the same patient.

Important transitions include:

```text
Triage → X-Ray
X-Ray → Triage
X-Ray → Doctor Consult
Doctor Consult → Discharge
```

For the final stable dataset, the overall average consecutive-event waiting time is approximately:

```text
13.52 minutes
```

The average X-Ray → Triage waiting time for loop-back cases is approximately:

```text
19.95 minutes
```

Waiting time is treated separately from conformance because a process can deviate without necessarily having the largest delay, and vice versa.

---

# 9. Conformance Checking

Conformance checking compares each patient's actual sequence against the expected pathway:

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

A patient is considered conformant when the recorded sequence exactly matches this expected sequence.

For the final stable dataset:

| Metric | Result |
|---|---:|
| Total patients | 200 |
| Conformant patients | 122 |
| Deviating patients | 78 |
| Conformance | 61.0% |
| Deviation | 39.0% |

Calculation:

```text
Conformance = 122 / 200 × 100 = 61.0%

Deviation = 78 / 200 × 100 = 39.0%
```

The 78 deviating cases correspond to the loop-back pattern in the final simulated dataset.

---

# 10. Week 3 — Root-Cause Investigation

## 10.1 Why Root-Cause Analysis Was Required

EDA, PM4Py, and conformance checking established that the X-Ray → Triage loop occurs.

However, these methods show **what is happening**, not necessarily **why it is happening**.

The original project hypothesis was that missing or incomplete intake paperwork could cause patients to return to Triage.

---

## 10.2 Missing_Paperwork Field

A new patient-level field was introduced:

```text
Missing_Paperwork
```

The field is assigned at the beginning of each simulated patient journey.

The event-generation logic then uses this condition to determine whether the patient experiences the loop-back.

Conceptually:

```text
Missing_Paperwork = True
            ↓
Triage → X-Ray → Triage
```

---

## 10.3 Root-Cause Results

The final simulated dataset produced:

| Missing Paperwork | Did Not Loop Back | Looped Back |
|---|---:|---:|
| False | 122 | 0 |
| True | 0 | 78 |

Therefore:

```text
78 patients with Missing_Paperwork = True
→ 78 patients looped back
```

and:

```text
122 patients with Missing_Paperwork = False
→ 122 patients did not loop
```

This gives an exact association within the simulated model.

---

## 10.4 Interpretation

The result demonstrates that a patient-level event-log attribute can be used to test a process hypothesis.

Within this simulated dataset:

```text
Missing Paperwork
        ↓
Triage → X-Ray → Triage
```

is the modeled explanation for the loop-back.

### Important limitation

This is **not real-world causal evidence**.

The relationship is deliberately encoded in the simulation logic. If real hospital data were used, the relationship would need to be tested using actual intake/EHR fields and appropriate statistical or process-analysis methods.

---

# 11. Week 3 — BigQuery Proof of Concept

A lightweight BigQuery proof of concept was introduced during Week 3.

The purpose was to explore a centralized data layer without replacing the existing Python/PM4Py workflow.

Final BigQuery configuration:

```text
Project: careflow-clinical-analytics
Dataset: careflow_raw
Table: hospital_event_log
```

The final stable event log was uploaded and verified.

Expected and verified row count:

```text
878 events
```

The BigQuery POC therefore provides a cloud representation of the same event log used locally.

---

# 12. Week 3 — dbt Proof of Concept

A dbt staging model was created:

```text
stg_hospital_event_log
```

The model reads from:

```text
careflow-clinical-analytics.careflow_raw.hospital_event_log
```

The staging model selects:

```text
Case_ID
Activity_Name
Timestamp
Missing_Paperwork
```

---

## 12.1 dbt Data Quality Tests

The team added four data-quality checks.

### Test 1 — Case_ID

```text
not_null
```

Ensures every event belongs to a patient case.

### Test 2 — Activity_Name

```text
not_null
```

Ensures every event contains an activity.

### Test 3 — Timestamp

```text
not_null
```

Ensures every event contains a timestamp.

### Test 4 — Activity_Name Accepted Values

Allowed values:

```text
Triage
X-Ray
Doctor Consult
Discharge
```

The final dbt validation result was:

```text
4/4 tests passed
0 errors
0 warnings
```

---

# 13. Week 3 — Reproducibility Fix

## 13.1 Problem

Before the reproducibility fix, the loop-back was controlled by unseeded randomness.

As a result, regenerating the event log could produce different event counts.

For example, different runs had produced counts such as:

```text
873
882
```

This caused inconsistencies between:

- Local CSV.
- Power BI.
- BigQuery.
- Documentation.

---

## 13.2 Solution

The generator was updated to use:

```python
random.seed(42)
```

The seed is set before generating the patient journeys.

---

## 13.3 Validation

The generator was run repeatedly.

The result remained:

```text
200 patients
878 events
```

The cleaned dataset remained:

```text
878 rows
0 rows removed
```

The final 878-event dataset is therefore reproducible.

This allows the entire team to work against the same stable dataset.

---

# 14. Week 3 — Power BI Dashboard

Power BI is used to consolidate the process-mining results into an interactive dashboard.

The dashboard includes:

- Total Cases.
- Total Events.
- Conformance / Deviation metrics.
- Activity distribution.
- Process transitions.
- Waiting-time analysis.
- Process-flow information.
- Patient-level details.

---

# 15. Power BI Deviating % Validation

During final validation, the dashboard showed:

```text
Total Events = 878
Deviating %  = 36.50%
```

The issue was investigated.

The previous measure was:

```DAX
Deviating % = 73/200
```

This was the old Mid-Review calculation based on the previous dataset.

It was not a cache problem.

The measure was corrected so that it reflects the current deviation count.

The final dataset contains:

```text
78 deviating patients
200 total patients
```

Therefore:

```text
78 / 200 × 100 = 39.0%
```

### Current Status

**✅ Deviating % calculation issue resolved.**

The dashboard should now reflect:

```text
Deviating % = 39.00%
```

---

# 16. Patient Details Drillthrough

A Patient Details page was added to the Power BI dashboard.

The page is configured as a Drillthrough page using:

```text
Case_ID
```

This allows a user to select a patient case and navigate to the detailed event journey.

Example:

```text
Dashboard
   ↓
Select Case_ID
   ↓
Drillthrough
   ↓
Patient Details
```

The Drillthrough was tested using:

```text
P001
```

The patient-level event journey was displayed successfully.

### Status

**✅ Drillthrough working**

---

# 17. Final Week 3 Dataset Metrics

The stable dataset used after the reproducibility fix contains:

| Metric | Final Value |
|---|---:|
| Patient cases | **200** |
| Total events | **878** |
| Triage events | **278** |
| X-Ray events | **200** |
| Doctor Consult events | **200** |
| Discharge events | **200** |
| Conformant cases | **122** |
| Deviating cases | **78** |
| Conformance | **61.0%** |
| Deviation | **39.0%** |
| Average consecutive-event wait | **≈13.52 min** |
| Average X-Ray → Triage wait for loop cases | **≈19.95 min** |

---

# 18. Week 3 Validation Summary

| Component | Status |
|---|---|
| Event generation | ✅ Completed |
| Data cleaning | ✅ Completed |
| EDA | ✅ Completed |
| Bottleneck / loop analysis | ✅ Completed |
| Waiting-time analysis | ✅ Completed |
| PM4Py DFG | ✅ Completed |
| PM4Py Petri Net | ✅ Completed |
| Conformance checking | ✅ Completed |
| Root-cause POC | ✅ Completed |
| BigQuery POC | ✅ Completed |
| dbt staging model | ✅ Completed |
| dbt data-quality tests | ✅ 4/4 passed |
| Reproducibility fix | ✅ Completed |
| Power BI dashboard | 🔄 Final refinement |
| Deviating % fix | ✅ Resolved |
| Patient Drillthrough | ✅ Completed |

---

# 19. Historical vs Final Dataset

Because the project evolved during development, earlier documents contain historical numbers.

### Original Mid-Review dataset

```text
873 events
73 deviating cases
36.5% deviation
127 conformant cases
63.5% conformance
```

### Intermediate dataset after root-cause change

```text
882 events
82 deviating cases
41.0% deviation
```

### Final stable dataset

```text
878 events
78 deviating cases
39.0% deviation
122 conformant cases
61.0% conformance
```

The final numbers are based on the reproducible dataset generated with:

```python
random.seed(42)
```

The historical numbers should not be used for the final dashboard or final review results.

---

# 20. Repository Structure

The main project structure is:

```text
CareFlow-Clinical-Pathway-Analytics/
│
├── data/
│   ├── hospital_event_log.csv
│   └── hospital_event_log_clean.csv
│
├── notebooks/
│   ├── eda.ipynb
│   ├── process_map.py
│   ├── dfg_output.png
│   └── petri_net_output.png
│
├── src/
│   ├── generate_events.py
│   └── clean_events.py
│
├── dashboard/
│   ├── CareFlow_Dashboard.pbix
│   └── dashboard_screenshot.png
│
├── careflow_dbt/
│   ├── dbt_project.yml
│   └── models/
│       ├── staging/
│       │   └── stg_hospital_event_log.sql
│       └── example/
│           └── schema.yml
│
├── README.md
├── PROJECT_DOCUMENTATION.md
├── TESTING_NOTES.md
├── MID_REVIEW_DRAFT.md
├── CONFORMANCE_FINDINGS.md
├── ROOT_CAUSE_FINDINGS.md
├── Process_Map_Findings.md
└── BigQuery_dbt_Migration_Plan.md
```

---

# 21. Week 4 Status

**Week 4 work has not yet started.**

Therefore, the following items should **not** be marked as completed yet:

- Final Review completion.
- Final presentation completion.
- Additional Week 4 dashboard refinements.
- Any new Week 4 analytics.
- Final deployment or productionization work.

The current project status is:

```text
Week 1 → ✅ Completed
Week 2 → ✅ Completed
Week 3 → ✅ Completed / Final validation in progress
Week 4 → ⏳ Not Started
```

---

# 22. Current Overall Project Status

```text
Data Generation                  → ✅
Data Cleaning                    → ✅
EDA                              → ✅
Bottleneck Analysis              → ✅
Waiting-Time Analysis            → ✅
PM4Py Process Discovery          → ✅
DFG                              → ✅
Petri Net                        → ✅
Conformance Checking             → ✅
Root-Cause POC                   → ✅
BigQuery POC                     → ✅
dbt Staging                      → ✅
dbt Data Quality                 → ✅ 4/4
Reproducibility                  → ✅
Power BI Dashboard               → 🔄
Deviating % Fix                  → ✅
Patient Drillthrough             → ✅
Week 4 Work                      → ⏳ Not Started
Final Review Documentation       → 🔄 In Progress
```

---

# 23. Key Findings So Far

## Finding 1 — Process Loop

The main process deviation is:

```text
Triage → X-Ray → Triage
```

This loop occurs in 78 of 200 patient cases in the final stable dataset.

---

## Finding 2 — Process Deviation

The final conformance analysis shows:

```text
122 conformant cases = 61.0%
78 deviating cases   = 39.0%
```

---

## Finding 3 — Waiting Time

The average waiting time between consecutive activities is approximately:

```text
13.52 minutes
```

The X-Ray → Triage transition for loop-back cases averages approximately:

```text
19.95 minutes
```

---

## Finding 4 — Root-Cause Hypothesis

The simulated `Missing_Paperwork` attribute has an exact association with the loop-back:

```text
Missing_Paperwork = True
        ↓
Triage → X-Ray → Triage
```

This is a simulation-based finding and not real-world causal evidence.

---

## Finding 5 — Reproducibility

Using:

```python
random.seed(42)
```

ensures that the same dataset is generated on every run.

This solved the earlier changing-event-count problem.

---

## Finding 6 — Data Quality

The dbt staging model has four successful data-quality checks:

```text
Case_ID       → not_null
Activity_Name → not_null
Timestamp     → not_null
Activity_Name → accepted_values
```

All:

```text
4/4 tests passed
```

---

# 24. Next Steps

Since Week 4 has not started, the next project phase can focus on:

- Final dashboard refinement.
- Deeper patient-level process analysis.
- Additional dashboard drill-downs if required.
- Final validation of all KPIs.
- Final Review documentation.
- Final Review presentation.
- Final project conclusion and limitations.

These activities will be documented as Week 4 work only after they are actually completed.

---

# 25. Conclusion

Through Weeks 1–3, CareFlow has developed from a simulated hospital event-log generator into an integrated process analytics proof of concept.

The project now covers:

```text
Event Generation
      ↓
Data Cleaning
      ↓
EDA
      ↓
Process Mining
      ↓
Conformance Checking
      ↓
Root-Cause POC
      ↓
BigQuery
      ↓
dbt
      ↓
Power BI
      ↓
Patient Drillthrough
```

The final stable dataset contains:

```text
200 patients
878 events
122 conformant cases
78 deviating cases
61.0% conformance
39.0% deviation
```

The project has completed the major Week 1–3 implementation work. **Week 4 has not yet started**, and therefore its activities should remain listed as pending rather than completed.
