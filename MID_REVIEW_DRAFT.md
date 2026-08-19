# CareFlow – Mid-Review

# 1. Project Overview

**CareFlow – Clinical Pathway Process Mining** is a healthcare process analytics project designed to understand patient journeys through hospital workflows.

The project uses timestamped hospital event logs to analyze the sequence of activities performed during patient journeys. Process mining techniques are used to discover the actual workflow, identify repeated activities, detect bottlenecks, and analyze deviations from the expected process.

The project is being developed incrementally:

```text
Hospital Event Data
        ↓
Data Preparation & Cleaning
        ↓
Exploratory Data Analysis
        ↓
PM4Py Process Discovery
        ↓
Process & Bottleneck Analysis
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

Repeated activities
Long waiting times
Process loop-backs
Different patient pathways
Deviations from the expected workflow
Inefficient transitions between activities

For example:
```text
Triage
   ↓
X-Ray
   ↓
Triage
```
The repeated Triage activity may indicate a potential process inefficiency that requires further investigation.

CareFlow aims to use process mining and data analytics to identify and visualize these process patterns.


# 3. Project Objectives

The main objectives of CareFlow are:
```text
Generate realistic timestamped hospital event logs.
Clean and standardize the event data.
Perform exploratory data analysis.
Understand patient activity sequences.
Discover the actual hospital workflow using PM4Py.
Identify repeated activities and potential bottlenecks.
Analyze transition and waiting times.
Compare actual patient journeys with the expected workflow.
Perform conformance checking.
Build a Power BI dashboard.
Present actionable process insights.
```
# 4. Week 1 – Data Preparation & Exploratory Analysis
## 4.1 Event Log Generation

A Python-based event generator was developed to simulate hospital patient journeys.

The generated event log contains:

Unique patient identifiers (Case_ID)
Hospital activities (Activity_Name)
Activity timestamps (Timestamp)

The generated dataset contains:

200 patients
883 events

## 4.2 Data Cleaning

The clean_events.py script was developed to prepare the raw event log for analysis.

The cleaning process includes:

Missing value checking
Timestamp validation
Duplicate checking
Data standardization
Preparation of the cleaned event log

The cleaned dataset contains:

Original rows: 883
Final cleaned rows: 883
Rows removed: 0
Unique patients: 200

The cleaned event log is stored at:

data/hospital_event_log_clean.csv

## 4.3 Exploratory Data Analysis

Basic EDA was performed using:

notebooks/eda.ipynb

The analysis includes:
```text
Dataset overview
Number of patients
Number of events
Activity distribution
Average events per patient
Repeated Triage analysis
Triage → X-Ray → Triage loop analysis
X-Ray → Triage waiting-time analysis
Activity visualizations
```
A repeated Triage rate of 36.5% was identified during the initial analysis.

This value is treated as a Repeated Triage Rate KPI and will be considered as one indicator during bottleneck analysis.

Note: Repeated Triage should not be considered the bottleneck by itself. Waiting times, transition frequencies, and process deviations will also be considered.

# 5. Week 2 – Process Mining
## 5.1 PM4Py Process Discovery

PM4Py was introduced to discover the actual patient workflow from the cleaned event log.

The cleaned event log was used as the input for process discovery.

The PM4Py workflow successfully generated:

Directly-Follows Graph (DFG)
Petri Net process model
Process map visualization

The process discovery script was successfully executed from a fresh clone of the repository.

Status

Completed – PASS

## 5.2 Directly-Follows Graph

The Directly-Follows Graph represents the transitions between hospital activities.

It helps identify:

Common activity transitions
Frequently occurring process paths
Process loops
Potentially unusual transitions

Example process pattern:
```text
Triage
   ↓
X-Ray
   ↓
Triage
```
The DFG will be used together with transition frequency and waiting-time analysis to identify important process patterns.

## 5.3 Petri Net Process Model

A Petri Net process model was generated using PM4Py.

The Petri Net provides a structured representation of:

Activities
Process transitions
Possible patient paths
Process flow relationships

The generated process model was successfully verified during fresh-clone testing.

Status

Completed – PASS

# 6. Bottleneck Analysis

The project focuses on identifying potential bottlenecks using multiple indicators rather than a single metric.

The current indicators include:

Repeated Triage Rate
Repeated Triage Rate = 36.5%

This represents the percentage of patients experiencing repeated Triage activity in the analyzed dataset.

Transition Analysis

Transitions between activities will be analyzed to identify frequently occurring and potentially inefficient process paths.

Examples include:
```text
Triage → X-Ray
X-Ray → Triage
Triage → Doctor Consult
Waiting-Time Analysis
```
Waiting time between consecutive activities will be calculated and visualized.

Important transitions include:
```text
X-Ray → Triage
Triage → Doctor Consultation
Doctor Consultation → X-Ray
```
Actual average waiting-time and transition-time KPIs will be finalized during the dashboard analysis phase.

# 7. Conformance Checking

Conformance checking will be used to compare the actual patient journeys against the expected hospital workflow.

The expected workflow provides a reference process such as:
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
The actual event log will be compared against this expected process to identify:

Deviations
Unexpected activity sequences
Repeated activities
Loop-backs
Potentially non-compliant patient paths
Current Status

# In Progress

Today's conformance-checking results will be added after the final results are generated and verified.

Conformance Results

To be updated with today's verified results.

Possible metrics to document include:

Number of conforming cases
Number of deviating cases
Conformance percentage
Major deviation patterns
Most frequently observed deviations

No conformance findings will be added until the actual PM4Py output has been verified.

# 8. Power BI Dashboard

Power BI will be used to present the process-mining and healthcare operational insights in an interactive dashboard.

## The dashboard is planned to include:

KPI Cards
Total Patients
Total Events
Repeated Triage Rate
Average Waiting Time
Average Transition Time
Process Conformance Rate
Patient Flow Analysis

## The dashboard will visualize:

Patient activity flow
Activity frequency
Process transitions
Common patient pathways
Bottleneck Analysis

## The dashboard will highlight:

Repeated activities
High waiting-time transitions
Frequently occurring process loops
Potential bottleneck areas
Process Analysis

## The dashboard will include:

Process map / flow visualization
Transition analysis
Waiting-time analysis
Conformance results
Current Status

Dashboard work – In Progress

Actual KPI values will be updated after the calculations and visualizations are finalized.

## 9. BigQuery / dbt Scope Decision

BigQuery and dbt are currently deferred from the implementation.

The current project uses:
```text
CSV
 ↓
