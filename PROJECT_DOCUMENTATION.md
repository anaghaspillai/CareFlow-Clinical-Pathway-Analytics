# CareFlow – Clinical Pathway Process Mining

## 1. Project Information

**Project Name:** CareFlow – Clinical Pathway Process Mining

**Domain:** Healthcare Operations & Process Analytics

**Project Type:** Data Analytics / Process Mining

**Primary Objective:** Analyze patient journeys through hospital workflows to identify bottlenecks, inefficient process paths, repeated activities, and deviations from expected workflows.

---

# 2. Introduction

Hospitals generate large amounts of operational data through their Electronic Health Record (EHR) systems. This data contains information about the activities performed for each patient along with timestamps.

Traditional business intelligence dashboards generally summarize this information using metrics such as average waiting time, number of patients, and average processing time.

However, these summaries do not always reveal the actual sequence of activities experienced by individual patients.

CareFlow addresses this problem using **process mining**.

The project converts chronological patient activity records into an event log and applies process-mining techniques to discover the actual process followed by patients.

---

# 3. Problem Statement

Hospital administrators may observe high Emergency Room waiting times without knowing the exact operational reason behind them.

A patient journey can contain:

* Multiple waiting periods
* Repeated activities
* Unnecessary process loops
* Different paths between patients
* Delays between activities
* Deviations from the expected workflow

For example, a patient may be sent back to Triage after completing an X-Ray. Traditional dashboards may show the overall waiting time but may not clearly expose this repeated process pattern.

CareFlow aims to discover such hidden process inefficiencies.

---

# 4. Proposed Solution

CareFlow creates a chronological event log containing patient activities and timestamps.

The event data is then:

1. Generated or collected.
2. Stored in a data warehouse.
3. Cleaned and standardized.
4. Converted into an event-log structure.
5. Analyzed using process-mining algorithms.
6. Evaluated for bottlenecks and process deviations.
7. Presented through a Power BI dashboard.

The overall architecture is:

```text
                 Hospital / Simulated Data
                           │
                           ▼
                  Patient Event Logs
                           │
                           ▼
                    Google BigQuery
                           │
                           ▼
                    dbt Transformation
                           │
                           ▼
                    Clean Event Log
                           │
                           ▼
                       PM4Py
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
        Process Discovery       Process Analysis
                │                     │
                └──────────┬──────────┘
                           ▼
                      Power BI
                           │
                           ▼
                Healthcare Insights
```

---

# 5. Patient Event Log

The main data structure used by the project is a chronological event log.

Each record represents an activity performed during a patient's journey.

Important fields include:

| Field       | Description                                        |
| ----------- | -------------------------------------------------- |
| `Case_ID`   | Unique identifier representing a patient's journey |
| `Activity`  | Activity performed by the patient                  |
| `Timestamp` | Date and time at which the activity occurred       |

Additional patient attributes may be included for analysis and filtering.

Example:

| Case_ID | Activity            | Timestamp        |
| ------- | ------------------- | ---------------- |
| P0001   | Registration        | 2026-01-05 09:00 |
| P0001   | Triage              | 2026-01-05 09:15 |
| P0001   | Doctor Consultation | 2026-01-05 10:00 |
| P0001   | X-Ray               | 2026-01-05 10:30 |
| P0001   | Doctor Review       | 2026-01-05 11:20 |
| P0001   | Pharmacy            | 2026-01-05 11:45 |
| P0001   | Discharge           | 2026-01-05 12:10 |

---

# 6. Example Patient Workflow

A normal patient journey can be represented as:

```text
Registration
      ↓
Triage
      ↓
Doctor Consultation
      ↓
X-Ray / Lab Test
      ↓
Doctor Review
      ↓
Pharmacy
      ↓
Discharge
```

The simulated dataset will also contain inefficient paths.

Example:

```text
Registration
      ↓
Triage
      ↓
Doctor Consultation
      ↓
X-Ray
      ↓
Triage
      ↓
Doctor Review
      ↓
Pharmacy
      ↓
Discharge
```

The repeated Triage activity represents a potential process loop that can later be investigated.

---

# 7. Project Objectives

The main objectives are:

### 7.1 Event Log Generation

Create realistic, timestamped hospital event logs representing patient journeys.

### 7.2 Data Preparation

Clean and standardize the raw event data into a format suitable for process mining.

### 7.3 Process Discovery

Use PM4Py to discover the actual workflow followed by patients.

### 7.4 Bottleneck Identification

Analyze the time taken between activities and identify stages where patients experience delays.

### 7.5 Process Deviation Detection

Identify patient journeys that differ from the expected process.

### 7.6 Dashboard Development

