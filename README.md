# CareFlow – Clinical Pathway Process Mining

## 📌 Project Overview

**CareFlow** is a healthcare process analytics and process mining project designed to analyze patient journeys through hospital workflows.

Traditional hospital dashboards can show metrics such as average waiting time, but they may not clearly reveal the actual sequence of activities a patient experiences or where operational bottlenecks occur.

CareFlow uses timestamped patient event logs to discover hospital processes, analyze patient journeys, identify repeated activities and potential process bottlenecks, and present actionable insights through a business intelligence dashboard.

---

## 🎯 Problem Statement

Hospital administrators may know the overall waiting time in an Emergency Room but may not know **why patients are waiting** or **where the workflow is getting delayed**.

For example, patients may experience:

* Long waiting times between activities
* Repeated or unnecessary activities
* Patients being sent back to previous stages
* Delays between diagnosis and treatment
* Different patient paths through the hospital

CareFlow aims to identify these process inefficiencies using process mining and data analytics.

---

## 💡 Proposed Solution

CareFlow creates and analyzes a chronological event log representing patient journeys through a hospital.

The project follows this workflow:

```text
Patient Event Data
        ↓
Data Generation
        ↓
Data Cleaning & Transformation
        ↓
Event Log Preparation
        ↓
PM4Py Process Discovery
        ↓
Process Map / Process Model
        ↓
Bottleneck & Waiting-Time Analysis
        ↓
Power BI Dashboard
        ↓
Actionable Healthcare Insights
```

---

## 🏥 Example Patient Journey

A patient may follow a process such as:

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

CareFlow also simulates operational inefficiencies and loop-backs so that process mining techniques can identify variations in patient journeys.

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

The actual process patterns are determined from the generated event log and PM4Py process discovery results.

---

## 🔍 Key Objectives

* Generate realistic timestamped hospital event logs.
* Standardize the event data for process mining.
* Discover the actual patient workflow.
* Generate process models using PM4Py.
* Analyze process transitions and patient journeys.
* Identify potential process bottlenecks.
* Analyze waiting times between activities.
* Detect repeated activities and loop-backs.
* Compare actual patient journeys with expected workflows.
* Build an interactive BI dashboard.
* Provide insights that can support hospital process improvement.

---

## 🛠️ Technology Stack

### Current Technologies

| Technology   | Purpose                              |
| ------------ | ------------------------------------ |
| Python       | Event-log generation and processing  |
| Pandas       | Data cleaning and analysis           |
| Matplotlib   | Basic visualization                  |
| CSV          | Event-log storage                    |
| PM4Py        | Process discovery and process mining |
| Graphviz     | Process-map visualization            |
| Git & GitHub | Version control and collaboration    |
| Power BI     | Dashboard development                |

### Deferred / Optional Technologies

| Technology | Status                     |
| ---------- | -------------------------- |
| BigQuery   | Deferred for current scope |
| dbt        | Deferred for current scope |

---

# ▶️ How to Run

## 1. Clone the Repository

Clone the repository and navigate to the project folder.

```bash
git clone https://github.com/anaghaspillai/CareFlow-Clinical-Pathway-Analytics
cd CareFlow-Clinical-Pathway-Analytics
```

## 2. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

> **Note:** PM4Py process-map visualization requires Graphviz to be installed on the system in addition to the Python `graphviz` package.

## 3. Generate the Hospital Event Log

Run the Python event-log generator:

```bash
python src/generate_events.py
```

This generates simulated hospital patient event data and saves it as a CSV file.

## 4. Clean the Event Log

Run the event-cleaning script:

```bash
python src/clean_events.py
```

This cleans and prepares the generated event log for further analysis and process mining.

## 5. Perform Basic Exploratory Data Analysis

Open the EDA notebook:

```text
notebooks/eda.ipynb
```

Run the notebook cells to perform basic exploratory data analysis on the cleaned event log.

The EDA covers:

* Dataset overview
* Number of patients and events
* Activity distribution
* Average events per patient
* Repeated Triage activity analysis
* Triage → X-Ray → Triage loop-back analysis
* X-Ray → Triage waiting-time analysis
* Basic activity visualization

## 6. Perform PM4Py Process Discovery

Run the PM4Py process discovery script:

```bash
python notebooks/process_map.py
```

The script uses the cleaned hospital event log to perform process discovery using PM4Py.

The current Week 2 implementation generates:

