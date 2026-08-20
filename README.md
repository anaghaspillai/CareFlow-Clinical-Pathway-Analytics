# CareFlow – Clinical Pathway Process Mining

## 📌 Project Overview

**CareFlow** is a healthcare process analytics and process mining project designed to analyze patient journeys through hospital workflows.

Traditional hospital dashboards can show metrics such as average waiting time, but they may not clearly reveal the actual sequence of activities a patient experiences or where operational bottlenecks occur.

CareFlow uses timestamped patient event logs to discover hospital processes, analyze patient journeys, identify repeated activities and potential process bottlenecks, measure waiting and transition times, compare actual patient paths against an expected workflow, perform conformance checking, and present insights through a Power BI dashboard.

---

## 💡 Proposed Solution

CareFlow creates and analyzes a chronological event log representing patient journeys through a hospital.

The current implementation follows:

```text
Patient Event Data
        ↓
Data Generation
        ↓
Data Cleaning & Transformation
        ↓
Event Log Preparation
        ↓
Exploratory Data Analysis
        ↓
Bottleneck & Waiting-Time Analysis
        ↓
PM4Py Process Discovery
        ↓
DFG / Petri Net Process Model
        ↓
Conformance Checking
        ↓
Power BI Dashboard
        ↓
Healthcare Process Insights
```

---

# 🔍 Key Objectives

* Generate realistic timestamped hospital event logs.
* Standardize the event data for process mining.
* Discover the actual patient workflow.
* Generate formal process models using PM4Py.
* Analyze process transitions and patient journeys.
* Identify potential process bottlenecks.
* Analyze waiting and transition times between activities.
* Detect repeated activities and loop-backs.
* Compare actual patient journeys with the expected workflow.
* Perform conformance checking.
* Build an interactive Power BI dashboard.
* Provide insights that can support hospital process improvement.

---

# 🛠️ Technology Stack

### Current Technologies

| Technology   | Purpose                              | Status         |
| ------------ | ------------------------------------ | -------------- |
| Python       | Event-log generation and processing  | ✅ Completed    |
| Pandas       | Data cleaning and analysis           | ✅ Completed    |
| Matplotlib   | Basic visualization                  | ✅ Completed    |
| CSV          | Event-log storage                    | ✅ Current      |
| PM4Py        | Process discovery and process mining | ✅ Completed    |
| Graphviz     | Process-map visualization            | ✅ Completed    |
| Git & GitHub | Version control and collaboration    | ✅ Current      |
| Power BI     | Dashboard development                | 🔄 In Progress |

### Deferred Technologies

| Technology | Status     | Decision                       |
| ---------- | ---------- | ------------------------------ |
| BigQuery   | ⏸ Deferred | Not required for current scope |
| dbt        | ⏸ Deferred | Not required for current scope |

The project is currently focused on completing the core process-mining workflow using the existing CSV-based event log.

---

# 🔬 Analysis Completed So Far

## 1. Exploratory Data Analysis

Basic EDA was performed on the cleaned hospital event log.

The analysis includes:

* Dataset overview
* Number of patients and events
* Activity distribution
* Average events per patient
* Repeated Triage activity analysis
* Triage → X-Ray → Triage loop-back analysis
* X-Ray → Triage waiting-time analysis
* Activity visualizations

The dataset contains:

* **200 patient cases**
* **883 recorded events**

---

## 2. Bottleneck Analysis

The initial EDA identified a repeated process pattern:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

A total of:

**73 out of 200 patients**

experienced this loop.

This represents:

**36.5% of patient cases**

The Triage → X-Ray → Triage pattern was therefore identified as the primary process bottleneck requiring further investigation.

> **Note:** The repeated Triage pattern is treated as an observed process deviation and potential bottleneck. The underlying operational/root cause has not yet been confirmed.

---

## 3. Waiting-Time Analysis

Waiting-time analysis was performed to understand the time spent between consecutive hospital activities.

Particular attention was given to transitions associated with the identified bottleneck, including:

```text
X-Ray → Triage
```

The analysis also considered important transitions such as:

```text
Triage → X-Ray
X-Ray → Triage
Triage → Doctor Consultation
Doctor Consultation → X-Ray
```

Waiting-time analysis complements bottleneck analysis by considering both the frequency of process transitions and the time associated with movement between activities.

The waiting-time analysis is being incorporated into the Power BI dashboard through Average Wait Time and transition analysis.

### Status

**✅ Completed – Dashboard Integration In Progress**

> The final Average Wait Time value will be added after the dashboard calculation is finalized and validated.

---

# 4. PM4Py Process Discovery

PM4Py was introduced to move from manual Pandas-based process analysis to formal process discovery.

The cleaned hospital event log was provided as input to the PM4Py workflow.

The process discovery implementation successfully generated:

* Directly-Follows Graph (DFG)
* Petri Net process model
* Process-map visualizations

### Status

**✅ Completed – Verified**

The PM4Py workflow was also tested from a fresh clone of the repository.

---

## 4.1 Directly-Follows Graph

The Directly-Follows Graph represents transitions between consecutive hospital activities.

It provides a process-level view of:

* Common activity transitions
* Frequently occurring paths
* Repeated transitions
* Loop-back patterns
* Patient-flow relationships

The DFG provides formal process evidence supporting the process patterns initially identified during EDA.

The following loop was observed:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

---

## 4.2 Petri Net Process Model

A Petri Net process model was generated using PM4Py.

The model provides a structured representation of the discovered patient workflow and helps visualize:

* Activities
* Transitions
* Process paths
* Repeated process behavior
* Possible deviations

The generated Petri Net was successfully verified during the PM4Py workflow testing.

### Status

**✅ Completed – Verified**

---

# 5. Conformance Checking

Conformance checking was added to compare actual patient journeys against the expected hospital pathway.

The reference pathway used for the analysis is:

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

Each of the **200 patient cases** was compared against this ideal pathway.

A patient was considered conformant if their recorded activity sequence exactly matched:

```text
Triage → X-Ray → Doctor Consult → Discharge
```

without repeated or additional activities.

## 5.1 Conformance Results

| Metric                 | Result |
| ---------------------- | -----: |
| Total Patients         |    200 |
| Conformant Patients    |    127 |
| Deviating Patients     |     73 |
| Conformance Percentage |  63.5% |
| Deviation Percentage   |  36.5% |

### Key Finding

**127 patients (63.5%)** followed the ideal pathway, while **73 patients (36.5%)** deviated from it.

The 36.5% deviation rate is consistent with the previously identified:

```text
Triage → X-Ray → Triage
```

loop.

The pattern has now been observed through multiple analytical approaches:

```text
Manual EDA
    ↓
Bottleneck Identification
    ↓
PM4Py Process Discovery
    ↓
Conformance Checking
```

This consistency strengthens confidence that the identified process deviation represents a significant pattern in the generated event log.

> **Important:** The underlying operational/root cause of the loop has not yet been confirmed and requires further investigation.

### Status

**✅ Completed – Results Verified**

---

# 📊 Power BI Dashboard

Power BI is being used to consolidate the process-mining findings into an interactive dashboard.

The dashboard development has progressed to include the core process KPIs, conformance analysis, activity analysis, and transition/process analysis.

## KPI Cards

The dashboard currently includes / is being finalized with four main KPI areas:

### 1. Total Cases

Displays the total number of patient cases analyzed.

**Verified value: 200**

### 2. Conformant %

Shows the percentage of patient cases that followed the defined expected pathway.

**Verified value: 63.5%**

### 3. Deviating %

Shows the percentage of patient cases that deviated from the expected pathway.

**Verified value: 36.5%**

This label is preferred over "Bottleneck %" because the metric specifically represents conformance deviation.

### 4. Average Wait Time

Shows the average waiting time between relevant patient activities.

**Final value: To be added after final calculation validation.**