Create a Power BI dashboard to communicate process performance and operational insights.

---

# 8. Technology Stack

## Python

Python is used for generating simulated hospital event data and performing data-processing tasks.

## Pandas

Pandas is used for creating, cleaning, transforming, and analyzing tabular event data.

## BigQuery

Google BigQuery is used as the data warehouse for storing the raw hospital event logs.

## dbt

dbt is used to transform and standardize the raw data into an event-log structure suitable for process mining.

## PM4Py

PM4Py is the process-mining library used to discover and analyze patient workflows.

## Power BI

Power BI is used to create the final business intelligence dashboard and communicate process insights.

## GitHub

GitHub is used for version control, collaboration, branch management, and project documentation.

---

# 9. Week-wise Development Plan

## Week 1 – EHR Simulation and Warehouse Setup

### Data Engineering

* Build a Python script for generating mock hospital event logs.
* Simulate patient journeys.
* Introduce operational inefficiencies and process loop-backs.
* Load the raw event logs into BigQuery.
* Begin the initial data-cleaning phase.

### Expected Output

```text
Python Generator
       ↓
Hospital Event Log
       ↓
CSV
       ↓
BigQuery Raw Table
```

---

## Week 2 – Event Normalization and Process Discovery

### Data Engineering

* Standardize raw event data.
* Create a clean event-log format.
* Ensure the required fields are properly formatted.

### Process Mining

* Load the cleaned event log into PM4Py.
* Discover the actual patient workflow.
* Generate a process representation showing major patient paths.

### Expected Output

```text
Raw Data
   ↓
Clean Event Log
   ↓
PM4Py
   ↓
Discovered Patient Process
```

---

## Week 3 – Bottleneck Analysis and Business Intelligence

### Data Analysis

Calculate transition times between activities.

Examples:

* Registration → Triage
* Triage → Doctor
* Doctor → X-Ray
* X-Ray → Doctor Review
* Doctor Review → Pharmacy

Identify activities associated with longer waiting times.

### Dashboard

Connect the processed data to Power BI and create visualizations for:

* Patient volume
* Average waiting time
* Activity frequency
* Process transitions
* Major bottlenecks
* Patient journey patterns

---

## Week 4 – Conformance Checking and Finalization

The actual patient journeys are compared with the expected or ideal hospital process.

The project aims to identify:

* Non-compliant paths
* Repeated activities
* Unusual process sequences
* Inefficient patient journeys

The dashboard is then refined with filtering and drill-down capabilities.

---

# 10. Expected Results

At the end of the project, CareFlow is expected to provide:

* A structured hospital event log.
* A discovered patient process model.
* Identification of major process bottlenecks.
* Waiting-time analysis.
* Identification of repeated activities and loop-backs.
* Comparison between actual and expected workflows.
* An interactive Power BI dashboard.
* Actionable insights for improving hospital operations.

---

# 11. Business Value

The purpose of CareFlow is not simply to display hospital statistics.

The project aims to identify **why** operational delays occur.

For example:

```text
Traditional Dashboard:

Average ER Waiting Time = 85 minutes
```

CareFlow can go further by analyzing:

```text
Where is the delay?

Registration → Triage       = 10 min
Triage → Doctor             = 45 min
Doctor → X-Ray              = 15 min
X-Ray → Doctor Review       = 60 min
```

This allows administrators to investigate the specific stages responsible for delays.

---

# 12. GitHub Collaboration

The project follows a team-based Git workflow.

Each team member works on an individual branch.

Example:

```text
main
│
├── Anagha S Pillai
├── Yashaswini NP
├── Vaishnavi Dipak Bhagat
└── Shravani BG
```

The workflow is:

```text
Create / Receive Task
        ↓
Work on Individual Branch
        ↓
Make Changes
        ↓
git add
        ↓
git commit
        ↓
git push
        ↓
Team Lead Review
        ↓
Merge into main
```

The `main` branch contains the merged project code.

---

# 13. Project Folder Structure

```text
CareFlow/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── generate_data.py
│   └── analyze_data.py
│
├── notebooks/
│
├── dashboard/
│
├── README.md
├── PROJECT_DOCUMENTATION.md
└── requirements.txt
```

The structure can be expanded as additional project components are implemented.

---

# 14. Conclusion

CareFlow applies process mining and data analytics to healthcare operations.

Instead of looking only at aggregate hospital statistics, the project analyzes chronological patient journeys to discover how the process actually operates.

By combining Python, BigQuery, dbt, PM4Py, and Power BI, the project aims to identify bottlenecks, repeated activities, process deviations, and opportunities for operational improvement.

The final outcome is an analytical system that transforms patient event logs into meaningful process insights for healthcare operations.