Python
 ↓
Pandas
 ↓
PM4Py
 ↓
Power BI
```
This scope decision keeps the project focused on the core process-mining workflow.

BigQuery and dbt may be considered later if the project requires a data warehouse or additional transformation layer.

# 10. Current Technology Stack
## Technologies Currently Used

| Technology | Purpose                              |
| ---------- | ------------------------------------ |
| Python     | Event generation and data processing |
| Pandas     | Data cleaning and analysis           |
| Matplotlib | Basic visualization                  |
| CSV        | Event-log storage                    |
| PM4Py      | Process mining and process discovery |
| Graphviz   | Process visualization support        |
| Git        | Version control                      |
| GitHub     | Team collaboration                   |
| Power BI   | Interactive dashboard            |

## Technologies Planned for Later Phases

| Technology | Purpose                          |
| ---------- | -------------------------------- |
| BigQuery   | Data warehouse, if required      |
| dbt        | Data transformation, if required |

# 11. Fresh-Clone Testing

The project was tested from a fresh clone to verify that the merged implementation works correctly for a new team member.

The following were verified:
```text
Repository cloning
Dependency installation
Event generation
Data cleaning
EDA workflow
PM4Py process discovery
Process map generation
README setup instructions
PM4Py Fresh-Clone Result

Status: PASS
```
The PM4Py process discovery script executed successfully and generated the expected process-mining outputs.

# 12. Key Findings So Far

The current analysis has identified the following observations:

## Finding 1 – Repeated Triage

A repeated Triage rate of:

36.5%

was identified during the initial EDA.

This is being used as the Repeated Triage Rate KPI for the bottleneck analysis.

## Finding 2 – Process Loop

The following loop-back pattern is present in the event data:
```text
Triage
   ↓
X-Ray
   ↓
Triage
```
This pattern will be further evaluated using transition and waiting-time analysis.

## Finding 3 – Process Discovery

PM4Py successfully discovered the patient process from the cleaned event log.

Both the DFG and Petri Net process model were generated successfully.

## Finding 4 – Conformance Analysis

Conformance checking is being performed to compare actual patient journeys with the expected workflow.

Final conformance findings will be added after today's results are verified.

# 13. Current Project Status

| Component                | Status         |
| ------------------------ | -------------- |
| Event generation         | ✅ Completed    |
| Raw CSV generation       | ✅ Completed    |
| Data cleaning            | ✅ Completed    |
| Data dictionary          | ✅ Completed    |
| Basic EDA                | ✅ Completed    |
| Repeated Triage analysis | ✅ Completed    |
| PM4Py process discovery  | ✅ Completed    |
| DFG generation           | ✅ Completed    |
| Petri Net generation     | ✅ Completed    |
| Fresh-clone testing      | ✅ Completed    |
| Bottleneck analysis      | 🔄 In Progress |
| Waiting-time analysis    | 🔄 In Progress |
| Conformance checking     | 🔄 In Progress |
| Power BI dashboard       | 🔄 In Progress |
| BigQuery                 | ⏸ Deferred     |
| dbt                      | ⏸ Deferred     |


# 14. Mid-Review Deliverables
The current Mid-Review will demonstrate:
```text

Week 1
Data Generation
      ↓
Data Cleaning
      ↓
     EDA
      ↓
Repeated Triage Analysis
```
```text

Week 2
      ↓
PM4Py Process Discovery
      ↓
     DFG
      ↓
  Petri Net
      ↓
Bottleneck Analysis
      ↓
Conformance Checking
      ↓
Power BI Dashboard
```
```text
The final Mid-Review presentation will include:

Project overview
Problem statement
Objectives
Data preparation
EDA findings
PM4Py process discovery
Process map / DFG
Petri Net
Bottleneck analysis
Conformance checking results
Power BI dashboard
Technology stack
Scope decisions
Current status
Next steps
```
# 15. Conclusion

CareFlow has progressed from initial hospital event-log generation and data preparation to process discovery using PM4Py.

The cleaned event log has been successfully analyzed, and PM4Py has successfully generated the process model and process map.

The current phase focuses on connecting process discovery with bottleneck analysis, conformance checking, and Power BI visualization.

The project will ultimately provide a process-oriented view of patient journeys and help identify areas where hospital workflows may be inefficient or require further investigation.

```

