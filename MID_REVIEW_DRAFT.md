
# CareFlow-Clinical-Pathway-Analytics – Mid-Review

## 1. Project Overview

**CareFlow – Clinical Pathway Process Mining** is a healthcare process analytics project focused on understanding patient journeys through hospital workflows.

The project uses timestamped hospital event logs to represent the sequence of activities followed by patients.

The main goal is to use data analytics and process mining techniques to discover patient workflows, identify repeated activities and potential bottlenecks, analyze process transitions and waiting times, and present meaningful insights through a Power BI dashboard.

The project is being developed incrementally, with:

- Week 1 focused on data generation, cleaning, and exploratory analysis.
- Week 2 focused on process mining and process discovery.
- Upcoming phases focused on bottleneck analysis, dashboard development, and final process analysis.



## 2. Problem Statement

Hospital administrators may have access to metrics such as patient counts and average waiting times, but these metrics may not clearly explain how patients move through the hospital workflow.

Patients can experience:

- Long waiting times between activities.
- Repeated activities.
- Different paths through the hospital.
- Process loops.
- Delays between diagnostic and treatment activities.

For example, a patient may follow:

```text
Triage
   ↓
X-Ray
   ↓
Triage
````

The repeated Triage activity represents a potential process loop that can be investigated using process mining.

CareFlow aims to discover the actual patient workflow from event-log data and identify process patterns that may help reveal operational inefficiencies.

---

# 3. Project Objectives

The main objectives of CareFlow are:

* Generate realistic simulated hospital event logs.
* Create chronological patient activity records.
* Clean and standardize the event data.
* Perform exploratory data analysis.
* Identify repeated activities and potential process loops.
* Prepare event logs for process mining.
* Discover patient workflows using PM4Py.
* Generate process models such as Directly-Follows Graphs and Petri Nets.
* Analyze process transitions and waiting times.
* Identify potential process bottlenecks.
* Develop an interactive Power BI dashboard.
* Provide process-oriented insights for improving hospital workflows.

---

# 4. Week 1 – Data Preparation

## 4.1 Event Generation

A Python-based event generator was developed to create simulated hospital patient event logs.

Each patient is assigned a unique `Case_ID`, and each event contains an activity and timestamp.

The generated event data represents patient journeys through hospital activities.

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
Doctor Review
      ↓
Pharmacy
      ↓
Discharge
```

The generated dataset also includes simulated process loop-backs for analysis.

Example:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

---

## 4.2 CSV Creation

The generated hospital event data is stored as a CSV file.

The main event-log fields are:

| Column          | Description                                        |
| --------------- | -------------------------------------------------- |
| `Case_ID`       | Unique identifier representing a patient's journey |
| `Activity_Name` | Hospital activity performed                        |
| `Timestamp`     | Date and time of the activity                      |

The raw event log is used as the input for the data-cleaning stage.

---

## 4.3 Data Cleaning

The `clean_events.py` script was developed to prepare the raw event log for analysis.

The cleaning process includes:

* Checking missing values.
* Validating timestamps.
* Removing invalid records.
* Checking duplicate records.
* Preparing the event data for further analysis.
* Generating a cleaned CSV file.

The cleaned event log is saved as:

```text
data/hospital_event_log_clean.csv
```

The cleaned dataset is used as the input for the PM4Py process-mining stage.

---

## 4.4 Exploratory Data Analysis

Basic exploratory data analysis was performed using:

```text
notebooks/eda.ipynb
```

The EDA covers:

* Dataset overview.
* Number of patients.
* Number of events.
* Activity distribution.
* Average events per patient.
* Repeated Triage activity.
* Triage → X-Ray → Triage loop-back analysis.
* X-Ray → Triage waiting-time analysis.
* Basic activity visualization.

The EDA helped establish an initial understanding of the hospital event log before applying process mining techniques.

---

## 4.5 Week 1 Workflow

The Week 1 workflow was:

```text
Python Event Generator
        ↓
Hospital Patient Event Log
        ↓
Raw CSV
        ↓
Data Cleaning
        ↓
Cleaned CSV
        ↓
EDA
        ↓
Activity Analysis
        ↓
Triage → X-Ray → Triage Analysis
```

