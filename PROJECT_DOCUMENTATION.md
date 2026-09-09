
# CareFlow – Clinical Pathway Process Mining

## 📌 Project Overview

CareFlow is an end-to-end healthcare process analytics and process mining project developed to understand how patients move through a hospital workflow.

The project starts with timestamped event-log generation and cleaning, followed by:

* Exploratory Data Analysis (EDA)
* Bottleneck and waiting-time analysis
* PM4Py process discovery
* Directly-Follows Graph (DFG) and Petri Net generation
* Conformance checking
* Root-cause investigation
* BigQuery and dbt analytics
* Cross-validation
* Power BI dashboard reporting

The final reproducible dataset contains **200 patient cases and 878 events**.

### Expected Pathway

```text
Triage → X-Ray → Doctor Consult → Discharge
```

### Main Observed Process Deviation

```text
Triage → X-Ray → Triage
```

The main loop affects **78 cases (39.0%)**.

---

# 🎯 Problem Statement

Hospital workflows involve multiple activities and patient pathways. Traditional dashboards can provide aggregated information such as patient counts and waiting times, but they may not clearly show the actual sequence of activities followed by individual patients.

Patients may experience:

* Repeated activities
* Long waiting times
* Process loop-backs
* Different patient pathways
* Deviations from the expected workflow
* Inefficient transitions between activities

CareFlow uses process mining and data analytics to identify, quantify and visualize these process patterns. 

---

# 🎯 Project Objectives

The project objectives are to:

* Generate realistic timestamped patient event logs.
* Clean, standardize and validate event data.
* Perform EDA on patients, activities, sequences and waiting times.
* Identify repeated activities and potential bottlenecks.
* Discover the actual workflow using PM4Py.
* Generate DFG and Petri Net process models.
* Compare actual patient journeys with the expected pathway through conformance checking.
* Investigate a simulated root-cause field, `Missing_Paperwork`.
* Build a BigQuery + dbt analytics pipeline.
* Perform automated data-quality checks.
* Cross-validate Python findings against BigQuery/dbt outputs.
* Connect the analytics layer to Power BI.
* Provide patient-level drillthrough. 

---

# 🔄 Project Workflow

```text
Hospital Event Data
        ↓
Python Generation
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Bottleneck & Waiting-Time Analysis
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
dbt Staging
        ↓
dbt Analytics
        ↓
Cross-Validation
        ↓
Power BI Dashboard
        ↓
Patient Drillthrough
        ↓
Final Insights
```

---

# 🛠️ Technology Stack

| Technology | Use in CareFlow                                              |   |
| ---------- | ------------------------------------------------------------ | - |
| Python     | Event generation, processing and validation                  |   |
| Pandas     | Data cleaning, EDA and sequence analysis                     |   |
| Matplotlib | EDA visualizations                                           |   |
| PM4Py      | Process discovery and conformance analysis                   |   |
| Graphviz   | Process-map visualization                                    |   |
| BigQuery   | Cloud storage and analytics                                  |   |
| dbt        | SQL transformations, analytics models and data-quality tests |   |
| Power BI   | Interactive KPI dashboard, process analysis and drillthrough |   |
| Git/GitHub | Version control and collaboration                            |   |

---

# 📊 Dataset

The event log represents hospital patient journeys.

## Core Fields

| Field               | Description                                           |
| ------------------- | ----------------------------------------------------- |
| `Case_ID`           | Unique patient process case                           |
| `Activity_Name`     | Hospital activity performed                           |
| `Timestamp`         | Time at which the activity occurred                   |
| `Missing_Paperwork` | Simulated indicator used for root-cause investigation |

## Final Stable Dataset

| Metric        | Value |
| ------------- | ----: |
| Patient Cases |   200 |
| Events        |   878 |
| Cleaned Rows  |   878 |
| Rows Removed  |     0 |
| Random Seed   |    42 |

The fixed random seed ensures reproducible results. 

---

# 📅 Weekly Project Progress

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

# 🧹 Data Generation and Cleaning

The generator simulates patient journeys with timestamps.

### Normal Cases

```text
Triage → X-Ray → Doctor Consult → Discharge
```

### Deviating Cases

```text
Triage → X-Ray → Triage → Doctor Consult → Discharge
```

The final implementation uses:

```python
random.seed(42)
```

The cleaning workflow:

* Checks missing values.
* Validates timestamps.
* Checks duplicates.
* Standardizes activity values.
* Prepares the event log for analysis. 

---

# 🔍 Exploratory Data Analysis

EDA was performed to analyze:

* Dataset structure.
* Number of patient cases and events.
* Activity frequency distribution.
* Average events per patient.
* Repeated activity patterns.
* Loop-back behavior.
* Waiting time between consecutive activities.
* Activity and transition visualizations.

The final analysis identified **78 loop-back cases out of 200 patients**, equal to **39.0%**. 

---

# 🔄 Bottleneck Analysis

The main process pattern identified was:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

Out of **200 patient cases**:

* **78 patients** experienced the loop.
* The loop represents **39.0%** of all cases.

The repeated Triage pattern was identified as the primary process deviation requiring further investigation. 

---

# ⏱️ Waiting-Time Analysis

Waiting-time analysis was performed to understand the time spent between consecutive activities.

The analysis focused on transitions including:

* Triage → X-Ray
* X-Ray → Triage
* Triage → Doctor Consult

## Final Results

| Measure                                    |    Final Result |
| ------------------------------------------ | --------------: |
| Loop-back Cases                            |        78 / 200 |
| Loop-back Rate                             |           39.0% |
| Average Event-to-Event Wait                | ≈ 13.52 minutes |
| Average X-Ray → Triage Wait for Loop Cases | ≈ 19.95 minutes |

The waiting-time analysis complements the bottleneck analysis by identifying potential delays between activities. 

---

# 🔬 PM4Py Process Discovery

PM4Py was used to move from manual event-log analysis to formal process mining.

The implementation includes:

* Directly-Follows Graph (DFG)
* Petri Net process model
* Process-map visualization
* Fresh-clone verification

The discovered process confirms the main repeated behavior:

```text
Triage → X-Ray → Triage
```

The DFG provides a process-level representation of frequent transitions, loops and repeated activity sequences. 

---

# 🕸️ Petri Net Process Model

A Petri Net model was generated using PM4Py.

The model represents:

* Activities
* Process transitions
* Possible patient paths
* Process-flow relationships
* Repeated process behavior

The Petri Net model was successfully verified during project testing. 

---

# 🧩 Conformance Checking

The expected pathway is:

```text
Triage → X-Ray → Doctor Consult → Discharge
```

Each patient case was compared with this reference sequence.

## Final Results

| Metric           |      Result |
| ---------------- | ----------: |
| Total Cases      |         200 |
| Conformant Cases | 122 (61.0%) |
| Deviating Cases  |  78 (39.0%) |

A conformant case follows the defined pathway, while an additional repeated activity produces a deviating case. 

---

# 🔎 Root-Cause Investigation

The process-mining analysis identifies **what happened**, while root-cause analysis investigates a possible reason for the loop.

The project uses the simulated attribute:

```text
Missing_Paperwork
```

## Results

| Missing_Paperwork | Did Not Loop | Looped |
| ----------------- | -----------: | -----: |
| False             |          122 |      0 |
| True              |            0 |     78 |

The simulation produces a **100% association** between `Missing_Paperwork = True` and the loop.

> ⚠️ This is a proof-of-concept finding only. Because the relationship is encoded in simulated data, it cannot be interpreted as real-world clinical causation. 

---

# ☁️ BigQuery and dbt Implementation

The final project extends the local process-mining workflow with a BigQuery and dbt analytics layer.

The raw event data is stored in BigQuery and transformed into analysis-ready tables using dbt.

| Layer / Model            | Purpose                                       | Rows |   |
| ------------------------ | --------------------------------------------- | ---: | - |
| `hospital_event_log`     | Central event-data storage                    |  878 |   |
| `stg_hospital_event_log` | Clean staging representation                  |  878 |   |
| `patient_events`         | Analysis-ready event records                  |  878 |   |
| `patient_transitions`    | Sequential activity transitions and durations |  678 |   |
| `case_summary`           | Case-level process indicators                 |  200 |   |
| `conformance_summary`    | Case-level conformance results                |  200 |   |

---

# 🧪 dbt Data Quality

The completed dbt pipeline includes automated tests for:

* Required fields.
* Accepted activity values.
* Case-level uniqueness.
* Conformance status values.

## Test Results

| Test            |         Status |
| --------------- | -------------: |
| Automated Tests | **15/15 PASS** |
| Errors          |              0 |
| Warnings        |              0 |
| Skipped         |              0 |



---

# 🔄 Cross-Validation

To ensure the data-engineering layer did not change the original analytical conclusion, Python results were compared with BigQuery/dbt outputs.

