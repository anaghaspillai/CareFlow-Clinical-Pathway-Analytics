## CareFlow-Clinical-Pathway-Analytics

---

## 1. Project Overview

CareFlow is a healthcare process analytics and process mining project designed to understand patient journeys through hospital workflows.

The project uses timestamped hospital event logs to represent the sequence of activities performed during a patient's journey.

The main objective is to identify:

- Patient activity sequences
- Repeated activities
- Process loops
- Transition patterns
- Waiting times
- Potential bottlenecks
- Variations in patient journeys

The project is developed incrementally, beginning with data generation and preparation, followed by process discovery using PM4Py and dashboard development.

---

## 2. Problem Statement

Hospital administrators may have access to numerical KPIs such as average waiting time, number of patients, and activity counts. However, these metrics do not always show the actual sequence of activities experienced by patients.

A patient may move through several hospital activities and may sometimes return to a previous activity.

For example:

```text
Triage
   ↓
X-Ray
   ↓
Triage
````

This type of repeated activity sequence may indicate a potential process inefficiency or loop-back.

CareFlow aims to use process mining techniques to discover the actual patient workflow from event data and provide a clearer understanding of hospital processes.

---

## 3. Project Objectives

The main objectives of CareFlow are:

* Generate realistic simulated hospital event logs.
* Create chronological patient activity records.
* Clean and standardize event data.
* Perform exploratory data analysis.
* Identify repeated activities and process loops.
* Prepare event logs for process mining.
* Discover patient workflows using PM4Py.
* Generate process models such as Directly-Follows Graphs and Petri Nets.
* Analyze process transitions and waiting times.
* Identify potential bottlenecks and inefficient paths.
* Develop a Power BI dashboard in the later phase.
* Provide process-oriented insights for hospital workflow improvement.

---

# 4. Week 1 – Data Preparation

## 4.1 Event Generation

A Python-based event generator was created to simulate hospital patient journeys.

Each patient is assigned a unique `Case_ID`.

The event log contains activities and timestamps representing the patient's movement through the hospital workflow.

Example:

```text
Patient
   ↓
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

The generated data also contains simulated process loop-backs for analysis.

Example:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

---

## 4.2 Raw Event Log

The generated event data is stored as a CSV file.

The raw event log contains the initial patient activity records before cleaning.

The main fields are:

| Column          | Description                               |
| --------------- | ----------------------------------------- |
| `Case_ID`       | Unique identifier for a patient's journey |
| `Activity_Name` | Hospital activity performed               |
| `Timestamp`     | Date and time of the activity             |

---

## 4.3 Data Cleaning

The `clean_events.py` script was developed to prepare the raw event log for analysis and process mining.

The cleaning process includes:

* Checking for missing values.
* Validating timestamps.
* Removing invalid records.
* Checking duplicate records.
* Standardizing event data.
* Saving the cleaned event log.

The cleaned file is generated at:

```text
data/hospital_event_log_clean.csv
```

---

## 4.4 Exploratory Data Analysis

Basic exploratory data analysis was performed using:

```text
notebooks/eda.ipynb
```

The EDA focuses on:

* Dataset overview
* Number of patients
* Number of events
* Activity distribution
* Average events per patient
* Repeated Triage activity
* Triage → X-Ray → Triage loop-back
* X-Ray → Triage waiting-time analysis
* Basic activity visualization

The EDA was performed to understand the structure and patterns in the event log before process mining.

---

# 5. Week 2 – Process Mining

## 5.1 PM4Py Introduction

PM4Py was introduced during Week 2 for process discovery and process analysis.

PM4Py is used to transform the cleaned event log into a process-mining event log and discover the process followed by patients.

The main process-mining fields are:

```text
Case_ID
Activity_Name
Timestamp
```

These fields represent:

```text
Case_ID        → Process Case
Activity_Name  → Process Activity
Timestamp      → Event Time
```

---

## 5.2 PM4Py Installation

PM4Py was installed successfully in the testing environment.

The installation command used was:

```bash
pip install pm4py
```

The installation completed successfully with the required dependencies.

Installed packages included:

```text
pm4py
cvxopt
graphviz
```

---

## 5.3 Process Discovery

A PM4Py process discovery script was created and executed using the cleaned hospital event log.

The process discovery workflow is:

```text
Cleaned CSV
      ↓
Load Event Log
      ↓
Convert Data for PM4Py
      ↓
Process Discovery
      ↓
Directly-Follows Graph
      ↓
Petri Net
```

The process discovery script is located at:

```text
notebooks/process_map.py
```

The script was successfully executed using:

```bash
python notebooks/process_map.py
```

The terminal confirmed:

```text
Process map generated successfully!
```

---

## 5.4 Directly-Follows Graph

The Directly-Follows Graph (DFG) represents the transitions between activities in the patient journey.

For example:

```text
Triage
   ↓
X-Ray
   ↓
Doctor Consultation
```

