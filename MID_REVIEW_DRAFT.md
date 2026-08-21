
# CareFlow – Clinical Pathway Process Mining
# Mid-Review Draft

---

# 1. Project Overview

**CareFlow – Clinical Pathway Process Mining** is a healthcare process analytics and process mining project designed to understand patient journeys through hospital workflows.

Traditional hospital dashboards can provide numerical metrics such as patient counts, activity counts, and average waiting times. However, these metrics may not clearly reveal the actual sequence of activities experienced by patients or where process deviations occur.

CareFlow uses timestamped hospital event logs to:

* Understand patient activity sequences.
* Discover the actual patient workflow.
* Identify repeated activities and process loops.
* Analyze process transitions.
* Analyze waiting times.
* Identify potential process inefficiencies.
* Compare actual patient journeys against an expected workflow.
* Perform conformance checking.
* Present process insights through a Power BI dashboard.

The project follows the workflow:

```text
Hospital Event Data
        ↓
Data Generation
        ↓
Data Cleaning & Transformation
        ↓
Event Log Preparation
        ↓
Exploratory Data Analysis
        ↓
Repeated Activity & Process Analysis
        ↓
Waiting-Time Analysis
        ↓
PM4Py Process Discovery
        ↓
DFG + Petri Net
        ↓
Conformance Checking
        ↓
Power BI Dashboard
        ↓
Consolidated Process Insights
````

---

# 2. Problem Statement

Hospital workflows involve multiple activities such as registration, triage, consultation, diagnostic tests, review, pharmacy, and discharge.

Traditional dashboards generally focus on numerical KPIs such as:

* Number of patients
* Activity counts
* Average waiting time
* Average processing time

Although these metrics are useful, they may not show the actual process followed by individual patients.

Patients may experience:

* Repeated activities
* Process loop-backs
* Different activity sequences
* Delays between activities
* Deviations from the expected workflow
* Inefficient transitions

For example:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

The repeated Triage activity after X-Ray represents an observed process deviation that requires further investigation.

CareFlow aims to use process mining and analytics to identify, quantify, and visualize these process patterns.

---

# 3. Project Objectives

The main objectives of CareFlow are:

* Generate realistic timestamped hospital event logs.
* Clean and standardize hospital event data.
* Perform exploratory data analysis.
* Understand patient activity sequences.
* Identify repeated activities and process loops.
* Analyze process transitions.
* Analyze waiting times between activities.
* Discover the actual hospital workflow using PM4Py.
* Generate Directly-Follows Graphs and Petri Net models.
* Compare actual patient journeys with an expected workflow.
* Perform conformance checking.
* Identify process deviations.
* Build an interactive Power BI dashboard.
* Consolidate process-mining and dashboard findings.
* Provide process-oriented insights that can support further hospital workflow investigation.

---

# 4. Data Preparation

## 4.1 Event Log Generation

A Python-based event generator was developed to simulate hospital patient journeys.

Each patient is assigned a unique:

```text
Case_ID
```

The event log contains:

```text
Case_ID
Activity_Name
Timestamp
```

These represent:

```text
Case_ID        → Patient process case
Activity_Name  → Hospital activity
Timestamp      → Time of activity
```

The simulated patient journeys contain normal activity sequences as well as process loop-backs for analysis.

Example normal pathway:

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

Example observed loop:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

---

# 5. Data Cleaning

The `clean_events.py` script was used to prepare the generated event log for process analysis.

The cleaning workflow includes:

* Missing-value checking.
* Timestamp validation.
* Duplicate checking.
* Data standardization.
* Event-log preparation.
* Saving the cleaned event log.

The cleaned event log is stored as:

```text
data/hospital_event_log_clean.csv
```

The dataset used for the current analysis contains:

```text
Total patient cases = 200
Total recorded events = 883
```

The cleaned event log was successfully prepared for EDA and PM4Py process discovery.

---

# 6. Exploratory Data Analysis

Basic exploratory data analysis was performed using the hospital event log.

The EDA included:

* Dataset overview.
* Total patient cases.
* Total events.
* Activity distribution.
* Average events per patient.
* Repeated activity analysis.
* Triage → X-Ray → Triage loop analysis.
* X-Ray → Triage transition analysis.
* Waiting-time analysis.
* Basic activity visualizations.

The analysis identified a repeated process pattern involving:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

A total of:

```text
73 out of 200 patients
```

experienced this repeated loop.

Therefore:

```text
73 / 200 × 100 = 36.5%
```

The observed repeated-loop rate is:

**36.5%**

---

# 7. Process Loop / Deviation Analysis

The primary repeated process pattern identified in the event data is:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

The pattern affects:

```text
73 / 200 patient cases
```

which represents:

```text
36.5%
```

of all patient cases.

This repeated activity pattern was identified during EDA and subsequently examined through formal process discovery and conformance checking.

### Important Interpretation

The **36.5% value represents observed process deviation / repeated-process behavior**.

It should not automatically be interpreted as a confirmed waiting-time bottleneck.

A waiting-time bottleneck requires separate evidence from:

* Transition frequency.
* Waiting-time measurements.
* Average transition duration.
* Distribution of waiting times.
* Process impact.

Therefore, the current validated interpretation is:

> **The Triage → X-Ray → Triage pattern is a significant observed process deviation requiring further investigation.**

The root cause of this deviation has not yet been confirmed by the available event data.

---

# 8. Waiting-Time Analysis

Waiting-time analysis was performed to understand the time between consecutive patient activities.

Particular attention was given to transitions associated with the observed process deviation, including:

```text
X-Ray → Triage
```

Other relevant transitions include:

```text
Triage → X-Ray
X-Ray → Triage
Triage → Doctor Consult
Doctor Consult → Discharge
```

Waiting-time analysis provides additional information about process performance by examining how long patients spend between activities.

The waiting-time findings are being incorporated into the Power BI dashboard through:

* Average Wait Time KPI.
* Transition analysis.
* Waiting-time visualizations.

### Current Interpretation

The repeated Triage pattern identifies a process deviation.

The available analysis does not yet establish that this pattern is itself a waiting-time bottleneck.

Therefore, waiting-time evidence is treated separately from the 36.5% process-deviation metric.

### Status

**Completed – Dashboard Integration / Validation In Progress**

---

# 9. PM4Py Process Discovery

PM4Py was introduced to move from manual Pandas-based analysis to formal process discovery.

The cleaned hospital event log was provided as input to the PM4Py workflow.

The process discovery workflow is:

```text
Cleaned Event Log
        ↓