---

## Conformance Split

A **Conformance Split** visual has been added to the dashboard to clearly compare conformant and deviating patient journeys.

```text
Conformant
127 / 200 = 63.5%

        VS

Deviating
73 / 200 = 36.5%
```

This visual provides a direct summary of patient-path compliance with the expected workflow.

---

## Activity Analysis

The dashboard includes activity-level analysis to understand the distribution of hospital activities across the event log.

This helps connect the overall patient KPIs with the individual activities occurring throughout the patient journey.

---

## Transition Analysis

Transition analysis is being used to examine how patients move between consecutive hospital activities.

Important transitions include:

```text
Triage → X-Ray
X-Ray → Triage
Triage → Doctor Consultation
Doctor Consultation → X-Ray
```

Particular attention is given to:

```text
X-Ray → Triage
```

because it contributes to the observed:

```text
Triage → X-Ray → Triage
```

process loop.

---

## Dashboard Structure

The dashboard is organized from high-level KPIs to detailed process analysis.

### Top Section

```text
Total Cases | Conformant % | Deviating % | Average Wait Time
```

### Middle Section

* Activity Counts
* Conformance Split
* Patient/process activity distribution

### Lower Section

* Transition analysis
* Waiting-time analysis
* Process map
* Bottleneck / repeated activity analysis

This structure allows users to move from overall process performance to the specific patient-flow patterns behind the KPIs.

---

## Dashboard Number Validation

The dashboard values are being cross-checked against the documented process analysis.

Currently verified:

```text
Total Cases      = 200
Conformant       = 127
Conformant %     = 63.5%
Deviating        = 73
Deviating %      = 36.5%
Repeated Triage  = 73 / 200 = 36.5%
```

The dashboard therefore distinguishes between:

* **Deviating %** → Conformance deviation.
* **Repeated Triage Rate** → Specific repeated-process finding.

This avoids using one generic "Bottleneck %" metric for two different concepts.

### Dashboard Status

**🔄 In Progress – Core KPIs and Process Analysis Implemented**

---

# 🔄 Current Project Workflow

The implemented workflow is now:

```text
Python Event Generator
        ↓
Hospital Event Log
        ↓
Raw CSV
        ↓
clean_events.py
        ↓
Cleaned CSV
        ↓
EDA
        ↓
Bottleneck Analysis
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
Final Process Insights
```

---

# 🗄️ BigQuery / dbt Scope Decision

BigQuery and dbt were considered as part of the planned data-engineering workflow.

After evaluating the current project scope, the team decided to **defer BigQuery and dbt** rather than introduce an additional data-engineering layer at this stage.

