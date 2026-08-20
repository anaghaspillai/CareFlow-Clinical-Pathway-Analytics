# CareFlow – Mid-Review

# 1. Project Overview

**CareFlow – Clinical Pathway Process Mining** is a healthcare process analytics project designed to understand patient journeys through hospital workflows.

The project uses timestamped hospital event logs to analyze the sequence of activities performed during patient journeys. Process mining techniques are used to discover the actual workflow, identify repeated activities, detect bottlenecks, analyze waiting and transition times, and compare actual patient paths against an expected process.

The project is being developed incrementally:

```text
Hospital Event Data
        ↓
Data Preparation & Cleaning
        ↓
Exploratory Data Analysis
        ↓
Bottleneck & Waiting-Time Analysis
        ↓
PM4Py Process Discovery
        ↓
Process Model / Process Map
        ↓
Conformance Checking
        ↓
Power BI Dashboard
        ↓
Healthcare Process Insights
```

# 2. Problem Statement

Hospital workflows involve multiple activities such as registration, triage, consultation, diagnostic tests, review, pharmacy, and discharge.

Traditional dashboards can show numerical KPIs such as patient counts and average waiting times, but they may not clearly show the actual sequence of activities followed by patients.

Patients may experience:

* Repeated activities
* Long waiting times
* Process loop-backs
* Different patient pathways
* Deviations from the expected workflow
* Inefficient transitions between activities

For example:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

The repeated Triage activity may indicate a potential process inefficiency that requires further investigation.

CareFlow aims to use process mining and data analytics to identify, quantify, and visualize these process patterns.

# 3. Project Objectives

The main objectives of CareFlow are:

* Generate realistic timestamped hospital event logs.
* Clean and standardize the event data.
* Perform exploratory data analysis.
* Understand patient activity sequences.
* Identify repeated activities and potential bottlenecks.
* Analyze transition and waiting times.
* Discover the actual hospital workflow using PM4Py.
* Generate formal process models.
* Compare actual patient journeys with the expected workflow.
* Perform conformance checking.
* Build an interactive Power BI dashboard.
* Present actionable process insights.

# 4. Week 1 – Data Preparation & Exploratory Analysis

## 4.1 Event Log Generation

A Python-based event generator was developed to simulate hospital patient journeys.

The generated event log contains:

* Unique patient identifiers (`Case_ID`)
* Hospital activities (`Activity_Name`)
* Activity timestamps (`Timestamp`)

The generated dataset contains:

* **200 patients**
* **883 events**

## 4.2 Data Cleaning

The `clean_events.py` script was developed to prepare the raw event log for analysis.

The cleaning process includes:

* Missing value checking
* Timestamp validation
* Duplicate checking
* Data standardization
* Preparation of the cleaned event log

The cleaned dataset contains:

```text
Original rows: 883
Final cleaned rows: 883
Rows removed: 0
Unique patients: 200
```

The cleaned event log is stored at:

```text
data/hospital_event_log_clean.csv
```

## 4.3 Exploratory Data Analysis

Basic EDA was performed using:

```text
notebooks/eda.ipynb
```

The analysis includes:

* Dataset overview
* Number of patients
* Number of events
* Activity distribution
* Average events per patient
* Repeated Triage analysis
* Triage → X-Ray → Triage loop analysis
* X-Ray → Triage waiting-time analysis
* Activity visualizations

A repeated Triage rate of **36.5%** was identified during the initial analysis.

This value is treated as a **Repeated Triage Rate KPI** and is used as one indicator in the bottleneck analysis.

> **Note:** Repeated Triage is treated as an observed process pattern rather than the bottleneck by itself. Waiting times, transition frequencies, and conformance results are also considered.

# 5. Bottleneck Analysis

The bottleneck analysis focused on identifying repeated and potentially inefficient process patterns.

The main pattern identified was:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

Out of the 200 patient cases:

* **73 patients** experienced the Triage → X-Ray → Triage loop.
* This represents **36.5% of all patient cases**.

The repeated Triage pattern was therefore identified as the primary process bottleneck requiring further investigation.

The finding was initially identified through EDA and was subsequently examined using formal PM4Py process discovery and conformance checking.

### Status

**Completed**

# 6. Waiting-Time Analysis

Waiting-time analysis was performed to understand the time spent between consecutive activities in the patient journey.

Particular attention was given to transitions associated with the identified process loop, including:

```text
X-Ray → Triage
```

Waiting-time analysis helps complement the bottleneck analysis by considering not only how frequently a transition or loop occurs, but also how much time is associated with the patient movement between activities.

The analysis also considered important process transitions such as:

```text
Triage → X-Ray
X-Ray → Triage
Triage → Doctor Consultation
Doctor Consultation → X-Ray
```