### Week 1 Status

**COMPLETED**

---

# 5. Week 2 – Process Mining

## 5.1 PM4Py Setup

PM4Py was introduced during Week 2 for process discovery and process analysis.

The PM4Py package was successfully installed in the testing environment.

The installation included the required supporting packages.

The process-mining environment was verified before running the process discovery workflow.

---

## 5.2 PM4Py Process Discovery

The cleaned hospital event log was used as input for the PM4Py process discovery workflow.

The process discovery script is:

```text
notebooks/process_map.py
```

The script was executed using:

```bash
python notebooks/process_map.py
```

The process discovery script executed successfully.

Terminal output confirmed:

```text
Process map generated successfully!
```

---

## 5.3 Process Model / Process Map

The PM4Py workflow successfully generated process-mining outputs.

The generated outputs include:

* Directly-Follows Graph (DFG)
* Petri Net process model

The Directly-Follows Graph represents how activities follow one another in patient journeys.

A simplified example is:

```text
Triage
   ↓
Doctor Consultation
   ↓
X-Ray
   ↓
Doctor Review
```

The process model provides a visual representation of the patient workflow discovered from the event log.

---

## 5.4 Bottleneck Analysis

The project is currently moving from process discovery toward detailed bottleneck analysis.

The generated process model will be used to investigate:

* Frequently occurring transitions.
* Repeated activities.
* Process loops.
* Long waiting-time transitions.
* Potential bottlenecks.
* Variations in patient journeys.

The previously identified:

```text
Triage → X-Ray → Triage
```

pattern will be further investigated using the process-mining results.

> Detailed bottleneck conclusions will be added after analyzing the generated PM4Py process outputs. No unverified bottleneck findings are recorded at this stage.

---

## 5.5 Transition and Waiting-Time Analysis

The next stage of Week 2 analysis is to examine the time taken between consecutive hospital activities.

For example:

```text
Activity A
    ↓
Waiting Time
    ↓
Activity B
```

The analysis will focus on:

* Activity-to-activity transitions.
* Average transition time.
* Minimum and maximum waiting time.
* Frequently occurring transitions.
* Potential delays.
* Triage → X-Ray → Triage loop-back timing.

These results will later support the bottleneck analysis and Power BI dashboard.

---

## 5.6 Fresh-Clone Testing

The project was tested from a fresh clone to verify that the workflow can be reproduced by another team member.

The following workflow was verified:

```text
Clone Repository
        ↓
Install Dependencies
        ↓
Generate Event Log
        ↓
Clean Event Log
        ↓
Run EDA
        ↓
Run PM4Py Process Discovery
        ↓
Generate Process Map
```

The PM4Py process discovery script successfully executed during the fresh-clone test.

### Fresh-Clone Testing Status

**PASSED**

---

# 6. Key Findings

The following observations have been verified during the current project phase:

### 6.1 Event Log Successfully Generated

The Python event generator successfully creates simulated hospital patient event data.

---

### 6.2 Event Data Successfully Cleaned

The raw event log was successfully processed using `clean_events.py` and a cleaned event log was generated.

---

### 6.3 EDA Successfully Performed

The EDA notebook provides initial analysis of:

* Patient and event counts.
* Activity distribution.
* Repeated activities.
* Patient activity patterns.
* Triage → X-Ray → Triage loop-back.

---

### 6.4 PM4Py Process Discovery Successfully Completed

PM4Py was successfully installed and executed.

The process discovery workflow generated:

```text
Directly-Follows Graph
        +
Petri Net Process Model
```

---

### 6.5 Fresh-Clone Workflow Verified

The project was cloned and tested in a fresh local environment.

The setup and PM4Py workflow executed successfully.

---

### Current Finding Status

Detailed findings regarding:

* Most frequent transition.
* Highest waiting-time transition.
* Confirmed bottleneck.
* Process deviations.

will be added after detailed analysis of the generated process model.

---

# 7. BigQuery / dbt Scope Decision

For the current implementation, the project uses CSV files for event-log storage and Python/Pandas for data cleaning and preparation.

BigQuery and dbt are currently deferred.

