# CareFlow – Clinical Pathway Process Mining

## 📌 Project Overview

**CareFlow** is an end-to-end healthcare process analytics and process mining project designed to analyze patient journeys through hospital workflows.

The project uses timestamped hospital event logs to:

* Discover patient workflows.
* Identify repeated activities and process loop-backs.
* Analyze transitions and waiting times.
* Compare actual patient journeys with an expected pathway.
* Perform conformance checking.
* Investigate a simulated root-cause hypothesis.
* Validate analytics through BigQuery and dbt.
* Present results through an interactive Power BI dashboard.

### Final Workflow

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
dbt Staging + Analytics + Data Quality Tests
        ↓
Cross-Validation
        ↓
Power BI Dashboard
        ↓
Patient Drillthrough
        ↓
Final Process Insights
```

---

# 🎯 Key Objectives

* Generate realistic timestamped hospital event logs.
* Clean and standardize event data.
* Perform exploratory data analysis.
* Discover the patient workflow using PM4Py.
* Generate Directly-Follows Graphs and Petri Net models.
* Identify repeated activities and process loop-backs.
* Analyze waiting and transition times.
* Perform conformance checking.
* Investigate a simulated root-cause hypothesis.
* Build a BigQuery and dbt analytics pipeline.
* Perform automated data-quality checks.
* Cross-validate Python and BigQuery/dbt results.
* Develop an interactive Power BI dashboard.
* Provide patient-level drillthrough.

---

# 🛠️ Technology Stack

| Technology   | Purpose                                    |
| ------------ | ------------------------------------------ |
| Python       | Event-log generation and processing        |
| Pandas       | Data cleaning and analysis                 |
| Matplotlib   | Visualizations                             |
| PM4Py        | Process discovery and conformance checking |
| Graphviz     | Process-map visualization                  |
| BigQuery     | Cloud storage and analytics                |
| dbt          | Data transformation and quality testing    |
| Power BI     | Interactive dashboard and drillthrough     |
| Git & GitHub | Version control and collaboration          |

---

# 📊 Final Stable Dataset

The event generator uses:

```python
random.seed(42)
```

The final reproducible dataset contains:

| Metric        | Final Value |
| ------------- | ----------: |
| Patient Cases |     **200** |
| Total Events  |     **878** |
| Cleaned Rows  |     **878** |
| Rows Removed  |       **0** |
| Random Seed   |      **42** |

Main fields:

* `Case_ID`
* `Activity_Name`
* `Timestamp`
* `Missing_Paperwork`

---

# 🧹 Data Cleaning

The cleaning workflow performs:

* Missing-value checks.
* Timestamp validation.
* Activity-name standardization.
* Duplicate checks.
* Chronological sorting.
* Cleaned event-log generation.

### Final Validation

```text
Original Rows: 878
Final Rows:    878
Rows Removed:  0
Unique Cases:  200
```

**Status: ✅ Completed**

---

# 🔬 Exploratory Data Analysis

The analysis covers:

* Patient and event counts.
* Activity distribution.
* Repeated activity analysis.
* Process loop-back analysis.
* Waiting-time analysis.
* Activity and transition visualizations.

The main process pattern identified is:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

This repeated Triage path represents the main process deviation.

**Status: ✅ Completed**

---

# 🔄 Bottleneck / Process Deviation Analysis

### Expected Pathway

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

### Main Observed Deviation

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

Final results:

* **78 of 200 patients** follow the loop-back pattern.
* Loop-back / deviation rate = **39.0%**.
* **122 of 200 patients** follow the expected pathway.
* Conformance rate = **61.0%**.

**Status: ✅ Completed**

---

# ⏱️ Waiting-Time Analysis

Waiting-time analysis measures the time between consecutive activities.

Final results:

```text
Average Event-to-Event Wait ≈ 13.52 minutes
Average X-Ray → Triage Wait ≈ 19.95 minutes
```

**Status: ✅ Completed**

---

# 🔬 PM4Py Process Discovery

PM4Py was used for formal process mining.

Generated outputs include:

* Directly-Follows Graph (DFG).
* Petri Net process model.
* Process-map visualization.

The discovered workflow confirms the expected patient pathway while also identifying the repeated Triage loop.

**Status: ✅ Completed and Verified**

---

# 🧩 Conformance Checking

The reference pathway is:

```text
Triage → X-Ray → Doctor Consult → Discharge
```

Final results:

| Metric              |    Result |
| ------------------- | --------: |
| Total Patients      |   **200** |
| Conformant Patients |   **122** |
| Deviating Patients  |    **78** |
| Conformance         | **61.0%** |
| Deviation           | **39.0%** |

**Status: ✅ Completed**

---

# 🔎 Root-Cause Investigation

A simulated `Missing_Paperwork` field was used to investigate the loop-back pattern.

| Missing Paperwork | Did Not Loop | Looped Back |
| ----------------- | -----------: | ----------: |
| False             |          122 |           0 |
| True              |            0 |          78 |

The simulated data shows a **100% association** between `Missing_Paperwork = True` and the loop-back pattern.

> This is a proof of concept using simulated data and should not be interpreted as real-world clinical causation.

**Status: ✅ Completed**

---

# 🗄️ BigQuery Integration

The final cleaned event log was integrated into BigQuery.

The BigQuery analytics layer supports the transformed project data and Power BI reporting.

Final row count:

```text
878
```

**Status: ✅ Completed**

---

# 🧱 dbt Analytics Pipeline

The completed dbt pipeline includes:

* `stg_hospital_event_log`
* `patient_events`
* `patient_transitions`
* `case_summary`
* `conformance_summary`

The models provide cleaned event data, activity transitions, patient-level summaries and conformance results.

**Status: ✅ Completed**

---

# 🧪 dbt Data Quality Tests

The completed pipeline includes automated tests for:

* Required fields.
* Accepted activity values.
* Case-level uniqueness.
* Conformance status validation.

### Final Result

```text
Automated Tests: 15/15 PASS
Errors:          0
Warnings:        0
Skipped:         0
```

**Status: ✅ Completed – 15/15 Tests Passed**

---

# 🔄 Cross-Validation

The final Python analysis was cross-validated against the BigQuery/dbt analytics output.

| Metric          | Python | BigQuery/dbt | Match |
| --------------- | -----: | -----------: | ----- |
| Patients        |    200 |          200 | YES   |
| Deviating Cases |     78 |           78 | YES   |
| Deviation Rate  |  39.0% |        39.0% | YES   |

**Status: ✅ Completed – Exact Match**

---

# 📊 Power BI Dashboard

The final Power BI dashboard includes:

* Total Cases.
* Total Events.
* Conformance %.
* Deviating %.
* Average Wait Time.
* Activity distribution.
* Process transitions.
* Conformance split.
* Bottleneck analysis.
* Waiting-time analysis.
* Patient-level drillthrough.

The dashboard is connected to the completed BigQuery analytics layer.

**Status: ✅ Completed**

---

# 🧮 Deviating % KPI

The earlier hardcoded Deviating % value was corrected.

Final value:

```text
78 / 200 = 39.0%
```

The Power BI KPI now correctly reflects:

```text
Deviating % = 39.00%
```

**Status: ✅ Corrected and Validated**

---

# 🔎 Patient Drillthrough

A Patient Details page was implemented using:

```text
Case_ID
```

The drillthrough displays:

```text
Case_ID
Activity_Name
Timestamp
```

Patient-level drillthrough was tested successfully, including patient `P001`.

**Status: ✅ Completed**

---

# 🔄 Reproducibility

The project uses:

```python
random.seed(42)
```

This ensures that the final dataset consistently produces:

```text
200 Patients
878 Events
```

The same stable dataset is used for:

* Python analysis.
* PM4Py process mining.
* BigQuery/dbt analytics.
* Cross-validation.
* Power BI reporting.

**Status: ✅ Completed**

---

# 🧪 Final Testing

The following components were successfully tested:

* Event generation and reproducibility.
* Data cleaning and validation.
* EDA.
* PM4Py process discovery.
* DFG generation.
* Petri Net generation.
* Conformance checking.
* Root-cause proof of concept.
* BigQuery validation.
* dbt staging and analytics models.
* 15/15 dbt data-quality tests.
* Python vs BigQuery/dbt cross-validation.
* Power BI refresh and KPI validation.
* Deviating % correction.
* Patient drillthrough.

**Status: ✅ All Final Testing Completed**

---

# 📅 Project Development

## Week 1 – Data Preparation & Initial Analysis

Completed:

* Set up the project repository, branches, documentation and tracking workflow. 
* Developed the Python event generator and simulated hospital patient journeys. 
* Generated and cleaned the initial event log using Python and Pandas. 
* Performed EDA, activity analysis and waiting-time analysis. 
* Identified the Triage → X-Ray → Triage loop as the main process deviation. 
* Created the data requirements and data dictionary. 
* Installed and configured PM4Py for process-mining analysis. 
* Completed initial README, project documentation and fresh-clone testing.


**Status: ✅ Completed**

---

## Week 2 – Process Mining, Conformance and Mid-Review Preparation

Completed:

* Implemented formal PM4Py process discovery.
* Generated the Directly-Follows Graph (DFG) and Petri Net process model.
* Completed conformance checking against the expected clinical pathway.
* Developed the initial Power BI dashboard with KPI cards, DAX measures and process-analysis visuals.
* Refined dashboard terminology and layout based on team feedback. 
* Documented process-map findings and the initial BigQuery/dbt scope decision. 
* Performed consistency and validation checks across process-mining outputs. 
* Prepared the Mid-Review report, presentation and supporting documentation.

**Status: ✅ Completed**

---

## Weeks 3 - Process Mining, Mid-Review & Dashboard Refinement

Completed:

* Continued process-mining and conformance analysis after the initial implementation. 
* Refined the Power BI dashboard based on review feedback. 
* Performed consistency checks across process maps, conformance results and dashboard figures. 
* Completed Mid-Review presentation and the documentation/next-steps section. 
* Consolidated the technical findings and documentation for the final project phase.

**Status: ✅ Completed**

---
## Weeks 4 -Data Engineering, Root Cause & Final Integration

Completed:

*	Investigated the recurring process loop using the simulated Missing_Paperwork attribute. 
*	Implemented the BigQuery + dbt Raw → Staging → Analytics pipeline. 
*	Built the dbt analytics models: patient_events, patient_transitions, case_summary, and conformance_summary. 
*	Implemented and passed 15/15 automated data-quality tests. 
*	Corrected the repeated-activity logic in case_summary. 
*	Fixed the random seed to 42 and stabilized the final dataset at 878 events / 200 patients. 
*	Cross-validated Python vs BigQuery/dbt results, confirming 78 deviating cases (39.0%). 
*	Connected case_summary and conformance_summary directly to Power BI. 
*	Implemented and tested patient-level Drillthrough using Case_ID. 
*	Corrected the stale Deviating % KPI from 36.5% to the final 39.0%. 
*	Completed the Final Review documentation and README files.

---
# 📋 Final Project Status

| Component                  | Status                      |
| -------------------------- | --------------------------- |
| Event Generation           | ✅ Completed                 |
| Fixed Random Seed          | ✅ Completed                 |
| Final Stable Dataset       | ✅ 878 Events / 200 Patients |
| Data Cleaning              | ✅ Completed                 |
| EDA                        | ✅ Completed                 |
| Bottleneck / Loop Analysis | ✅ Completed                 |
| Waiting-Time Analysis      | ✅ Completed                 |
| PM4Py Process Discovery    | ✅ Completed                 |
| DFG                        | ✅ Completed                 |
| Petri Net                  | ✅ Completed                 |
| Conformance Checking       | ✅ Completed                 |
| Root-Cause POC             | ✅ Completed                 |
| BigQuery                   | ✅ Completed                 |
| dbt Analytics Pipeline     | ✅ Completed                 |
| dbt Data Quality Tests     | ✅ 15/15 Passed              |
| Cross-Validation           | ✅ Exact Match               |
| Power BI Dashboard         | ✅ Completed                 |
| Deviating % KPI            | ✅ Corrected                 |
| Patient Drillthrough       | ✅ Completed                 |
| Final Testing              | ✅ Completed                 |
| Final Documentation        | ✅ Completed                 |

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

dbt Tests            = 15/15 Passed
Cross-Validation     = Exact Match
```