PM4Py Event Log
        ↓
Process Discovery
        ↓
Directly-Follows Graph
        ↓
Petri Net
        ↓
Process Map
```

The PM4Py process discovery script was successfully executed.

The process discovery workflow generated:

* Directly-Follows Graph.
* Petri Net process model.
* Process-map visualization.

### Status

**Completed – Verified**

---

# 10. Directly-Follows Graph

The Directly-Follows Graph (DFG) represents transitions between consecutive hospital activities.

The DFG provides a process-level view of:

* Common activity transitions.
* Frequently occurring paths.
* Repeated transitions.
* Process loops.
* Patient-flow relationships.

The observed process pattern:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

is represented within the discovered process behavior.

The DFG therefore provides formal process-level evidence supporting the process patterns initially identified during EDA.

### Status

**Completed – Verified**

---

# 11. Petri Net Process Model

A Petri Net process model was generated using PM4Py.

The Petri Net provides a structured representation of the discovered patient workflow.

It helps visualize:

* Activities.
* Transitions.
* Process paths.
* Process relationships.
* Repeated behavior.
* Potential deviations.

The generated Petri Net was successfully verified during the PM4Py workflow.

### Status

**Completed – Verified**

---

# 12. Expected Reference Workflow

For conformance checking, the expected patient pathway was defined as:

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

This workflow represents the reference pathway against which the actual patient activity sequences are compared.

---

# 13. Conformance Checking

Conformance checking was performed to compare actual patient journeys against the defined expected workflow.

The reference workflow is:

```text
Triage → X-Ray → Doctor Consult → Discharge
```

Each of the 200 patient cases was evaluated against this expected pathway.

A patient was classified as **conformant** when the recorded activity sequence exactly matched the expected pathway without repeated or additional activities.

---

# 14. Conformance Results

The final validated conformance results are:

| Metric                 | Result |
| ---------------------- | -----: |
| Total Patients         |    200 |
| Conformant Patients    |    127 |
| Deviating Patients     |     73 |
| Conformance Percentage |  63.5% |
| Deviation Percentage   |  36.5% |

Therefore:

```text
127 / 200 = 63.5% conformant
```

and:

```text
73 / 200 = 36.5% deviating
```

---

# 15. Conformance Interpretation

The conformance analysis shows:

```text
127 patients → 63.5% conformant
73 patients  → 36.5% deviating
```

The 36.5% deviation rate is consistent with the repeated process pattern identified earlier:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

The same 73-case pattern is therefore visible through multiple analytical stages:

```text
EDA
 ↓