This is an intentional scope decision to keep the project focused on the core process-mining workflow.

The current architecture is:

```text
Event Generation
      ↓
Raw CSV
      ↓
Data Cleaning
      ↓
Cleaned CSV
      ↓
EDA
      ↓
PM4Py Process Discovery
      ↓
Process Analysis
      ↓
Power BI Dashboard
```

BigQuery and dbt may be reconsidered later if they become necessary for the project requirements.

---

# 8. Current Technology Stack

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

---

# 9. Power BI Dashboard

Power BI is planned for the upcoming dashboard-development phase.

The dashboard is expected to provide an interactive view of hospital process performance.

Potential dashboard components include:

* Total number of patients.
* Total number of events.
* Activity distribution.
* Patient journey analysis.
* Process transition frequency.
* Waiting-time analysis.
* Repeated activity analysis.
* Potential bottleneck indicators.
* Process-path analysis.
* Patient-level filtering.

The dashboard will be developed after the process-mining analysis and bottleneck analysis are completed.

---

# 10. Current Project Status

## Week 1 – Data Preparation

**Status: COMPLETED**

Completed:

* Event generation.
* CSV creation.
* Data cleaning.
* Cleaned CSV generation.
* Data dictionary preparation.
* Basic EDA.
* Triage → X-Ray → Triage investigation.
* README documentation.
* Project documentation.

---

## Week 2 – Process Mining

**Status: IN PROGRESS**

Completed:

* PM4Py installation.
* PM4Py process discovery setup.
* Process discovery script.
* Directly-Follows Graph generation.
* Petri Net generation.
* Process map generation.
* Fresh-clone testing.
* README verification.

Currently working on:

* Detailed process-map analysis.
* Transition analysis.
* Waiting-time analysis.
* Bottleneck identification.
* Preparing process insights for Power BI.

---

# 11. Next Steps

The next stages of the project are:

## Step 1 – Detailed Process Analysis

Analyze the generated PM4Py process model to understand:

* Main patient paths.
* Common transitions.
* Repeated activities.
* Process loops.
* Process variations.

---

## Step 2 – Transition Analysis

Calculate transition-level statistics such as:

* Number of transitions.
* Frequency of transitions.
* Average transition time.
* Waiting-time distribution.

---

## Step 3 – Bottleneck Analysis

Investigate potential bottlenecks using:

* Waiting times.
* Repeated activities.
* Process loops.
* Frequently occurring transitions.

The:

```text
Triage → X-Ray → Triage
```

pattern will be specifically investigated.

---

## Step 4 – Power BI Dashboard

Use the analyzed process data to develop an interactive Power BI dashboard.

The dashboard will focus on:

* Patient flow.
* Activity distribution.
* Waiting times.
* Process transitions.
* Bottlenecks.
* Patient journey variations.

---

## Step 5 – Conformance Checking

In a later phase, actual patient journeys can be compared against the expected hospital workflow.

This can help identify:

* Deviations.
* Unexpected process paths.
* Repeated activities.
* Non-compliant workflows.

---

## Step 6 – Final Documentation

The final documentation will include:

* Verified process findings.
* Bottleneck analysis.
* Dashboard screenshots.
* Final technology stack.
* Project outcomes.
* Limitations.
* Future improvements.

---

# Mid-Review Summary

At the mid-review stage, CareFlow has successfully progressed from hospital event-log generation and data preparation to PM4Py-based process discovery.

The current workflow is:

```text
Hospital Event Generation
          ↓
Data Cleaning
          ↓
Exploratory Data Analysis
          ↓
Cleaned Event Log
          ↓
PM4Py Process Discovery
          ↓
DFG + Petri Net
          ↓
Transition & Bottleneck Analysis
          ↓
Power BI Dashboard
```

The data-preparation pipeline and PM4Py process-discovery workflow have been successfully tested from a fresh clone.

The next major focus is to analyze the generated process model, identify verified bottlenecks and waiting-time patterns, and use these findings to build the Power BI dashboard.

---

## Project Context

CareFlow is being developed as part of the **Infotact Solutions Advanced Data Analytics internship project**.

The project is being developed collaboratively using Git and GitHub through weekly development milestones.

```
