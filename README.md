# CareFlow – Clinical Pathway Process Mining

## 📌 Project Overview

**CareFlow** is a healthcare process analytics and process mining project designed to analyze patient journeys through hospital workflows.

Traditional hospital dashboards can show metrics such as patient counts and average waiting time, but they may not clearly reveal the actual sequence of activities a patient experiences or where process deviations and potential bottlenecks occur.

CareFlow uses timestamped patient event logs to discover hospital processes, analyze patient journeys, identify repeated activities and potential bottlenecks, measure waiting and transition times, compare actual patient paths against an expected workflow, and present insights through an interactive Power BI dashboard.

---

## 💡 Proposed Solution

CareFlow creates and analyzes a chronological event log representing patient journeys through a hospital.

The implemented workflow is:

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
* Standardize and clean event data for process mining.
* Discover the actual patient workflow.
* Generate formal process models using PM4Py.
* Analyze process transitions and patient journeys.
* Identify repeated activities and potential process bottlenecks.
* Analyze waiting and transition times between activities.
* Detect repeated activities and process loop-backs.
* Compare actual patient journeys with the expected workflow.
* Perform conformance checking.
* Build an interactive Power BI dashboard.
* Provide process insights that can support hospital workflow improvement.

---

# 🛠️ Technology Stack

## Current Technologies

| Technology   | Purpose                              
| ------------ | ------------------------------------ 
| Python       | Event-log generation and processing
| Pandas       | Data cleaning and analysis           
| Matplotlib   | Basic visualization                  
| CSV          | Event-log storage                    
| PM4Py        | Process discovery and process mining 
| Graphviz     | Process-map visualization            
| Git & GitHub | Version control and collaboration    
| Power BI     | Interactive dashboard development  
## Deferred Technologies

| Technology | Status     | Decision                       |
| ---------- | ---------- | ------------------------------ |
| BigQuery   | ⏸ Deferred | Not required for current scope |
| dbt        | ⏸ Deferred | Not required for current scope |

The project currently focuses on completing and validating the core process-mining workflow using the existing CSV-based event log.

---

# 📊 Dataset

The current hospital event log contains:

* **200 patient cases**
* **883 recorded events**

Each event contains information such as:

* `Case_ID` – Unique patient/case identifier
* `Activity_Name` – Hospital activity performed
* `Timestamp` – Time at which the activity occurred

The cleaned event log is used as the main input for EDA, process discovery, conformance checking, and Power BI analysis.

---

# 🔬 Analysis Completed So Far

## 1. Exploratory Data Analysis

Basic EDA was performed on the cleaned hospital event log using Python and Pandas.

The analysis includes:

* Dataset overview
* Number of patients and events
* Activity distribution
* Average events per patient
* Repeated Triage activity analysis
* Triage → X-Ray → Triage loop-back analysis
* X-Ray → Triage waiting-time analysis
* Activity visualizations

The analysis identified a repeated Triage pattern involving:

**73 out of 200 patients = 36.5%**

---

# 2. Bottleneck Analysis

The initial EDA identified the following repeated process pattern:

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

The Triage → X-Ray → Triage pattern was therefore identified as the primary process deviation and potential bottleneck requiring further investigation.

> The observed loop is treated as a process pattern requiring investigation. The underlying operational root cause has not yet been confirmed from the available event data.

### Status

**✅ Completed**

---

# 3. Waiting-Time Analysis

Waiting-time analysis was performed to understand the time spent between consecutive hospital activities.

Particular attention was given to transitions associated with the identified process pattern, including:

```text
X-Ray → Triage
```

The analysis also considered transitions such as:

```text
Triage → X-Ray
X-Ray → Triage
Triage → Doctor Consultation
Doctor Consultation → X-Ray
```

Waiting-time analysis complements the bottleneck analysis by examining not only how frequently a process pattern occurs, but also the time associated with transitions in the patient journey.

The results are being incorporated into the Power BI dashboard through waiting-time and transition analysis.

### Status

**✅ Analysis Completed**

---

# 4. PM4Py Process Discovery

PM4Py was used to move from manual Pandas-based process analysis to formal process discovery.

The cleaned hospital event log was provided as input to the PM4Py workflow.