Repeated Process Analysis
 ↓
PM4Py Process Discovery
 ↓
Conformance Checking
```

This consistency increases confidence that the observed process deviation is a meaningful pattern within the generated event log.

However, the available analysis does not establish the operational root cause of the deviation.

A possible explanation may exist in the underlying simulated workflow, but the root cause has not been independently confirmed by the event data.

### Status

**Completed – Results Verified**

---

# 16. Week 2 Final Validation

As part of Day 10 consolidation, the Week 2 outputs were reviewed to ensure consistency between:

```text
PM4Py Process Discovery
        ↓
Conformance Checking
        ↓
Power BI Dashboard
```

The final validation confirmed that the three components are aligned.

## Validated Metrics

```text
Total Cases       = 200
Repeated Loop     = 73
Repeated Loop %   = 36.5%

Conformant Cases  = 127
Conformant %      = 63.5%

Deviating Cases   = 73
Deviating %       = 36.5%
```

## Validated Main Flow

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

## Validation Conclusion

The final Week 2 validation confirmed that:

* PM4Py process discovery is consistent with the observed process behavior.
* Conformance results are consistent with the defined reference pathway.
* Dashboard KPI definitions use the validated metrics.
* Total case counts are aligned across the analysis.
* Conformant and deviating case counts are aligned.
* The 36.5% value is consistently treated as process deviation.
* Waiting-time bottleneck interpretation is kept separate from the deviation metric.

### Final Validation Status

**✅ Week 2 Validation Completed**

---

# 17. Power BI Dashboard

Power BI is being used to consolidate the process-mining findings into an interactive dashboard.

The dashboard brings together:

* Patient-level case counts.
* Conformance metrics.
* Process deviation metrics.
* Activity analysis.
* Transition analysis.
* Waiting-time analysis.
* Repeated activity analysis.
* Process insights.

---

## 17.1 Core KPI Cards

The current dashboard KPI structure includes four main KPI cards.

### KPI 1 – Total Cases

Shows the total number of patient cases analyzed.

```text
200
```

### KPI 2 – Conformant %

Shows the percentage of patient cases following the expected workflow.

```text
63.5%
```

### KPI 3 – Deviating %

Shows the percentage of patient cases that deviated from the expected workflow.

```text
36.5%
```

This label is preferred over using “Bottleneck %” because the metric specifically represents conformance deviation.

### KPI 4 – Average Wait Time

Shows the average waiting time between relevant patient activities.

The final value will be reported after the dashboard calculation is fully validated.

---

# 18. Dashboard Visualizations

The Power BI dashboard includes / is being developed with the following analytical areas.

## Activity Analysis

Activity counts are used to understand how frequently different hospital activities occur.

## Conformance Analysis

The conformance split displays:

```text
63.5% Conformant
        vs
36.5% Deviating
```

## Transition Analysis

The dashboard provides visibility into transitions between activities.

Examples include:

```text
Triage → X-Ray
X-Ray → Triage
Triage → Doctor Consult
Doctor Consult → Discharge
```

## Waiting-Time Analysis

Waiting-time visuals are used to examine the time spent between patient activities.

## Repeated Activity Analysis

The dashboard highlights the repeated Triage pattern and its occurrence across patient cases.

## Process Analysis

The dashboard incorporates process-level findings from PM4Py and the discovered patient workflow.

---

# 19. Dashboard Number Validation

The dashboard metrics were cross-checked against the final Week 2 validation.

The validated values are:

```text
Total Cases      = 200

Conformant       = 127
Conformant %     = 63.5%

Deviating        = 73
Deviating %      = 36.5%

Repeated Loop    = 73 / 200
Repeated Loop %  = 36.5%
```

The dashboard KPI definitions are aligned with the validated process findings.

The terminology is intentionally separated:

```text
Deviating %
      ↓
Conformance deviation

Repeated Loop %
      ↓
Observed repeated process behavior

Waiting Time
      ↓
Separate transition-time evidence
```

This prevents the same 36.5% value from being incorrectly presented as a waiting-time bottleneck.

### Status

**✅ KPI Definitions Validated**

**🔄 Dashboard Refinement In Progress**

---

# 20. BigQuery / dbt Scope Decision

BigQuery and dbt were evaluated as possible additions to the project architecture.

For the current implementation, the team decided to defer both technologies.

The decision was made to keep the project focused on the core process-mining workflow.

The current architecture is:

```text
Event Generation
      ↓