| Metric          | Python | BigQuery/dbt | Match |
| --------------- | -----: | -----------: | ----- |
| Patients        |    200 |          200 | ✅ YES |
| Deviating Cases |     78 |           78 | ✅ YES |
| Deviation Rate  |  39.0% |        39.0% | ✅ YES |

**Result: Exact Match**

The same central process metric was independently reproduced through Python and SQL analytics paths. 

---

# 📊 Power BI Dashboard

The final Power BI dashboard is connected to the BigQuery analytics layer.

The dashboard includes:

* Total Cases
* Total Events
* Conformance %
* Deviating %
* Average Wait Time
* Activity distribution
* Process analysis
* Conformance split
* Patient Details drillthrough



---

# 🔎 Patient Drillthrough

A Patient Details page was implemented using:

```text
Case_ID
```

Selecting a patient displays the detailed event sequence, including:

* `Case_ID`
* `Activity_Name`
* `Timestamp`

The feature was tested using patient `P001` and verified successfully. 

---

# ♻️ Reproducibility

The project uses:

```python
random.seed(42)
```

This produces a stable dataset of:

* **200 patient cases**
* **878 events**

The same dataset is used for:

* Python analysis
* BigQuery/dbt validation
* Power BI reporting



---

# 🧪 Final Testing

The following components were successfully tested:

* ✅ Fresh-clone setup and dependency installation
* ✅ Event generation and reproducibility
* ✅ Data cleaning and validation
* ✅ EDA
* ✅ PM4Py process discovery
* ✅ DFG generation
* ✅ Petri Net generation
* ✅ Conformance checking
* ✅ Root-cause proof of concept
* ✅ BigQuery raw-table validation
* ✅ dbt staging and analytics builds
* ✅ 15/15 dbt data-quality tests
* ✅ Python vs BigQuery/dbt cross-validation
* ✅ Power BI refresh and KPI validation
* ✅ Deviating % fix
* ✅ Patient drillthrough



---

# 📌 Final Results

| Indicator                |            Final Result |
| ------------------------ | ----------------------: |
| Patients                 |                     200 |
| Events                   |                     878 |
| Conformant Cases         |             122 (61.0%) |
| Deviating Cases          |              78 (39.0%) |
| Main Loop                | Triage → X-Ray → Triage |
| Average Event Wait       |         ≈ 13.52 minutes |
| Loop X-Ray → Triage Wait |         ≈ 19.95 minutes |
| dbt Tests                |            15/15 Passed |
| Cross-Validation         |             Exact Match |



---

# 💡 Key Insights

* Process mining reveals patient sequence behavior that aggregate KPIs may hide.
* The **Triage → X-Ray → Triage** loop is the dominant deviation in the final simulated event log.
* **39.0%** of patient cases deviate from the expected pathway.
* Python and BigQuery/dbt independently reproduce the same deviation result.
* Power BI converts the validated analytics into an interactive operational view.
* The root-cause analysis demonstrates a method for testing hypotheses, while the simulated nature of the data limits real-world interpretation. 

---

# ⚠️ Limitations

* The event log is simulated and does not represent real clinical EHR data.
* `Missing_Paperwork` is simulated and cannot establish clinical causation.
* Waiting-time values depend on the simulation's timestamp logic.
* Conformance is defined against the project's fixed reference pathway.
* A real deployment would require privacy, governance, clinical validation and operational data-quality controls. 

---

# 🚀 Future Scope

Possible future improvements include:

* Validate the root-cause hypothesis using real hospital intake or EHR data.
* Support multiple clinical pathways and richer conformance rules.
* Introduce incremental or scheduled data ingestion.
* Expand anomaly detection and process-performance monitoring.
* Add department, resource and time-of-day analysis.
* Extend Power BI with additional patient and operational segmentation. 

---

# 🎓 Conclusion

CareFlow demonstrates an end-to-end and reproducible approach to healthcare process analytics and process mining.

The project progressed from:

```text
Event Generation & Cleaning
        ↓
Process Mining
        ↓
Conformance Checking
        ↓
Root-Cause Investigation
        ↓
BigQuery + dbt Analytics
        ↓
Cross-Validation
        ↓
Power BI Reporting
```

The final stable dataset contains **200 patients and 878 events**.

The main process finding is:

```text
Triage → X-Ray → Triage
```

This loop occurs in **78 cases**, resulting in a **39.0% deviation rate**.

The BigQuery/dbt analytics layer independently reproduced the Python findings and provides the analytics foundation for the final Power BI dashboard. The project demonstrates how process mining can be used to understand not only aggregate metrics, but also how individual patient journeys differ from the expected process. 