The process discovery implementation successfully generated:

* Directly-Follows Graph (DFG)
* Petri Net process model
* Process-map visualizations

The PM4Py workflow was also tested successfully from a fresh clone of the repository.

### Status

**✅ Completed – Verified**

---

## 4.1 Directly-Follows Graph

The Directly-Follows Graph represents transitions between consecutive hospital activities.

It provides a process-level view of:

* Common activity transitions
* Frequently occurring paths
* Repeated transitions
* Loop-back patterns
* Patient-flow relationships

The DFG provides formal process evidence supporting the patterns initially identified during EDA.

The observed loop-back pattern is:

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

Conformance checking was performed to compare actual patient journeys against the expected hospital pathway.

The reference pathway used for the analysis was:

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consult
   ↓
Discharge
```

Each of the **200 patient cases** was compared against this expected pathway.

A patient was considered conformant if their recorded activity sequence exactly matched the defined expected pathway without repeated or additional activities.

## Conformance Results

| Metric                 | Result |
| ---------------------- | -----: |
| Total Patients         |    200 |
| Conformant Patients    |    127 |
| Deviating Patients     |     73 |
| Conformance Percentage |  63.5% |
| Deviation Percentage   |  36.5% |
| Total events           |   873  |
| Average Wait time      |  13.10 |
 
### Key Finding

**127 patients (63.5%)** followed the defined expected pathway, while **73 patients (36.5%)** deviated from it.

The 36.5% deviation rate is consistent with the previously identified Triage → X-Ray → Triage loop.

The pattern has been observed through multiple analytical stages:

```text
Manual EDA
    ↓
Bottleneck / Process Pattern Identification
    ↓
PM4Py Process Discovery
    ↓