The resulting waiting-time information is being incorporated into the Power BI dashboard through the **Average Wait Time** KPI and transition/waiting-time visualizations.

### Status

**Completed – Dashboard Integration In Progress**

> The final Average Wait Time value will be documented after the dashboard calculation is completed and validated.

# 7. Week 2 – Process Mining

## 7.1 PM4Py Process Discovery

PM4Py was introduced to discover the actual patient workflow from the cleaned event log.

The cleaned event log was used as the input for process discovery.

The PM4Py workflow successfully generated:

* Directly-Follows Graph (DFG)
* Petri Net process model
* Process-map visualization

The process discovery script was successfully executed from a fresh clone of the repository.

### Status

**Completed – PASS**

## 7.2 Directly-Follows Graph

The Directly-Follows Graph represents transitions between consecutive hospital activities.

It helps identify:

* Common activity transitions
* Frequently occurring process paths
* Process loops
* Repeated transitions
* Potentially unusual activity sequences

The DFG provides a formal process-level representation of the patterns initially identified during EDA.

The following loop-back pattern was observed:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

## 7.3 Petri Net Process Model

A Petri Net process model was generated using PM4Py.

The Petri Net provides a structured representation of:

* Activities
* Process transitions
* Possible patient paths
* Process flow relationships
* Repeated process behavior

The generated process model was successfully verified during fresh-clone testing.

### Status

**Completed – PASS**

# 8. Conformance Checking

Conformance checking was performed to compare the actual patient activity sequences against the expected hospital workflow.

The reference workflow used for the analysis was:

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

Each of the **200 patient cases** was checked against this ideal pathway.

A patient was considered **conformant** if the recorded activity sequence exactly matched:

```text
Triage → X-Ray → Doctor Consult → Discharge
```

without repeated or additional activities.

## 8.1 Conformance Results

| Metric                 | Result |
| ---------------------- | -----: |
| Total Patients         |    200 |
| Conformant Patients    |    127 |
| Deviating Patients     |     73 |
| Conformance Percentage |  63.5% |
| Deviation Percentage   |  36.5% |

## 8.2 Key Finding

Out of 200 patient cases:

* **127 patients (63.5%)** followed the ideal pathway.
* **73 patients (36.5%)** deviated from the expected pathway.

The **36.5% deviation rate** is consistent with the repeated Triage pattern identified during earlier analysis.

The same pattern was observed through three analytical stages:

1. **Manual EDA / Bottleneck Analysis** – 73 out of 200 patients experienced the Triage → X-Ray → Triage loop.
2. **PM4Py Process Discovery** – the same loop-back pattern was represented in the discovered process.
3. **Conformance Checking** – 73 patient cases were identified as deviating from the ideal pathway.

The consistency across these analyses strengthens confidence that the observed process deviation is a significant pattern in the generated event log.

## 8.3 Interpretation

The results indicate that:

* **63.5%** of analyzed patient cases followed the defined ideal pathway.
* **36.5%** of cases deviated from the expected pathway.

The major observed deviation is associated with the repeated Triage pattern after X-Ray.

A possible explanation, based on the original project hypothesis, could be missing information or paperwork. However, the root cause has **not been confirmed** by the available event data and requires further investigation.

### Status

**Completed – Results Verified**

# 9. Power BI Dashboard

Power BI is being used to consolidate the process-mining and healthcare operational findings into an interactive dashboard.

The dashboard has now been expanded to include the core process KPIs and supporting process-analysis visuals.

## 9.1 Core KPI Cards

The dashboard includes / is being finalized with four main KPI cards:

### 1. Total Cases

Displays the total number of patient cases analyzed.

**Current verified value: 200**

### 2. Conformant %

Shows the percentage of patient cases that followed the defined expected pathway.

**Current verified value: 63.5%**

### 3. Deviating %

Shows the percentage of patient cases that deviated from the expected pathway.

**Current verified value: 36.5%**

This is preferred as the dashboard label rather than “Bottleneck %” because the metric specifically represents conformance deviation.

### 4. Average Wait Time

Shows the average waiting time between relevant patient activities.

**Final dashboard value: To be added after final calculation validation.**

## 9.2 Dashboard Visual Structure

The current dashboard layout is organized to provide a clear progression from high-level KPIs to detailed process analysis.

### Top Section – KPI Cards

```text
Total Cases | Conformant % | Deviating % | Average Wait Time
```

This provides an immediate overview of the patient process performance.

### Middle Section – Activity and Conformance Analysis

The dashboard includes:

* Activity Counts
* Conformance Split
* Patient/process activity distribution

The **Conformance Split** visualizes:

```text
63.5% Conformant
        vs
36.5% Deviating
```

### Lower Section – Process Analysis