Raw CSV
      ↓
Python / Pandas Cleaning
      ↓
Cleaned CSV
      ↓
EDA
      ↓
PM4Py
      ↓
Process Analysis
      ↓
Conformance Checking
      ↓
Power BI
```

### Decision

```text
BigQuery → Deferred
dbt      → Deferred
```

They may be considered in a future version if scalable data warehousing or transformation requirements arise.

---

# 21. Fresh-Clone Testing

The project was tested from a fresh clone to verify reproducibility.

The following workflow was successfully tested:

```text
Repository Clone
      ↓
Dependency Installation
      ↓
Event Generation
      ↓
Data Cleaning
      ↓
EDA
      ↓
PM4Py Process Discovery
      ↓
DFG Generation
      ↓
Petri Net Generation
      ↓
Process Map Verification
```

The PM4Py workflow successfully executed from the fresh clone.

### Result

**✅ PASS**

---

# 22. Current Project Status

| Component                                 | Status          |
| ----------------------------------------- | --------------- |
| Event Generation                          | ✅ Completed     |
| Raw CSV Generation                        | ✅ Completed     |
| Data Cleaning                             | ✅ Completed     |
| Data Dictionary                           | ✅ Completed     |
| Exploratory Data Analysis                 | ✅ Completed     |
| Repeated Process Analysis                 | ✅ Completed     |
| Waiting-Time Analysis                     | ✅ Completed     |
| PM4Py Process Discovery                   | ✅ Completed     |
| DFG Generation                            | ✅ Completed     |
| Petri Net Generation                      | ✅ Completed     |
| Process Map Verification                  | ✅ Completed     |
| Fresh-Clone Testing                       | ✅ Completed     |
| Conformance Checking                      | ✅ Completed     |
| Conformance Results Validation            | ✅ Completed     |
| Dashboard KPI Definitions                 | ✅ Validated     |
| PM4Py / Conformance / Dashboard Alignment | ✅ Validated     |
| Power BI Core Dashboard                   | 🔄 In Progress  |
| Dashboard Refinement                      | 🔄 In Progress  |
| Mid-Review Documentation                  | 🔄 Finalization |
| Mid-Review Presentation                   | 🔄 Preparation  |
| Final Project                             | ⏳ Upcoming      |

---

# 23. Week 1 Progress

Week 1 focused on data preparation and initial process analysis.

Completed activities:

* Hospital event-log generation.
* Raw CSV creation.
* Data cleaning.
* Data dictionary preparation.
* Cleaned event-log preparation.
* Exploratory data analysis.
* Activity distribution analysis.
* Repeated activity analysis.
* Triage → X-Ray → Triage investigation.
* Initial waiting-time analysis.

### Week 1 Status

**✅ Completed**

---

# 24. Week 2 Progress

Week 2 progressed from process discovery into conformance checking and dashboard development.

Completed activities:

```text
PM4Py Setup
     ↓
Process Discovery
     ↓
DFG Generation
     ↓
Petri Net Generation
     ↓
Process Interpretation
     ↓
Conformance Checking
     ↓
Dashboard KPI Development
     ↓
Final Validation
```

The project progressed beyond the initial process-discovery scope by completing conformance checking and dashboard KPI alignment.

### Week 2 Status

**✅ Core Week 2 Analysis Completed**

**✅ Final Validation Completed**

**🔄 Dashboard Refinement Continuing**

---

# 25. Key Findings

## Finding 1 – Repeated Process Pattern

The main observed repeated process pattern is:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

It occurs in:

```text
73 / 200 patient cases
```

representing:

```text
36.5%
```

of the analyzed cases.

---

## Finding 2 – Process Deviation

Conformance checking identified:

```text
73 deviating cases
```

representing:

```text
36.5%
```

of the patient cases.

This deviation rate is consistent with the repeated process pattern observed during EDA and PM4Py process discovery.

---

## Finding 3 – Conformant Patient Journeys

The conformance analysis identified:

```text
127 / 200 cases
```

as conformant.

This represents:

```text
63.5%
```

of the analyzed patient cases.

---

## Finding 4 – PM4Py Process Discovery

PM4Py successfully generated:

* Directly-Follows Graph.
* Petri Net process model.
* Process-map visualization.

The discovered process behavior supports the activity patterns identified during the earlier EDA.

---

## Finding 5 – Waiting-Time Analysis

Waiting-time analysis was performed to understand delays between consecutive hospital activities.

The analysis is being used separately from process-deviation analysis.

The 36.5% deviation value should not be interpreted as a waiting-time bottleneck without additional transition-time evidence.

---

## Finding 6 – Cross-Component Validation

The final Week 2 validation confirmed alignment between:

```text
PM4Py
  ↕
