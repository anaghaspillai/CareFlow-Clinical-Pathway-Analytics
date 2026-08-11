# CareFlow – Clinical Pathway Process Mining

## 📌 Project Overview

**CareFlow** is a healthcare process analytics and process mining project designed to analyze patient journeys through hospital workflows.

Traditional hospital dashboards can show metrics such as average waiting time, but they may not clearly reveal the actual sequence of activities a patient experiences or where operational bottlenecks occur.

CareFlow uses timestamped patient event logs to discover the actual hospital process, identify inefficient patient journeys, detect repeated activities and process bottlenecks, and present actionable insights through a business intelligence dashboard.

---

## 🎯 Problem Statement

Hospital administrators often know the overall waiting time in an Emergency Room but may not know **why patients are waiting** or **where the workflow is getting delayed**.

For example, patients may experience:

* Long waiting times between activities
* Repeated or unnecessary activities
* Patients being sent back to previous stages
* Delays between diagnosis and treatment
* Different patient paths through the hospital

CareFlow aims to identify these hidden process inefficiencies through process mining and data analytics.

---

## 💡 Proposed Solution

CareFlow creates and analyzes a chronological event log representing patient journeys through a hospital.

The project follows this general workflow:

```text
Patient Event Data
        ↓
Data Generation / Collection
        ↓
Data Cleaning & Transformation
        ↓
Event Log Preparation
        ↓
Process Mining using PM4Py
        ↓
Process & Bottleneck Analysis
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

CareFlow also simulates operational inefficiencies and loop-backs so that process mining techniques can identify them.

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
Triage  ← Process Loop
      ↓
Doctor Review
      ↓
Pharmacy
      ↓
Discharge
```

---

## 🔍 Key Objectives

* Generate realistic timestamped hospital event logs.
* Standardize the event data for process mining.
* Discover the actual patient workflow.
* Identify process bottlenecks.
* Analyze transition and waiting times.
* Detect repeated activities and loop-backs.
* Compare actual patient journeys with expected workflows.
* Build an interactive BI dashboard.
* Provide insights that can support hospital process improvement.

---

## 🛠️ Technology Stack

| Technology       | Purpose                                     |
| ---------------- | ------------------------------------------- |
| **Python**       | Event-log generation and data processing    |
| **Pandas**       | Data manipulation and analysis              |
| **BigQuery**     | Data warehouse for hospital event logs      |
| **dbt**          | Data cleaning and transformation            |
| **PM4Py**        | Process mining and process discovery        |
| **Power BI**     | Process and operational analytics dashboard |
| **Git & GitHub** | Version control and team collaboration      |

---
## ▶️ How to Run

### 1. Clone the Repository

Clone the repository and navigate to the project folder.

```bash
git clone <https://github.com/anaghaspillai/CareFlow-Clinical-Pathway-Analytics>
cd CareFlow-Clinical-Pathway-Analytics
```

### 2. Install Dependencies

Install the required Python library:

```bash
pip install -r requirements.txt
```

### 3. Generate the Hospital Event Log

Run the Python event log generator:

```bash
python src/generate_events.py
```

This generates the simulated hospital patient event data and saves it as a CSV file.

### 4. Clean the Event Log

Run the event cleaning script:

```bash
python src/clean_events.py
```

This cleans and prepares the generated event log for the next stage of the project.

### 5. Current Workflow

The current implementation follows this workflow:

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
PM4Py (Next Week)
```

> **Note:** BigQuery, PM4Py, and Power BI will be implemented in the upcoming phases of the project.
## 📊 Expected Analysis

The project will analyze:

* Patient flow
* Activity sequences
* Waiting times
* Process transitions
* Repeated activities
* Bottlenecks
* Process deviations
* Patient journey variations

---

## 📅 Project Development Plan

### Week 1 – Event Log Engineering

* Generate mock hospital event logs using Python.
* Create realistic patient journeys.
* Introduce operational inefficiencies and loop-backs.
* Load raw event logs into BigQuery.
* Begin initial data cleaning and preparation.

### Week 2 – Event Normalization & Process Discovery

* Standardize the event log.
* Prepare `Case_ID`, `Activity`, and `Timestamp` fields.
* Use PM4Py to discover the actual patient process.
* Generate a process graph representing patient flows.

### Week 3 – Bottleneck Analysis & Dashboard

* Calculate transition and waiting times.
* Identify major process bottlenecks.
* Connect the processed data to Power BI.
* Build operational and process-mining visualizations.

### Week 4 – Conformance Checking & Finalization

* Compare actual patient journeys with the expected workflow.
* Identify non-compliant or inefficient paths.
* Add filtering and drill-down capabilities.
* Finalize the dashboard and documentation.

---

## 📁 Project Structure

```text
CareFlow/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── generate_events.py
│   └── clean_events.py
│
├── notebooks/
│
├── dashboard/
│
├── README.md
├── PROJECT_DOCUMENTATION.md
└── requirements.txt
```

---

## 👥 Team Collaboration

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

## 🎯 Expected Outcome

The final CareFlow system will provide a process-oriented view of hospital operations rather than only traditional numerical KPIs.

It will help reveal where patient journeys become inefficient, where bottlenecks occur, and which process paths require improvement.

---

## 📚 Project Reference

This project is developed as part of the **Infotact Solutions Advanced Data Analytics** internship project.