The DFG helps identify:

* Common activity transitions
* Frequently followed activities
* Process paths
* Repeated transitions
* Potential process loops

The generated process-map output was successfully verified during testing.

---

## 5.5 Petri Net Process Model

PM4Py was also used to generate a Petri Net process model.

A Petri Net provides a structured representation of the discovered process and helps visualize the relationships between activities and transitions.

The generated Petri Net is part of the Week 2 process discovery output.

---

## 5.6 Process Map Output

The process discovery workflow generates process-map output files.

The generated output was verified after executing the PM4Py script.

The process map output is stored in the project output location used by the PM4Py script.

The exact process patterns and bottleneck findings will be documented after the process model is analyzed in detail.

> No specific bottleneck conclusion is recorded here unless it has been verified from the generated PM4Py output.

---

# 6. Fresh-Clone Testing

Fresh-clone testing was performed to verify that the project can be obtained from GitHub and executed in a clean local environment.

## 6.1 Clone Verification

The repository was cloned using Visual Studio Code's Git clone functionality.

The cloned project was opened successfully.

Result:

**PASS**

---

## 6.2 Dependency Verification

The following command was used:

```bash
pip install -r requirements.txt
```

The required project dependencies were successfully available.

Result:

**PASS**

---

## 6.3 Event Generation Verification

The event generator was executed using:

```bash
python src/generate_events.py
```

The event log was generated successfully.

Result:

**PASS**

---

## 6.4 Data Cleaning Verification

The cleaning script was executed using:

```bash
python src/clean_events.py
```

The cleaned event log was generated successfully.

Result:

**PASS**

---

## 6.5 EDA Verification

The EDA notebook was checked using:

```text
notebooks/eda.ipynb
```

The notebook contains the Week 1 exploratory analysis and loop-back investigation.

Result:

**PASS**

---

## 6.6 PM4Py Verification

The PM4Py process discovery script was executed using:

```bash
python notebooks/process_map.py
```

The script successfully generated the process map.

Terminal output confirmed:

```text
Process map generated successfully!
```

The generated PM4Py output was verified in the project.

Result:

**PASS**

---

# 7. Testing Summary

| Test                              | Status |
| --------------------------------- | ------ |
| Repository clone                  | PASS   |
| Dependency installation           | PASS   |
| Event log generation              | PASS   |
| Event cleaning                    | PASS   |
| Cleaned CSV generation            | PASS   |
| EDA notebook                      | PASS   |
| PM4Py installation                | PASS   |
| PM4Py process discovery           | PASS   |
| Directly-Follows Graph generation | PASS   |
| Petri Net generation              | PASS   |
| Process map output verification   | PASS   |

---

# 8. Technology Stack

## Current Technologies

| Technology | Purpose                              |
| ---------- | ------------------------------------ |
| Python     | Event generation and data processing |
| Pandas     | Data cleaning and analysis           |
| Matplotlib | Basic visualization                  |
| CSV        | Event-log storage                    |
| PM4Py      | Process mining and process discovery |
| Graphviz   | Process model visualization support  |
| Git        | Version control                      |
| GitHub     | Team collaboration                   |
| Power BI   | Interactive process and business dashboard |

## Planned Technologies

| Technology | Planned Purpose                            |
| ---------- | ------------------------------------------ |
| BigQuery   | Data warehouse, if required                |
| dbt        | Data transformation, if required           |

---

# 9. BigQuery / dbt Scope Decision

For the current implementation, CSV files are used for event-log storage and Python/Pandas is used for data preparation.

BigQuery and dbt are currently deferred.

This is an intentional scope decision to keep the project focused on the core process-mining workflow.

Current architecture:

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

BigQuery and dbt may be reconsidered if they become necessary for the final implementation.

---

# 10. Power BI Dashboard

Power BI is planned for the later stage of the project.

The dashboard is expected to provide an interactive view of hospital process performance.

Potential dashboard components include:

* Total number of patients
* Total number of events
* Activity distribution
* Patient journey analysis
* Transition frequency
* Waiting-time analysis
* Repeated activity analysis
* Bottleneck indicators
* Process-path analysis
* Patient-level filtering

The dashboard will be developed after the process-mining analysis is finalized.

---

# 11. Key Findings

The following findings have been verified during the current implementation:

### Data Generation

The hospital event generator successfully created simulated patient event data.

### Data Cleaning

The raw event log was successfully cleaned and prepared for analysis.

### Exploratory Analysis

The EDA notebook provides analysis of activity distributions, patient journeys, repeated activities, and the Triage → X-Ray → Triage pattern.

### Process Mining

PM4Py was successfully installed and executed.

The process discovery workflow successfully generated:

* Directly-Follows Graph
* Petri Net process model

### Fresh-Clone Testing

The project was successfully tested from a fresh clone, confirming that the setup and execution workflow can be reproduced.