Conformance Checking
  ↕
Power BI KPI Definitions
```

The following values are consistent across the analysis:

```text
200 total cases
127 conformant cases
73 deviating cases
63.5% conformant
36.5% deviating
```

This provides a consistent analytical basis for the Mid-Review.

---

# 26. Mid-Review Demonstration Flow

The Mid-Review demonstration will follow the complete project workflow.

## Step 1 – Introduce the Problem

Explain that traditional hospital KPIs do not always reveal actual patient process sequences.

## Step 2 – Show the Event Data

Demonstrate the timestamped event log containing:

```text
Case_ID
Activity_Name
Timestamp
```

## Step 3 – Show EDA

Present:

* Activity distribution.
* Patient counts.
* Repeated activity analysis.
* Triage → X-Ray → Triage pattern.

## Step 4 – Show PM4Py

Demonstrate:

* Directly-Follows Graph.
* Petri Net.
* Discovered patient workflow.

## Step 5 – Show Conformance Checking

Present:

```text
Expected:

Triage → X-Ray → Doctor Consult → Discharge
```

Then show:

```text
127 conformant = 63.5%
73 deviating   = 36.5%
```

## Step 6 – Show Power BI

Demonstrate:

```text
Total Cases
Conformant %
Deviating %
Average Wait Time
```

along with:

* Activity analysis.
* Conformance split.
* Transition analysis.
* Waiting-time analysis.
* Process findings.

## Step 7 – Explain Validation

Explain that PM4Py, conformance checking, and dashboard KPI definitions were cross-checked and found to be aligned.

## Step 8 – Explain the Limitation

Clearly state:

> The 36.5% metric represents process deviation / repeated process behavior. It is not independently considered a waiting-time bottleneck without supporting transition-time evidence.

---

# 27. Mid-Review Deliverables

The Mid-Review will demonstrate the following completed work:

### Data Preparation

* Event-log generation.
* Data cleaning.
* Data dictionary.
* Exploratory analysis.

### Process Analysis

* Repeated activity analysis.
* Process-loop analysis.
* Waiting-time analysis.

### Process Mining

* PM4Py process discovery.
* Directly-Follows Graph.
* Petri Net.
* Process-map interpretation.

### Conformance

* Expected workflow definition.
* Conformance checking.
* Conformant cases.
* Deviating cases.
* Deviation percentage.

### Dashboard

* Total Cases KPI.
* Conformant % KPI.
* Deviating % KPI.
* Average Wait Time KPI.
* Activity analysis.
* Conformance split.
* Transition analysis.
* Waiting-time analysis.
* Process analysis.

### Validation

* PM4Py validation.
* Conformance validation.
* Dashboard KPI validation.
* Cross-component consistency check.

---

# 28. Current Validated Results Summary

The current CareFlow results can be summarized as:

```text
Total Patient Cases
        ↓
      200
        ↓
   ┌────┴────┐
   ↓         ↓
Conformant  Deviating
  127          73
 63.5%        36.5%
```

The major observed repeated process pattern is:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

The expected workflow used for conformance checking is:

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

---

# 29. Limitations

The current project uses a simulated hospital event log.

Therefore:

* The data represents a simulated workflow rather than real hospital operations.
* The observed process deviation should not be interpreted as a confirmed clinical or operational problem without real-world validation.
* The root cause of the repeated Triage pattern has not been established.
* Waiting-time bottleneck conclusions require separate transition-time evidence.
* The project demonstrates process-mining methodology rather than production hospital deployment.

These limitations will be considered when interpreting the final results.

---
## Project Structure
```text
CareFlow-Clinical-Pathway-Analytics/
│
├── data/
│   ├── hospital_event_log.csv
│   └── hospital_event_log_clean.csv
│
├── src/
│   ├── generate_events.py
│   └── clean_events.py
│
├── notebooks/
│   ├── eda.ipynb
│   └── process_map.py
│
├── dashboard/
│   ├── CareFlow_Dashboard.pbix
│   └── dashboard_screenshot.png
│
├── process_map.png
│
├── CONFORMANCE_FINDINGS.md
├── Conformance_Rules.md
├── Dashboard_KPI_Definitions.md
├── MID_REVIEW_DRAFT.md
├── PM4Py_Setup_Notes.md
├── PROCESS_MAP_FINDINGS.md
├── PROJECT_DOCUMENTATION.md
├── TESTING_NOTES.md
├── WEEK2_SUMMARY.md
├── CareFlow_Project_Requirements_Data_Fields.md
├── CareFlow_Day2_Data_Dictionary_Activity_Check.md
│
├── README.md
├── requirements.txt
└── .gitignore
```
# 30. Next Steps

The remaining activities are focused on final dashboard refinement and Mid-Review preparation.

1. Finalize the Power BI dashboard layout.
2. Complete and validate the Average Wait Time KPI.
3. Finalize transition and waiting-time visuals.
4. Integrate PM4Py process outputs into the presentation.
5. Add DFG and Petri Net screenshots.
6. Finalize the conformance visualization.
7. Cross-check all dashboard numbers one final time.
8. Complete the Mid-Review documentation.
9. Prepare the Mid-Review presentation.
10. Prepare the project demonstration.
11. Present the consolidated Week 2 findings during the Mid-Review.

---

# 31. Expected Final Outcome

The final CareFlow system is expected to provide a process-oriented view of hospital patient journeys rather than relying only on traditional numerical KPIs.

The final solution will combine:

```text
Hospital Event Data
        ↓