Conformance Checking
```

This consistency provides supporting evidence that the identified process deviation is a significant pattern in the analyzed event log.

> The underlying operational/root cause of the deviation has not yet been confirmed and requires further investigation.

### Status

**✅ Completed – Results Verified**

---

# 📊 Power BI Dashboard

Power BI is being used to consolidate the process-mining findings into an interactive dashboard.

## Core KPIs

The dashboard includes / is being finalized with:

* **Total Cases**
* **Conformant %**
* **Deviating %**
* **Average Wait Time**

Current verified values:

```text
Total Cases  = 200
Conformant % = 63.5%
Deviating %  = 36.5%
Average Wait time = 13.10
```

The final Average Wait Time value is being validated as part of the dashboard development.

## Process Analysis

The dashboard includes / is being refined with:

* Activity distribution
* Patient transitions
* Conformance split
* Bottleneck / repeated activity analysis
* Waiting-time analysis
* Process-flow analysis
* Process-map representation

### Dashboard Status

**🔄 In Progress**

The dashboard is being refined and validated against the Python-based analysis results.

---

# 🔄 Current Project Workflow

The implemented workflow is:

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

# 🔄 Fresh-Clone Verification

The complete project workflow was tested from a fresh clone of the repository to verify that the project can be set up and executed correctly in a clean environment.

The following components were verified:

* Repository cloning and project structure
* Dependency installation
* Event-log generation
* Data cleaning
* EDA workflow
* PM4Py process discovery
* Directly-Follows Graph generation
* Petri Net generation
* Process-map generation
* README setup instructions

### Verification Status

**✅ PASS – Complete workflow verified successfully**

This verification helps ensure that the project is reproducible and that the documented setup instructions are consistent with the implementation.

---

# 📝 Documentation & Verification

Throughout the project development, the **README and project documentation were continuously updated** to reflect completed implementation steps, analysis findings, process-mining results, dashboard progress, and project decisions.

The project was also reviewed from a fresh clone to verify that the documented setup instructions and implementation workflow function correctly.

---

# 📅 Updated Project Development Plan

## Week 1 – Data Preparation & Initial Analysis

### Completed

* Generated simulated hospital event logs using Python.
* Created realistic patient journeys.
* Introduced operational inefficiencies and loop-backs.
* Stored the generated event log as CSV.
* Cleaned and prepared event data using `clean_events.py`.
* Performed basic exploratory data analysis.
* Investigated the Triage → X-Ray → Triage loop.
* Analyzed repeated activities.
* Analyzed initial waiting-time patterns.
* Prepared the cleaned data for process mining.

### Status

**✅ Completed**

---

# Week 2 – Process Discovery, Conformance & Dashboard Development

### Completed

* Implemented PM4Py process discovery.
* Generated the Directly-Follows Graph.
* Generated the Petri Net process model.
* Verified the process-map outputs.
* Performed conformance checking against the expected workflow.
* Verified 127 conformant and 73 deviating patient cases.
* Evaluated BigQuery and dbt and deferred them from the current scope.
* Developed and refined the Power BI dashboard.
* Added core process KPIs and supporting process-analysis visuals.
* Tested the project workflow from a fresh clone.
* Updated project documentation and README with the latest findings.
* Prepared the Mid-Review documentation and presentation.

### Status

**✅ Completed**

---

# 🎓 Mid-Review Preparation

The Mid-Review is scheduled for **August 25–27**.

The presentation will bring together the complete progress achieved so far.

## 1. Bottleneck / Process Pattern

The main identified process loop is:

```text
Triage → X-Ray → Triage
```

with:

**73 / 200 patients = 36.5%**

---

## 2. Waiting-Time Analysis

Waiting-time analysis examines the time spent between consecutive patient activities, with particular attention to transitions related to the identified process pattern.

---

## 3. Process Discovery

Formal PM4Py outputs include:

* Directly-Follows Graph
* Petri Net process model
* Process-map interpretation

---

## 4. Conformance Checking

Verified comparison between actual patient journeys and the expected pathway:

```text
127 conformant cases  → 63.5%
73 deviating cases    → 36.5%
```

---

## 5. BigQuery / dbt Decision

The project currently uses:

```text
CSV + Python/Pandas + PM4Py + Power BI
```

BigQuery and dbt have been **deferred from the current implementation** to maintain focus on the core process-mining and dashboard objectives.

---

## 6. Power BI Dashboard

The dashboard consolidates:

* Patient KPIs
* Process transitions
* Bottleneck findings
* Waiting-time analysis
* Conformance results
* Process insights

---

# 📊 Current Project Status

| Component                  | Status                     |
| -------------------------- | -------------------------- |
| Event Generation           | ✅ Completed                |
| Data Cleaning              | ✅ Completed                |
| EDA                        | ✅ Completed                |
| Bottleneck Analysis        | ✅ Completed                |
| Waiting-Time Analysis      | ✅ Completed                |
| PM4Py Process Discovery    | ✅ Completed                |
| DFG Generation             | ✅ Completed                |
| Petri Net Generation       | ✅ Completed                |
| Process Map Interpretation | ✅ Completed                |
| Fresh-Clone Verification   | ✅ Completed                |
| BigQuery/dbt Evaluation    | ✅ Decision Made – Deferred |
| Conformance Checking       | ✅ Completed                |
| README Updates             | ✅ Completed                |                
| Power BI Dashboard         | ✅ Completed          |
| Mid-Review Documentation   | ✅ Completed               |
| Mid-Review PPT             | ✅ Completed              |

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

Waiting-time analysis provides additional information about delays between activities and is being used alongside transition frequency and process-loop analysis.

---

## Finding 3 – PM4Py Process Discovery

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

## Finding 5 – Dashboard

The Power BI dashboard brings together the major process findings through:

* Total Cases
* Total Events
* Deviating %
* Average Wait Time
* Activity analysis
* Conformance split
---

# 🚀 Next Steps

After the Mid-Review, remaining time can be used for dashboard refinement, deeper process analysis, and further investigation of the identified process deviations.

---

# 🎯 Expected Final Outcome

The final CareFlow system will provide a process-oriented view of hospital operations rather than relying only on traditional numerical KPIs.

It will help reveal:

* How patients move through hospital activities
* Where process delays occur
* Which activities are frequently repeated
* Where bottlenecks and loop-backs exist
* How patient journeys vary
* Which patient paths deviate from the expected workflow
* Which process areas may require further investigation

The final solution combines **process mining, data analytics, conformance checking, and Power BI visualization** to provide a clearer understanding of healthcare workflows.