* Directly-Follows Graph (DFG)
* Petri Net process model
* Process-map visualization

The generated process-map outputs can be used for further process and bottleneck analysis.

---

# 🔄 Current Workflow

The current implementation follows:

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
eda.ipynb
        ↓
Basic EDA
        ↓
Triage → X-Ray → Triage Analysis
        ↓
PM4Py Process Discovery
        ↓
DFG + Petri Net Process Model
        ↓
Process & Bottleneck Analysis
        ↓
Power BI Dashboard
```

> **Note:** The current implementation uses CSV files for data storage and analysis. BigQuery and dbt are deferred from the current scope.

---

# 🧪 Fresh Clone Testing

The Week 2 PM4Py workflow was tested from a fresh clone of the repository.

### PM4Py Process Discovery

**Status: ✅ PASS**

The project was cloned into a fresh local directory and the required dependencies were installed successfully.

The PM4Py process discovery script was executed using the cleaned hospital event log.

The workflow successfully generated:

* Directly-Follows Graph (DFG)
* Petri Net process model
* Process-map visualization

The generated outputs were verified after execution.


# 🗄️ BigQuery / dbt Scope Decision

For the current implementation, CareFlow uses CSV-based event-log storage and Python/Pandas for data cleaning and preparation.

BigQuery and dbt are **not being introduced in the current implementation**. This is an intentional scope decision to keep the project focused on the core process-mining workflow.

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
Process & Bottleneck Analysis
      ↓
Power BI Dashboard
```

BigQuery and dbt may be considered in a future version if required for scalable data engineering and transformation workflows.

---

# 📊 Expected Analysis

The project will analyze:

* Patient flow
* Activity sequences
* Waiting times
* Process transitions
* Repeated activities
* Potential bottlenecks
* Process deviations
* Patient journey variations

> **Note:** Specific process-mining findings will be documented after analyzing and validating the generated PM4Py outputs.

---

# 📅 Project Development Plan

## Week 1 – Data Preparation & Initial Analysis

* Generate simulated hospital event logs using Python.
* Create realistic patient journeys.
* Introduce operational inefficiencies and loop-backs.
* Store the generated event log as CSV.
* Clean and prepare the event data using `clean_events.py`.
* Perform basic exploratory data analysis using `eda.ipynb`.
* Investigate the **Triage → X-Ray → Triage** bottleneck loop.
* Prepare the cleaned data for process mining.

### Status: ✅ Completed

---

## Week 2 – Process Discovery

* Standardize the event log.
* Prepare `Case_ID`, `Activity_Name`, and `Timestamp` fields.
* Use PM4Py for process discovery.
* Generate a Directly-Follows Graph (DFG).
* Generate a Petri Net process model.
* Generate process-map visualizations.
* Verify the PM4Py workflow from a fresh repository clone.
* Prepare the process model for bottleneck and waiting-time analysis.

### Status: 🔄 PM4Py Process Discovery planned

---

## Week 3 – Bottleneck Analysis & Dashboard

* Calculate transition and waiting times.
* Identify major process bottlenecks.
* Analyze repeated activities and loop-backs.
* Connect processed data to Power BI.
* Build operational and process-mining visualizations.

### Status: 🔄 Planned

---

## Week 4 – Conformance Checking & Finalization

* Compare actual patient journeys with the expected workflow.
* Identify non-compliant or inefficient paths.
* Add filtering and drill-down capabilities.
* Finalize the dashboard.
* Complete project documentation and presentation.

### Status: 🔄 Planned

---

# 📁 Project Structure

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

# 👥 Team Collaboration

The project is developed collaboratively using GitHub.

Each team member works on an individual branch and commits their work to that branch.

```text
main
│
├── Anagha S Pillai
├── Yashaswini N P
├── Vaishnavi Dipak Bhagat
└── Shravani BG
```

Completed work is reviewed and merged into the `main` branch by the team lead.

---

# 🎯 Expected Outcome

The final CareFlow system will provide a process-oriented view of hospital operations rather than only traditional numerical KPIs.

It will help reveal:

* How patients move through hospital activities
* Where process delays occur
* Which activities are frequently repeated
* Where bottlenecks and loop-backs exist
* How patient journeys vary
* Which process areas may require improvement

The final solution will combine **process mining, data analytics, and Power BI visualization** to provide a clearer understanding of healthcare workflows.

---

# 📚 Project Reference

This project is developed as part of the **Infotact Solutions Advanced Data Analytics** internship project.
