# CareFlow – Clinical Pathway Process Mining

## 📌 Project Overview

**CareFlow** is a healthcare process analytics and process mining project designed to analyze patient journeys through hospital workflows.

Traditional hospital dashboards can show metrics such as average waiting time, but they may not clearly reveal the actual sequence of activities a patient experiences or where operational bottlenecks occur.

CareFlow uses timestamped patient event logs to discover hospital processes, analyze patient journeys, identify repeated activities and potential process bottlenecks, measure waiting and transition times, compare actual patient paths against an expected workflow, and present insights through a Power BI dashboard.

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

---

## 3. Waiting-Time Analysis

Waiting-time analysis was performed to understand the time spent between consecutive hospital activities.

Particular attention was given to transitions associated with the identified bottleneck, including:

```text
X-Ray → Triage
```

Waiting-time analysis complements the bottleneck analysis by examining not only **how frequently a process loop occurs**, but also **how much time may be associated with transitions within the patient journey**.

These findings will be incorporated into the Power BI dashboard.

---

# 4. PM4Py Process Discovery

PM4Py was used to move from manual Pandas-based process analysis to formal process discovery.

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

Each of the **200 patient cases** was compared against this ideal pathway.

A patient was considered conformant if their recorded activity sequence exactly matched the expected pathway without repeated or additional activities.

## Conformance Results

| Metric                 | Result |
| ---------------------- | -----: |
| Total Patients         |    200 |
| Conformant Patients    |    127 |
| Deviating Patients     |     73 |
| Conformance Percentage |  63.5% |
| Deviation Percentage   |  36.5% |

### Key Finding

**127 patients (63.5%)** followed the ideal pathway, while **73 patients (36.5%)** deviated from it.

The 36.5% deviation rate is consistent with the previously identified Triage → X-Ray → Triage loop.

The pattern has now been observed through three analytical approaches:

```text
Manual EDA
    ↓
Bottleneck Identification
    ↓
PM4Py Process Discovery
    ↓
Conformance Checking
```

This consistency strengthens confidence that the identified process deviation represents a genuine process pattern rather than an isolated data artifact.

> The underlying operational/root cause of the loop has not yet been confirmed and requires further investigation.

### Status

**✅ Completed – Results Verified**

---

# 📊 Power BI Dashboard

Power BI is being used to consolidate the process-mining findings into an interactive dashboard.

The dashboard currently includes / is being developed with:

### KPI Cards

* Total Patients
* Total Events
* Repeated Triage / Bottleneck KPI
* Waiting-Time metrics
* Transition metrics
* Conformance metrics

### Process Analysis

* Activity distribution
* Patient transitions
* Process-flow analysis
* Bottleneck identification
* Repeated activity analysis
* Waiting-time analysis
* Conformance results

### Dashboard Status

**🔄 In Progress**

The final dashboard will combine the process discovery, bottleneck, waiting-time, transition, and conformance findings.

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

The project has progressed beyond the original Week 2 scope and is currently ahead of schedule in several areas.

### Monday – Formal Process Discovery

* Implement PM4Py process discovery.
* Generate a Directly-Follows Graph.
* Generate a Petri Net process model.
* Verify the process-map outputs.
* Document what the discovered process shows.

### Status: ✅ Completed

---

### Tuesday – Data Platform Decision & Dashboard Direction

* Evaluate whether BigQuery/dbt is required for the current implementation.
* Decide whether to introduce the additional data-engineering layer or defer it.
* Continue with the CSV/Python/PM4Py architecture after the scope decision.
* Begin/continue Power BI dashboard development.

### Status: ✅ BigQuery/dbt Deferred

### Status: 🔄 Power BI Dashboard In Progress

---

### Wednesday – Conformance Checking

* Compare actual patient paths against the ideal workflow.
* Calculate conformant and deviating cases.
* Identify major deviation patterns.
* Refine the process model.
* Begin incorporating conformance findings into the Mid-Review documentation.

### Status: ✅ Completed

Current verified results:

```text
Total Patients      = 200
Conformant          = 127 (63.5%)
Deviating           = 73  (36.5%)
```

---

### Thursday – Power BI Dashboard

* Build the first working version of the Power BI dashboard.
* Add process KPIs.
* Add bottleneck metrics.
* Add waiting-time analysis.
* Add transition analysis.
* Add conformance metrics.
* Refine dashboard layout and usability.

### Status: 🔄 In Progress

---

### Friday – Consolidation & Validation

* Consolidate PM4Py process discovery.
* Consolidate bottleneck and waiting-time findings.
* Validate conformance results.
* Integrate dashboard outputs.
* Complete final validation.
* Finalize the Mid-Review draft.

### Status: 🔄 In Progress

---

# 🎓 Mid-Review Preparation

The Mid-Review is scheduled for **August 25–27**.

The presentation will bring together the complete progress achieved so far.

The Mid-Review will demonstrate:

### 1. Bottleneck Findings

The main identified loop:

```text
Triage → X-Ray → Triage
```

with:

**73 / 200 patients = 36.5%**

---

### 2. Waiting-Time Findings

Analysis of time spent between consecutive patient activities, with particular attention to transitions related to the identified bottleneck.

---

### 3. Process Discovery

Formal PM4Py outputs:

* Directly-Follows Graph
* Petri Net process model
* Process-map interpretation

---

### 4. Conformance Checking

Verified comparison between actual patient journeys and the expected pathway:

```text
127 conformant cases  → 63.5%
73 deviating cases    → 36.5%
```

---

### 5. BigQuery / dbt Decision

The project currently uses CSV + Python/Pandas + PM4Py.

BigQuery and dbt have been **deferred from the current implementation** to maintain focus on the core process-mining and dashboard objectives.

---

### 6. Power BI Dashboard

The dashboard will consolidate:

* Patient KPIs
* Process transitions
* Bottleneck findings
* Waiting-time metrics
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
| BigQuery/dbt Evaluation    | ✅ Decision Made – Deferred |
| Conformance Checking       | ✅ Completed                |
| Power BI Dashboard         | 🔄 In Progress             |
| Mid-Review Documentation   | 🔄 In Progress             |
| Final Presentation         | ⏳ Upcoming                 |

---

# 🎯 Current Key Findings

### Finding 1 – Major Process Loop

The analysis identified:

```text
Triage → X-Ray → Triage
```

affecting:

**73 out of 200 patients (36.5%)**

---

### Finding 2 – Waiting-Time Analysis

Waiting-time analysis provides additional information about delays between activities and will be used alongside transition frequency and process-loop analysis.

---

### Finding 3 – PM4Py Confirmation

The manually identified patient-flow patterns were subsequently examined using formal PM4Py process discovery.

The DFG and Petri Net provide a process-level representation of the hospital workflow.

---

### Finding 4 – Conformance

Conformance checking identified:

**127 conformant cases (63.5%)**

and

**73 deviating cases (36.5%)**

The deviation percentage is consistent with the previously identified repeated Triage pattern.

---

# 🚀 Next Steps

Before the Mid-Review:

1. Complete the first working Power BI dashboard.
2. Integrate bottleneck and waiting-time findings.
3. Add transition-time metrics.
4. Add verified conformance metrics.
5. Add DFG/Petri Net screenshots.
6. Refine process-map interpretation.
7. Perform final validation of all reported metrics.
8. Finalize the Mid-Review documentation.
9. Prepare the Mid-Review presentation and project demonstration.

After the Mid-Review, remaining buffer time can be used for dashboard refinement, deeper root-cause investigation, and additional process-mining analysis.

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