---

# 🎯 Key Findings

### Process Deviation

```text
Triage → X-Ray → Triage
```

This affects:

```text
78 / 200 Patients = 39.0%
```

### Conformance

```text
122 Conformant Cases = 61.0%
78 Deviating Cases   = 39.0%
```

### Root-Cause Proof of Concept

The simulated `Missing_Paperwork` field is associated with the loop-back pattern in the generated dataset.

### Reproducibility

The fixed random seed ensures stable and reproducible results.

### Data Validation

Python and BigQuery/dbt independently produce matching final results.

---

# 🚀 Project Completion

All planned project components have been successfully completed, validated and documented.

* ✅ Final Power BI dashboard validated.
* ✅ Dashboard KPIs verified.
* ✅ Patient drillthrough tested.
* ✅ BigQuery/dbt analytics completed.
* ✅ 15/15 dbt tests passed.
* ✅ Python and BigQuery/dbt results cross-validated.
* ✅ Final report completed.
* ✅ Final presentation completed.
* ✅ README and testing documentation completed.

---

# 🎓 Final Outcome

**CareFlow – Clinical Pathway Process Mining** is a fully completed end-to-end healthcare process analytics project.

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

The final solution demonstrates how process mining, data engineering and business intelligence can be integrated to analyze patient journeys, identify process deviations, investigate potential causes, validate analytical results and provide interactive reporting.

The final stable dataset contains **200 patient cases and 878 events**. The main process deviation is the **Triage → X-Ray → Triage** loop, affecting **78 cases (39.0%)**. The final results were independently reproduced through Python and BigQuery/dbt and are presented through the completed Power BI dashboard.
