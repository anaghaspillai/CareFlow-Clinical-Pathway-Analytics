# CareFlow – Clinical Pathway Process Mining

## 📌 Project Overview

**CareFlow** is a healthcare process analytics and process mining project designed to analyze patient journeys through hospital workflows.

Traditional hospital dashboards can report patient counts, activity counts, and waiting times, but they may not clearly reveal the sequence of activities followed by patients or where process deviations occur.

CareFlow uses timestamped hospital event logs to:

- Discover patient workflows.
- Identify repeated activities and process loop-backs.
- Analyze transitions and waiting times.
- Compare actual patient journeys with an expected pathway.
- Perform conformance checking.
- Investigate a simulated root-cause hypothesis.
- Validate data through BigQuery and dbt.
- Present the results through an interactive Power BI dashboard.

The current workflow is:

```text
Patient Event Data
        ↓
Python Event Generation
        ↓
Data Cleaning
        ↓
EDA
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
BigQuery
        ↓
dbt Staging + Data Quality Tests
        ↓
Power BI Dashboard
        ↓
Patient Drillthrough
        ↓
Final Process Insights
```

---

# 🎯 Key Objectives

- Generate realistic timestamped hospital event logs.
- Clean and standardize event data.
- Perform exploratory data analysis.
- Discover the actual patient workflow using PM4Py.
- Generate Directly-Follows Graphs and Petri Net models.
- Identify repeated activities and process loop-backs.
- Analyze waiting and transition times.
- Compare actual journeys with the expected workflow.
- Perform conformance checking.
- Investigate potential causes of process deviations.
- Store the final event log in BigQuery.
- Build a dbt staging model and data-quality checks.
- Develop an interactive Power BI dashboard.
- Provide patient-level drillthrough for detailed journey analysis.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Event-log generation and processing |
| Pandas | Data cleaning and analysis |
| Matplotlib | Basic visualizations |
| CSV | Local event-log storage |
| PM4Py | Process discovery and process mining |
| Graphviz | Process-map visualization |
| BigQuery | Cloud storage / analytics POC |
| dbt | Staging transformation and data-quality testing |
| Power BI | Interactive dashboard and drillthrough |
| Git & GitHub | Version control and collaboration |

---

# 📊 Final Stable Dataset

The event generator now uses a fixed random seed:

```python
random.seed(42)
```

This was introduced because earlier unseeded random generation caused the number of loop-back cases and total events to change between runs.

The final reproducible dataset contains:

| Metric | Final Value |
|---|---:|
| Patient cases | **200** |
| Total events | **878** |
| Rows removed during cleaning | **0** |
| Random seed | **42** |

The final activity counts are:

| Activity | Events |
|---|---:|
| Triage | 278 |
| X-Ray | 200 |
| Doctor Consult | 200 |
| Discharge | 200 |
| **Total** | **878** |

The event log also contains the `Missing_Paperwork` field used for the root-cause proof of concept.

Main fields:

- `Case_ID`
- `Activity_Name`
- `Timestamp`
- `Missing_Paperwork`

---

# 🧹 Data Cleaning

The script:

```text
src/clean_events.py
```

performs:

- Missing-value checks.
- Timestamp conversion and validation.
- Activity-name standardization.
- Duplicate removal.
- Chronological sorting by patient and timestamp.
- Cleaned event-log generation.

Final validation:

```text
Original rows: 878
Final rows:    878
Rows removed:  0
Unique cases:  200
```

Output:

```text
data/hospital_event_log_clean.csv
```

---

# 🔬 Exploratory Data Analysis

EDA was performed using Python/Pandas and the notebook:

```text
notebooks/eda.ipynb
```

The analysis covers:

- Dataset overview.
- Patient and event counts.
- Activity distribution.
- Average events per patient.
- Repeated activity analysis.
- Triage → X-Ray → Triage loop-back analysis.
- X-Ray → Triage waiting-time analysis.
- Activity visualizations.

The primary process pattern identified is:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

This repeated Triage path represents a process deviation from the expected pathway.

---

# 🔄 Bottleneck / Process Deviation Analysis

The expected patient pathway is:

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

The main observed deviation is:

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

In the final stable dataset:

- **78 of 200 patients** follow the loop-back pattern.
- Loop-back / deviation rate = **39.0%**.
- **122 of 200 patients** follow the expected four-activity sequence.
- Conformance rate = **61.0%**.

The repeated Triage path is treated as a significant process deviation requiring operational investigation.

> The event data identifies the pattern and its association with the simulated `Missing_Paperwork` field. It does not by itself prove that the same cause exists in a real hospital.

---

# ⏱️ Waiting-Time Analysis

Waiting-time analysis measures the time between consecutive activities for each patient.

Important transitions include:

```text
Triage → X-Ray
X-Ray → Triage
X-Ray → Doctor Consult
Doctor Consult → Discharge
```

For the final stable event log, the average time between consecutive recorded events is approximately:

```text
13.52 minutes
```

For patients following the Triage → X-Ray → Triage loop, the average X-Ray → Triage interval is approximately:

```text
19.95 minutes
```

Waiting time is analyzed separately from process conformance because a process deviation does not automatically mean that it caused a significant delay.

---

# 🔬 PM4Py Process Discovery

PM4Py was used to move from manual event-log analysis to formal process discovery.

Script:

```text
notebooks/process_map.py
```

Command:

```bash
python notebooks/process_map.py
```

The workflow successfully generated:

- Directly-Follows Graph (DFG).
- Petri Net process model.
- Process-map visualizations.

The main discovered pathway is:

```text
Triage → X-Ray → Doctor Consult → Discharge
```

The process model also shows the repeated Triage path after X-Ray.

### Status

**✅ Completed and verified**

---

# 🧩 Conformance Checking

The reference model used for conformance checking is:

```text
Triage → X-Ray → Doctor Consult → Discharge
```

A case is conformant when its complete recorded sequence matches this expected pathway without repeated or additional activities.

Final stable dataset results:

| Metric | Result |
|---|---:|
| Total patients | **200** |
| Conformant patients | **122** |
| Deviating patients | **78** |
| Conformance | **61.0%** |
| Deviation | **39.0%** |
| Total events | **878** |

The final 39.0% deviation rate matches the 78 patient loop-back count.

---

# 🔎 Root-Cause Investigation

The original process analysis identified the Triage → X-Ray → Triage loop but could not explain why the loop occurred.

A root-cause proof of concept was therefore added using:

```text
Missing_Paperwork
```

The field is assigned per patient in the simulation.

The final dataset shows:

| Missing Paperwork | Did Not Loop | Looped Back |
|---|---:|---:|
| False | 122 | 0 |
| True | 0 | 78 |

Therefore:

- Every patient with `Missing_Paperwork = True` looped back.
- No patient with `Missing_Paperwork = False` looped back.
- The observed simulated association is **100%**.

### Interpretation

Within the simulated model, missing/incomplete paperwork is a direct explanatory factor for the Triage → X-Ray → Triage loop.

This demonstrates a method for testing a root-cause hypothesis.

### Limitation

The correlation is intentionally built into the simulated generator. It should **not** be interpreted as proof of a real hospital root cause.

For real-world deployment, the hypothesis would need to be tested against actual intake/EHR data containing a genuine paperwork-completeness indicator.

---

# 🗄️ BigQuery Integration

A BigQuery proof of concept was implemented.

Current configuration:

```text
Project: careflow-clinical-analytics
Dataset: careflow_raw
Table: hospital_event_log
```

The final stable cleaned event log was uploaded to BigQuery.

The BigQuery table was verified against the local dataset.

Final row count:

```text
878
```

The table contains the event-log fields including:

```text
Case_ID
Activity_Name
Timestamp
Missing_Paperwork
```

### Status

**✅ Completed – POC verified**

---

# 🧱 dbt Staging Model

A dbt staging model was created:

```text
stg_hospital_event_log
```

Model file:

```text
careflow_dbt/models/staging/stg_hospital_event_log.sql
```

The staging model reads from:

```text
careflow-clinical-analytics.careflow_raw.hospital_event_log
```

The model exposes:

- `Case_ID`
- `Activity_Name`
- `Timestamp`
- `Missing_Paperwork`

### Status

**✅ Completed**

---

# 🧪 dbt Data Quality Tests

Data-quality checks were added to the dbt schema.

## Not-null tests

The following fields are required:

```text
Case_ID
Activity_Name
Timestamp
```