The dashboard includes / is being developed with:

* Transition analysis
* Waiting-time analysis
* Process map
* Bottleneck / repeated activity analysis

This section allows the user to move from overall KPIs to the specific process behavior behind those KPIs.

## 9.3 Dashboard Number Validation

The dashboard metrics are being cross-checked against the documented process findings.

The currently verified values are:

```text
Total Cases      = 200
Conformant       = 127
Conformant %     = 63.5%
Deviating        = 73
Deviating %      = 36.5%
Repeated Triage  = 73 / 200 = 36.5%
```

The **36.5%** value is consistent with the repeated Triage finding documented in the process analysis.

The dashboard therefore uses:

* **Deviating %** for the conformance KPI.
* **Repeated Triage Rate** when specifically referring to the repeated Triage finding.

This avoids using “Bottleneck %” as a generic label for two different concepts.

### Current Status

**Dashboard – In Progress / Core KPIs Being Finalized**

# 10. BigQuery / dbt Scope Decision

BigQuery and dbt were evaluated as possible additions to the project workflow.

For the current implementation, the team decided to **defer BigQuery and dbt**.

The decision allows the project to remain focused on completing the core process-mining and dashboard workflow using the existing event-log architecture.

The current implementation is:

```text
CSV
 ↓
Python
 ↓
Pandas
 ↓
EDA
 ↓
PM4Py
 ↓
Process Analysis
 ↓
Power BI
```

BigQuery and dbt may be considered in a future version if scalable data warehousing or transformation requirements arise.

### Status

**Deferred – Scope Decision Made**

# 11. Current Technology Stack

## 11.1 Technologies Currently Used

| Technology | Purpose                              | Status         |
| ---------- | ------------------------------------ | -------------- |
| Python     | Event generation and data processing | ✅ Completed    |
| Pandas     | Data cleaning and analysis           | ✅ Completed    |
| Matplotlib | Basic visualization                  | ✅ Completed    |
| CSV        | Event-log storage                    | ✅ Current      |
| PM4Py      | Process mining and process discovery | ✅ Completed    |
| Graphviz   | Process visualization support        | ✅ Completed    |
| Git        | Version control                      | ✅ Current      |
| GitHub     | Team collaboration                   | ✅ Current      |
| Power BI   | Interactive dashboard                | 🔄 In Progress |

## 11.2 Technologies Deferred

| Technology | Purpose                          | Status     |
| ---------- | -------------------------------- | ---------- |
| BigQuery   | Data warehouse, if required      | ⏸ Deferred |
| dbt        | Data transformation, if required | ⏸ Deferred |

# 12. Fresh-Clone Testing

The project was tested from a fresh clone to verify that the merged implementation works correctly for a new team member.

The following were verified:

```text
Repository cloning
Dependency installation
Event generation
Data cleaning
EDA workflow
PM4Py process discovery
DFG generation
Petri Net generation
Process map generation
README setup instructions
```

### PM4Py Fresh-Clone Result

**Status: PASS**

The PM4Py process discovery script executed successfully and generated the expected process-mining outputs.

# 13. Key Findings So Far

The current analysis has identified the following observations:

## Finding 1 – Repeated Triage

A repeated Triage rate of:

**36.5%**

was identified during the initial EDA.

This corresponds to:

**73 out of 200 patient cases.**

The repeated Triage rate is used as a process-analysis KPI.

## Finding 2 – Process Loop

The following loop-back pattern is present in the event data:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

This pattern represents the major repeated process behavior identified during the analysis.

## Finding 3 – Waiting-Time Analysis

Waiting-time analysis was performed to examine the time between consecutive activities.

The analysis provides additional context for understanding process delays and is being incorporated into the Power BI dashboard through the Average Wait Time KPI and transition/waiting-time visuals.

## Finding 4 – PM4Py Process Discovery

PM4Py successfully discovered the patient process from the cleaned event log.

Both the DFG and Petri Net process model were generated successfully.

The formal process model provides process-level evidence supporting the patterns identified during the earlier EDA.

## Finding 5 – Conformance Analysis

Formal conformance checking was completed by comparing the 200 patient cases against the expected workflow:

```text
Triage → X-Ray → Doctor Consult → Discharge
```

The analysis identified:

* **127 conformant patients (63.5%)**
* **73 deviating patients (36.5%)**

The 36.5% deviation rate is consistent with the previously identified repeated Triage pattern.

This provides additional evidence that the repeated Triage pattern represents a significant process deviation and potential bottleneck.

## Finding 6 – Dashboard KPI Alignment

The Power BI dashboard is being expanded to consolidate the verified findings.

The current core KPI structure is:

```text
Total Cases
Conformant %
Deviating %
Average Wait Time
```