The current implementation therefore remains:

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
Power BI
```

### Decision

**BigQuery: Deferred**

**dbt: Deferred**

This decision allows the team to focus on completing and validating the core process-mining workflow while keeping the project manageable within the current timeline.

BigQuery and dbt may be considered in a future version if scalable data warehousing or transformation requirements arise.

---

# 📅 Updated Project Development Plan

## Week 1 – Data Preparation & Initial Analysis

### Completed

* Generate simulated hospital event logs using Python.
* Create realistic patient journeys.
* Introduce operational inefficiencies and loop-backs.
* Store the generated event log as CSV.
* Clean and prepare event data using `clean_events.py`.
* Perform basic exploratory data analysis.
* Investigate the Triage → X-Ray → Triage loop.
* Analyze repeated activities.
* Analyze initial waiting-time patterns.
* Prepare the cleaned data for process mining.

### Status: ✅ Completed

---

# Week 2 – Process Discovery, Conformance & Dashboard Development

The project has progressed beyond the original Week 2 scope and is currently ahead in several areas.

## Monday – Formal Process Discovery

* Implement PM4Py process discovery.
* Generate a Directly-Follows Graph.
* Generate a Petri Net process model.
* Verify the process-map outputs.
* Document the discovered process.

### Status: ✅ Completed

---

## Tuesday – Data Platform Decision & Dashboard Direction

* Evaluate whether BigQuery/dbt is required.
* Decide whether to introduce the additional data-engineering layer.
* Continue with the CSV/Python/PM4Py architecture.
* Continue Power BI dashboard development.

### Status

**✅ BigQuery/dbt Deferred**

**🔄 Power BI Dashboard In Progress**

---

## Wednesday – Conformance Checking

* Compare actual patient paths against the ideal workflow.
* Calculate conformant and deviating cases.
* Identify major deviation patterns.
* Validate the relationship between conformance deviations and the observed Triage loop.
* Incorporate conformance findings into the dashboard and Mid-Review documentation.

### Status: ✅ Completed

Current verified results:

```text
Total Patients      = 200
Conformant          = 127 (63.5%)
Deviating           = 73  (36.5%)
```

---

## Thursday – Power BI Dashboard Development

* Build the working Power BI dashboard.
* Add Total Cases KPI.
* Add Conformant % KPI.
* Add Deviating % KPI.
* Add Conformance Split.
* Add activity analysis.
* Add transition analysis.
* Continue waiting-time analysis.
* Refine dashboard layout and usability.

### Status

**🔄 In Progress**

The core KPI and conformance visuals have been implemented and are being refined.

---

## Friday – Consolidation & Validation

Planned activities:

* Consolidate PM4Py process discovery.
* Consolidate bottleneck and waiting-time findings.
* Validate conformance results.
* Complete dashboard integration.
* Cross-check dashboard metrics.
* Finalize Mid-Review documentation.
* Prepare the Mid-Review presentation and demonstration.

### Status: 🔄 In Progress

---

# 🎓 Mid-Review Preparation

The Mid-Review is scheduled for **August 25–27**.

The presentation will bring together the progress achieved so far.

The Mid-Review will demonstrate:

### 1. Bottleneck Findings

```text
Triage → X-Ray → Triage
```

**73 / 200 patients = 36.5%**

### 2. Waiting-Time Findings

Analysis of time spent between consecutive patient activities, with particular attention to transitions related to the identified bottleneck.

### 3. Process Discovery

Formal PM4Py outputs:

* Directly-Follows Graph
* Petri Net process model
* Process-map interpretation

### 4. Conformance Checking

Verified comparison between actual patient journeys and the expected pathway:

```text
127 conformant cases → 63.5%
73 deviating cases   → 36.5%
```

### 5. BigQuery / dbt Decision

The project currently uses:

```text
CSV + Python/Pandas + PM4Py + Power BI
```

BigQuery and dbt have been **deferred from the current implementation** to maintain focus on the core process-mining and dashboard objectives.

### 6. Power BI Dashboard

The dashboard consolidates:

* Total patient cases
* Conformance percentage
* Deviation percentage
* Conformance split
* Activity counts
* Process transitions
* Waiting-time analysis
* Bottleneck findings
* Process map

---

# 📊 Current Project Status

| Component                      | Status                     |
| ------------------------------ | -------------------------- |
| Event Generation               | ✅ Completed                |
| Data Cleaning                  | ✅ Completed                |
| EDA                            | ✅ Completed                |
| Bottleneck Analysis            | ✅ Completed                |
| Waiting-Time Analysis          | ✅ Completed                |
| PM4Py Process Discovery        | ✅ Completed                |
| DFG Generation                 | ✅ Completed                |
| Petri Net Generation           | ✅ Completed                |
| Process Map Interpretation     | ✅ Completed                |
| BigQuery/dbt Evaluation        | ✅ Decision Made – Deferred |
| Conformance Checking           | ✅ Completed                |
| Conformance Results Validation | ✅ Completed                |
| Power BI Total Cases KPI       | ✅ Completed                |
| Power BI Conformant % KPI      | ✅ Completed                |
| Power BI Deviating % KPI       | ✅ Completed                |
| Power BI Conformance Split     | ✅ Completed                |
| Power BI Activity Analysis     | ✅ Completed                |
| Power BI Transition Analysis   | 🔄 In Progress             |
| Power BI Average Wait Time     | 🔄 In Progress             |
| Power BI Dashboard Refinement  | 🔄 In Progress             |
| Mid-Review Documentation       | 🔄 In Progress             |
| Final Presentation             | ⏳ Upcoming                 |

---

# 🎯 Current Key Findings

## Finding 1 – Major Process Loop

The analysis identified:

```text
Triage → X-Ray → Triage
```

affecting:

**73 out of 200 patients (36.5%)**

---

## Finding 2 – Waiting-Time Analysis

Waiting-time analysis provides additional information about delays between activities and is being integrated with transition analysis in the Power BI dashboard.

---

## Finding 3 – PM4Py Confirmation

The manually identified patient-flow patterns were subsequently examined using formal PM4Py process discovery.

The DFG and Petri Net provide a process-level representation of the hospital workflow.

---

## Finding 4 – Conformance

Conformance checking identified:

**127 conformant cases (63.5%)**

and

**73 deviating cases (36.5%)**

The deviation percentage is consistent with the previously identified repeated Triage pattern.

---

## Finding 5 – Dashboard Conformance Split

The Power BI dashboard now visually represents:

```text
63.5% Conformant
        vs