Data Preparation
        ↓
Exploratory Data Analysis
        ↓
Process Discovery
        ↓
Process Transition Analysis
        ↓
Waiting-Time Analysis
        ↓
Repeated Activity Analysis
        ↓
Conformance Checking
        ↓
Power BI Dashboard
        ↓
Process-Oriented Insights
```

The final Power BI dashboard is expected to provide an interactive view of:

* Total patient cases.
* Conformance performance.
* Process deviations.
* Activity frequencies.
* Patient transitions.
* Waiting times.
* Repeated activities.
* Process patterns.
* Potential areas for further investigation.

The final CareFlow solution will help demonstrate:

**How patients move through hospital activities**

**Where process deviations and repeated activities occur**

**How actual patient journeys compare with the expected workflow**

**Where waiting-time and transition analysis may reveal potential delays**

**Which process areas require further investigation**

The project is therefore expected to demonstrate how **process mining, data analytics, conformance checking, and Power BI visualization** can be combined to provide a clearer understanding of healthcare workflows.

---

# 32. Conclusion

CareFlow has progressed from hospital event-log generation and data preparation to exploratory analysis, process discovery, conformance checking, dashboard development, and final Week 2 validation.

The major observed process pattern is:

```text
Triage → X-Ray → Triage
```

which occurs in:

```text
73 / 200 cases = 36.5%
```

Conformance checking against the expected workflow:

```text
Triage → X-Ray → Doctor Consult → Discharge
```

identified:

```text
127 conformant cases = 63.5%
73 deviating cases   = 36.5%
```

The final Week 2 validation confirmed that the **PM4Py process discovery, conformance findings, and Power BI dashboard KPI definitions are aligned**.

The 36.5% value is consistently interpreted as **process deviation / repeated process behavior**, while waiting-time bottleneck interpretation is kept separate and requires transition-time evidence.

The project is now in the final preparation stage for the Mid-Review, with the core analytical workflow completed and the Power BI dashboard being refined.

The Mid-Review will demonstrate the complete journey from:

```text
Event Data
    ↓
EDA
    ↓
Process Mining
    ↓
Conformance Checking
    ↓
Dashboard
    ↓
Validated Process Insights
```

The final expected outcome is a process-oriented healthcare analytics solution that can reveal patient-flow patterns, repeated activities, process deviations, waiting-time behavior, and areas requiring further investigation for hospital workflow improvement.

---

# 33. Mid-Review Status

**Mid-Review Date: August 25–27**

### Overall Project Status

**Core Analytics: ✅ Completed**

**PM4Py Process Discovery: ✅ Completed**

**Conformance Checking: ✅ Completed**

**Week 2 Final Validation: ✅ Completed**

**Dashboard KPI Alignment: ✅ Completed**

**Power BI Dashboard Refinement: 🔄 In Progress**

**Mid-Review Documentation: ✅ Finalized**

**Mid-Review Presentation: 🔄 Preparation**

**Final Project: ⏳ Upcoming**

```

This is the version I would use as your **final `MID_REVIEW_DRAFT.md`**. It keeps the earlier Mid-Review structure but incorporates **today's actual Day 10 validation**, especially the important distinction that **36.5% = process deviation, not automatically a waiting-time bottleneck**.
```