The conformance split and repeated Triage finding have been cross-checked against the process analysis.

# 14. Current Project Status

| Component                      | Status                     |
| ------------------------------ | -------------------------- |
| Event generation               | ✅ Completed                |
| Raw CSV generation             | ✅ Completed                |
| Data cleaning                  | ✅ Completed                |
| Data dictionary                | ✅ Completed                |
| Basic EDA                      | ✅ Completed                |
| Repeated Triage analysis       | ✅ Completed                |
| Bottleneck analysis            | ✅ Completed                |
| Waiting-time analysis          | ✅ Completed                |
| PM4Py process discovery        | ✅ Completed                |
| DFG generation                 | ✅ Completed                |
| Petri Net generation           | ✅ Completed                |
| Process-map interpretation     | ✅ Completed                |
| Fresh-clone testing            | ✅ Completed                |
| BigQuery evaluation            | ✅ Decision Made – Deferred |
| dbt evaluation                 | ✅ Decision Made – Deferred |
| Conformance checking           | ✅ Completed                |
| Conformance results validation | ✅ Completed                |
| Power BI core KPIs             | 🔄 In Progress             |
| Power BI dashboard refinement  | 🔄 In Progress             |
| Mid-Review documentation       | 🔄 In Progress             |
| Final presentation             | ⏳ Upcoming                 |

# 15. Mid-Review Deliverables

The Mid-Review will demonstrate the complete progress achieved across data preparation, process analysis, process mining, conformance checking, and dashboard development.

## Week 1 – Data Preparation & Initial Analysis

```text
Data Generation
      ↓
Data Cleaning
      ↓
EDA
      ↓
Repeated Triage Analysis
      ↓
Bottleneck Identification
      ↓
Waiting-Time Analysis
```

## Week 2 – Process Mining & Dashboard Development

```text
PM4Py Process Discovery
      ↓
Directly-Follows Graph
      ↓
Petri Net Process Model
      ↓
Process Map Interpretation
      ↓
Conformance Checking
      ↓
Power BI Dashboard
```

## Mid-Review Presentation Content

The final Mid-Review presentation will include:

* Project overview
* Problem statement
* Project objectives
* Data preparation
* EDA findings
* Bottleneck analysis
* Waiting-time analysis
* PM4Py process discovery
* Directly-Follows Graph
* Petri Net process model
* Process-map interpretation
* Conformance-checking results
* Power BI dashboard
* Core dashboard KPIs
* BigQuery/dbt scope decision
* Current project status
* Key findings
* Next steps

## Core Results to Present

### Bottleneck Finding

```text
Triage → X-Ray → Triage
```

**73 / 200 patients = 36.5%**

### Conformance Finding

```text
127 conformant cases = 63.5%
73 deviating cases   = 36.5%
```

### Dashboard KPIs

```text
Total Cases
Conformant %
Deviating %
Average Wait Time
```

The final Average Wait Time value will be inserted after the dashboard calculation is finalized and validated.

# 16. Next Steps

The remaining activities before the Mid-Review are:

1. Complete the first working version of the Power BI dashboard.
2. Finalize the Average Wait Time KPI.
3. Add the verified conformance split to the dashboard.
4. Finalize transition and waiting-time visualizations.
5. Refine the process-map visualization.
6. Add the DFG and Petri Net screenshots to the Mid-Review.
7. Cross-check all dashboard numbers against the documented analysis.
8. Integrate bottleneck, waiting-time, transition, and conformance findings.
9. Perform a final validation pass.
10. Finalize the Mid-Review document and presentation.
11. Prepare the project demonstration for the Mid-Review scheduled for **August 25–27**.

# 17. Conclusion

CareFlow has progressed from initial hospital event-log generation and data preparation to exploratory analysis, bottleneck identification, waiting-time analysis, formal process discovery using PM4Py, conformance checking, and Power BI dashboard development.

The main process pattern identified so far is the:

```text
Triage → X-Ray → Triage
```

loop, which affects **73 out of 200 patient cases (36.5%)**.

Formal conformance checking further identified **127 conformant cases (63.5%)** and **73 deviating cases (36.5%)** when comparing patient journeys against the defined expected pathway.

The agreement between the earlier process analysis, PM4Py process discovery, and conformance results provides consistent evidence of the observed process deviation.

The current Power BI dashboard brings these findings together through core KPIs for **Total Cases, Conformant %, Deviating %, and Average Wait Time**, supported by activity counts, conformance visualization, transition/waiting-time analysis, and the discovered process map.

BigQuery and dbt have been intentionally deferred from the current scope so that the team can focus on completing and validating the core process-mining and dashboard workflow.

The final CareFlow solution will provide a process-oriented view of patient journeys and help identify where hospital workflows may be inefficient or require further investigation.