36.5% Deviating
```

This provides a clear high-level summary of patient-path compliance.

---

## Finding 6 – Dashboard Process Analysis

The dashboard is being expanded beyond basic KPIs to connect patient-level outcomes with process behavior.

The current process-analysis focus includes:

```text
Activity Counts
      ↓
Conformance Split
      ↓
Transitions
      ↓
Waiting Times
      ↓
Bottleneck / Process Loop
```

---

# 🚀 Next Steps

Before the Mid-Review:

1. Complete the first working Power BI dashboard.
2. Finalize the Average Wait Time KPI.
3. Finalize transition and waiting-time visualizations.
4. Refine the process-map visualization.
5. Add DFG/Petri Net screenshots to the presentation.
6. Cross-check all dashboard numbers against the documented analysis.
7. Integrate bottleneck, waiting-time, transition, and conformance findings.
8. Perform final validation of all reported metrics.
9. Finalize the Mid-Review documentation.
10. Prepare the Mid-Review presentation and project demonstration.

After the Mid-Review, remaining time can be used for:

* Dashboard refinement
* Deeper root-cause investigation
* Additional process-mining analysis
* Improved process visualizations
* Additional healthcare process insights

---

# 🎯 Expected Final Outcome

The final **CareFlow** system will provide a process-oriented view of hospital operations rather than relying only on traditional numerical KPIs.

The completed solution is expected to combine:

```text
Hospital Event Data
        ↓
Data Cleaning & Preparation
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
Power BI Dashboard
        ↓
Healthcare Process Insights
```

The final system will help reveal:

* How patients move through hospital activities.
* Where process delays occur.
* Which activities are frequently repeated.
* Where bottlenecks and loop-backs exist.
* How patient journeys vary.
* Which patient paths deviate from the expected workflow.
* Which transitions require further investigation.
* Where process improvements may be required.

The final Power BI dashboard is expected to provide a consolidated view of:

* **Total Patients / Cases**
* **Conformance Percentage**
* **Deviation Percentage**
* **Average Waiting Time**
* **Activity Distribution**
* **Process Transitions**
* **Repeated Activity / Bottleneck Analysis**
* **Conformance Split**
* **Discovered Process Map**

The project will combine **process mining, data analytics, conformance checking, and Power BI visualization** to provide a clearer understanding of healthcare workflows.

The identified **Triage → X-Ray → Triage** loop and the **36.5% deviation rate** will serve as important areas for further investigation, while the final analysis will avoid assuming a root cause unless it can be supported by the available event data.

Ultimately, CareFlow aims to demonstrate how process mining can transform timestamped hospital event data into meaningful process insights that can support the identification of inefficient workflows and potential areas for operational improvement.