## Accepted-values test

`Activity_Name` is restricted to:

```text
Triage
X-Ray
Doctor Consult
Discharge
```

The four implemented tests are:

```text
not_null → Case_ID
not_null → Activity_Name
not_null → Timestamp
accepted_values → Activity_Name
```

All four tests passed successfully with no errors or warnings.

### Status

**✅ Completed – 4/4 tests passed**

---

# 📊 Power BI Dashboard

The Power BI dashboard consolidates the process-mining results.

Main dashboard components include:

- Total Patients / Cases.
- Total Events.
- Deviating %.
- Conformance %.
- Average Wait Time.
- Activity distribution.
- Process transitions.
- Conformance split.
- Bottleneck / repeated activity analysis.
- Waiting-time analysis.
- Process-flow analysis.
- Patient-level drillthrough.

---

# 🧮 Deviating % KPI Fix

During final dashboard validation, Total Events correctly updated to:

```text
878
```

but the Deviating % card continued to show:

```text
36.50%
```

The issue was identified as a hardcoded measure:

```DAX
Deviating % = 73/200
```

This represented the old dataset:

```text
73 / 200 = 36.5%
```

The measure was corrected so that the dashboard uses the current deviation calculation instead of the old hardcoded value.

For the final stable dataset:

```text
78 / 200 = 39.0%
```

Therefore the final expected dashboard value is:

```text
Deviating % = 39.00%
```

This ensures the KPI reflects the final dataset rather than a cached or manually entered historical value.

---

# 🔎 Patient Drillthrough

A dedicated **Patient Details** page was implemented using Power BI Drillthrough.

The drillthrough field is:

```text
Case_ID
```

The Patient Details page displays:

```text
Case_ID
Activity_Name
Timestamp
```

A user can select a patient from the dashboard and navigate to:

```text
Main Dashboard
      ↓
Right-click / Drillthrough
      ↓
Patient Details
```

The selected patient's journey is then displayed at the event level.

A Back button was also added for navigation to the main dashboard.

The drillthrough was tested successfully, including a test using patient `P001`.

### Status

**✅ Completed – Working**

---

# 🔄 Reproducibility

The earlier event-count differences were caused by unseeded randomness in the event generator.

The generator originally used probability-based loop-back generation without a fixed seed.

The following was added:

```python
random.seed(42)
```

The generator was then executed multiple times and consistently produced:

```text
878 events
200 patients
```

The cleaned dataset also remained:

```text
878 rows
0 rows removed
```

This provides a stable foundation for:

- Power BI.
- BigQuery.
- dbt.
- PM4Py.
- Final Review documentation.

---

# 🧪 Fresh-Clone Verification

The repository workflow was tested from a fresh clone.

Verified components include:

- Repository cloning.
- Dependency installation.
- Event generation.
- Data cleaning.
- EDA.
- PM4Py process discovery.
- DFG generation.
- Petri Net generation.
- Process-map generation.
- Documentation/setup instructions.

### Status

**✅ Core workflow verified**

---

# 📅 Week-wise Development

## Week 1 – Data Preparation & Initial Analysis

Completed:

- Event-log generation.
- Data cleaning.
- Data validation.
- Basic EDA.
- Activity analysis.
- Repeated activity analysis.
- Triage → X-Ray → Triage loop investigation.
- Initial waiting-time analysis.

**Status: ✅ Completed**

---

## Week 2 – Process Mining & Mid-Review

Completed:

- PM4Py process discovery.
- DFG generation.
- Petri Net generation.
- Process-map verification.
- Initial conformance checking.
- Power BI dashboard development.
- KPI cards and process-analysis visuals.
- Mid-Review documentation.
- Mid-Review presentation.
- Fresh-clone verification.

The earlier dataset used during Mid-Review contained different event counts and deviation results.

**Status: ✅ Completed**

---

## Weeks 3–4 – Root Cause, Data Engineering POC & Final Dashboard

Completed:

- Investigated the root cause of the Triage → X-Ray → Triage loop.
- Added and analyzed the `Missing_Paperwork` field.
- Confirmed the simulated relationship between missing paperwork and loop-back behavior.
- Stabilized event generation using `random.seed(42)`.
- Finalized the reproducible dataset at 878 events and 200 patients.
- Uploaded the final event log to BigQuery.
- Verified the BigQuery table.
- Implemented the dbt staging model.
- Added three `not_null` tests.
- Added one `accepted_values` test.
- Passed all four dbt tests.
- Updated the Power BI dashboard to the final dataset.
- Fixed the hardcoded Deviating % measure.
- Implemented Patient Details Drillthrough.
- Tested patient-level navigation and event details.
- Began final dashboard validation and Final Review documentation.

**Status: 🔄 Final presentation / final validation**

---

# 📋 Current Project Status

| Component | Status |
|---|---|
| Event Generation | ✅ Completed |
| Fixed Random Seed | ✅ Completed |
| Final Stable Dataset | ✅ 878 events / 200 patients |
| Data Cleaning | ✅ Completed |
| EDA | ✅ Completed |
| Bottleneck / Loop Analysis | ✅ Completed |
| Waiting-Time Analysis | ✅ Completed |
| PM4Py Process Discovery | ✅ Completed |
| DFG | ✅ Completed |
| Petri Net | ✅ Completed |
| Conformance Checking | ✅ Final results available |
| Root-Cause POC | ✅ Completed |
| BigQuery POC | ✅ Completed |
| dbt Staging Model | ✅ Completed |
| dbt Data Quality Tests | ✅ 4/4 Passed |
| Power BI Dashboard | 🔄 Final validation |
| Deviating % KPI | ✅ Corrected |
| Patient Drillthrough | ✅ Working |
| Fresh-Clone Verification | ✅ Completed |
| Mid-Review Documentation | ✅ Completed |
| Final Review Documentation | 🔄 In Progress |

---

# 📌 Final Validated Metrics

```text
Total Patients       = 200
Total Events         = 878

Conformant Patients  = 122
Deviating Patients   = 78

Conformance          = 61.0%
Deviation            = 39.0%

Average Event Wait   ≈ 13.52 minutes
Loop X-Ray → Triage  ≈ 19.95 minutes
```

---

# 🎯 Key Findings

### Finding 1 – Process Deviation

The main process deviation is:

```text
Triage → X-Ray → Triage
```

It affects:

```text
78 / 200 patients = 39.0%
```

---

### Finding 2 – Root-Cause Association

In the simulated model:

```text
Missing_Paperwork = True
             ↓
Triage → X-Ray → Triage
```

The relationship is exact within the generated dataset.

---

### Finding 3 – Conformance

The expected workflow is:

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

Final results:

```text
122 conformant cases = 61.0%
78 deviating cases   = 39.0%
```

---

### Finding 4 – Waiting Time

The average time between consecutive events is approximately:

```text
13.52 minutes
```

The average X-Ray → Triage interval among loop-back cases is approximately:

```text
19.95 minutes
```

---

### Finding 5 – Reproducibility

The final event generator uses:

```text
seed = 42
```

and consistently produces:

```text
878 events
200 patients
```

---

### Finding 6 – Data Quality

The dbt POC validates:

```text
Case_ID          → not null
Activity_Name    → not null
Timestamp        → not null
Activity_Name    → accepted values
```

All four tests pass.

---

# 🚀 Final Next Steps

1. Complete the final Power BI visual/KPI validation.
2. Verify all dashboard values against the final stable dataset.
3. Confirm the Patient Details Drillthrough remains functional.
4. Capture final dashboard screenshots.
5. Complete the Final Review presentation.
6. Present the process-mining findings, root-cause POC, BigQuery/dbt POC, and dashboard insights.

---

# 🎓 Expected Final Outcome

CareFlow provides a process-oriented view of hospital operations rather than relying only on traditional numerical KPIs.

The final solution demonstrates how process mining and analytics can be combined to:

- Understand patient activity sequences.
- Identify repeated activities and process deviations.
- Quantify deviations using conformance checking.
- Analyze waiting times between activities.
- Test a root-cause hypothesis.
- Validate data through dbt.
- Store event data in BigQuery.
- Provide interactive process analysis through Power BI.
- Drill from high-level KPIs to individual patient journeys.

The project combines:

```text
Python
+
Pandas
+
PM4Py
+
BigQuery
+
dbt
+
Power BI
```

to create an end-to-end healthcare process analytics proof of concept.