> Detailed process findings such as the most frequent transition, highest waiting-time transition, or confirmed bottleneck will be added after analyzing the generated PM4Py outputs.

---

# 12. Current Project Status

## Week 1 – Data Preparation

**Status: COMPLETED**

Completed activities:

* Event log generation
* Raw CSV creation
* Data cleaning
* Cleaned CSV generation
* Data dictionary preparation
* Basic EDA
* Triage → X-Ray → Triage investigation
* README documentation
* Project documentation

---

## Week 2 – Process Mining

**Status: IN PROGRESS**

Completed activities:

* PM4Py setup
* PM4Py installation
* Process discovery script
* Directly-Follows Graph generation
* Petri Net generation
* Fresh-clone testing
* README verification

Current focus:

* Analyze the generated process model
* Identify important process transitions
* Analyze waiting times
* Investigate potential bottlenecks
* Prepare process findings for dashboard development

---

# 13. Development Roadmap

## Week 1 – Data Preparation

* Generate hospital event logs.
* Create simulated patient journeys.
* Clean event data.
* Prepare the data dictionary.
* Perform EDA.
* Investigate the Triage → X-Ray → Triage loop.

**Status: Completed**

---

## Week 2 – Process Discovery

* Install and configure PM4Py.
* Prepare event data for PM4Py.
* Discover the patient workflow.
* Generate Directly-Follows Graph.
* Generate Petri Net process model.
* Verify process-mining outputs.

**Status: In Progress / Core Process Discovery Completed**

---

## Week 3 – Bottleneck Analysis & Dashboard

Planned activities:

* Analyze process transitions.
* Calculate waiting times.
* Identify potential bottlenecks.
* Analyze repeated activities.
* Prepare process insights.
* Build Power BI dashboard.

**Status: Planned**

---

## Week 4 – Conformance & Finalization

Planned activities:

* Compare actual and expected patient workflows.
* Perform conformance checking.
* Identify process deviations.
* Add dashboard filters and drill-downs.
* Finalize dashboard.
* Complete project documentation.
* Prepare final project presentation.

**Status: Planned**

---

# 14. Project Structure

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
    └── petri_net_output.png
    └── dfg_output.png
│
├── dashboard
    └── CareFlow_Dashboard.pbix
    └── dashboard_screenshot.png
│
├── README.md
├── PROJECT_DOCUMENTATION.md
├── TESTING_NOTES.md
├── PROCESS_MAP_FINDINGS.md
├── CareFlow_Project_Requirements_Data_Fields.md
├── CareFlow_Day2_Data_Dictionary_Activity_Check.md
└── requirements.txt
├── PM4Py_Setup_Notes.md
├── process_map.png
```

---

# 15. GitHub Collaboration

The project is developed collaboratively using Git and GitHub.

Each team member works on an individual development branch.

Example:

```text
main
│
├── anagha-dev
├── yashaswini-dev
├── vaishnavi-dev
└── shravani-dev
```

The collaboration workflow is:

```text
Individual Branch
       ↓
Make Changes
       ↓
Test Changes
       ↓
Commit Changes
       ↓
Push to GitHub
       ↓
Pull Request
       ↓
Team Lead Review
       ↓
Merge into main
```

The `main` branch contains reviewed and merged project work.

---

# 16. Reproducibility

A new team member should be able to reproduce the project workflow by following these steps:

```bash
git clone https://github.com/anaghaspillai/CareFlow-Clinical-Pathway-Analytics
cd CareFlow-Clinical-Pathway-Analytics
pip install -r requirements.txt
python src/generate_events.py
python src/clean_events.py
python notebooks/process_map.py
```

For EDA, open:

```text
notebooks/eda.ipynb
```

The project was tested from a fresh clone to verify the setup and execution workflow.

---

# 17. Expected Final Outcome

The final CareFlow system is expected to provide a process-oriented view of hospital operations.

Instead of focusing only on numerical KPIs, the project will show:

```text
Patient Journey
      ↓
Activity Sequence
      ↓
Process Transitions
      ↓
Waiting Times
      ↓
Repeated Activities
      ↓
Potential Bottlenecks
      ↓
Actionable Insights
```

The final Power BI dashboard will provide an interactive interface for exploring these insights.

---

# 18. Conclusion

CareFlow combines data preparation, exploratory data analysis, process mining, and business intelligence to understand hospital patient workflows.

Week 1 established the data-generation, cleaning, and exploratory-analysis pipeline.

Week 2 introduced PM4Py process discovery and successfully generated process models including a Directly-Follows Graph and Petri Net.

The project is now moving toward detailed process analysis, bottleneck identification, and Power BI dashboard development.

---

## Project Context

CareFlow is being developed as part of the **Infotact Solutions Advanced Data Analytics internship project**.

The project is being developed incrementally through weekly milestones, with each phase building on the outputs of the previous phase.

````

