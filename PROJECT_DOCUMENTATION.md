# CareFlow – Clinical Pathway Process Mining

## 📌 Project Overview

CareFlow is a healthcare process analytics project focused on understanding patient journeys through hospital workflows.

The project uses timestamped hospital event data to prepare and analyze the sequence of activities followed by patients. The goal is to identify inefficient process paths, repeated activities, and bottlenecks in the patient journey.

During Week 1, the focus is on **preparing and understanding the hospital event data**. Process mining and dashboard development will be carried out in the upcoming weeks.

---

## 🎯 Problem Statement

Hospital workflows involve multiple activities such as registration, triage, consultation, diagnostic tests, review, pharmacy, and discharge.

Patients may experience delays or repeated activities during this process. One example of an inefficient process is:

```text
Triage
   ↓
X-Ray
   ↓
Triage
```

This type of repeated process may indicate a potential bottleneck or inefficiency.

CareFlow aims to prepare the patient event data so that these process patterns can be analyzed using process mining techniques in the next phase.

---

## 💡 Project Objective

The main objective of CareFlow is to analyze patient event logs and understand how patients move through hospital workflows.

The project aims to:

- Generate realistic hospital patient event data.
- Prepare and clean the event log.
- Understand the sequence of patient activities.
- Perform basic exploratory data analysis.
- Identify repeated activities and potential bottlenecks.
- Use process mining to discover the actual patient workflow.
- Visualize important process insights in later phases.

---

## 🏥 Patient Journey

The simulated hospital workflow contains activities such as:

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

The generated data also contains some intentionally simulated process inefficiencies.

For example:

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

The repeated **Triage** activity will be investigated during the analysis phase.

---

## 📊 Current Week 1 Implementation

Week 1 focuses on **data preparation and initial understanding of the hospital event log**.

The current implementation follows:

```text
Python Event Generator
        ↓
Hospital Patient Event Log
        ↓
Raw CSV
        ↓
clean_events.py
        ↓
Cleaned CSV
        ↓
Basic EDA
        ↓
Ready for PM4Py in Week 2
```

### Completed / Current Work

- Created a Python-based hospital event log generator.
- Generated simulated patient journeys.
- Stored the generated event log as a CSV file.
- Created `clean_events.py` for cleaning the event data.
- Generated a cleaned CSV ready for the next phase.
- Started preparing the data dictionary.
- Planned basic exploratory data analysis.
- Investigating the **Triage → X-Ray → Triage** process loop.
- Started researching PM4Py concepts for Week 2.

---

## 🔍 Week 1 Data Preparation

### 1. Event Log Generation

The Python generator creates simulated patient journeys through different hospital activities.

Each patient's journey is represented using a unique `Case_ID`.

Example:

```text
P0001
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

### 2. Raw Event Log

The generated patient events are stored in a CSV file.

The raw CSV represents the initial hospital event log before cleaning.

### 3. Data Cleaning

The `clean_events.py` script is used to prepare the raw event log for further analysis.

The cleaned CSV will be used as the input for process mining in Week 2.

### 4. Exploratory Data Analysis

Basic EDA is being performed to understand:

- Number of patients
- Number of events
- Activity distribution
- Patient journey patterns
- Repeated activities
- Potential process bottlenecks
- Triage → X-Ray → Triage loop

---

## 📖 Data Dictionary

The event log contains patient and activity information.

| Column | Description |
|---|---|
| `Case_ID` | Unique identifier representing a patient's journey |
| `Activity` | Hospital activity performed during the patient's journey |
| `Timestamp` | Date and time at which the activity occurred |
| `Patient_Age` | Age of the patient |
| `Gender` | Gender of the patient |

> The data dictionary will be updated if additional fields are introduced during the project.

---

## 🛠️ Technology Stack

### Currently Used

| Technology | Purpose |
|---|---|
| **Python** | Hospital event log generation and data processing |
| **Pandas** | Data cleaning and exploratory data analysis |
| **CSV** | Storage of raw and cleaned event logs |
| **Git & GitHub** | Version control and team collaboration |

### Upcoming Technologies

The following technologies will be introduced in later project phases:

| Technology | Planned Purpose |
|---|---|
| **PM4Py** | Process mining and process discovery |
| **BigQuery** | Data warehouse, if required later |
| **Power BI** | Dashboard and visualization |

---

## ▶️ How to Run

### 1. Clone the Repository

Clone the repository and navigate to the project folder.

```bash
git clone <https://github.com/anaghaspillai/CareFlow-Clinical-Pathway-Analytics>
cd CareFlow-Clinical-Pathway-Analytics
```

### 2. Install Dependencies

Install the currently required Python dependency:

```bash
pip install -r requirements.txt
```

The current `requirements.txt` contains:

```text
pandas
```

Additional libraries will be added as new project components are implemented.

### 3. Generate the Hospital Event Log

Run the Python event generator:

```bash
python src/generate_events.py
```

This generates the simulated hospital patient event data and saves the raw event log as a CSV file.

### 4. Clean the Event Log

Run the cleaning script:

```bash
python src/clean_events.py
```

This prepares the raw event log and produces the cleaned CSV for further analysis.

### 5. Current Workflow

```text
generate_events.py
       ↓
Raw Hospital Event Log
       ↓
Raw CSV
       ↓
clean_events.py
       ↓
Cleaned CSV
       ↓
Basic EDA
       ↓
PM4Py – Week 2
```

---

## 📅 Development Plan

### Week 1 – Data Preparation

The main focus of Week 1 is preparing and understanding the hospital event data.

#### Tasks

- Finalize README and project documentation.
- Create and maintain `requirements.txt`.
- Generate hospital event logs using Python.
- Clean the event data using `clean_events.py`.
- Finalize the data dictionary.
- Perform basic exploratory data analysis.
- Investigate the **Triage → X-Ray → Triage** bottleneck loop.
- Research PM4Py concepts and prepare for Week 2.
- Conduct a team check-in and review pending work.

### Week 1 Output

```text
Raw Patient Event Data
        ↓
Raw CSV
        ↓
Cleaned CSV
        ↓
Basic Data Understanding
        ↓
Ready for Process Mining
```

---

### Week 2 – Process Analysis

Week 2 will move from **data preparation to actual process analysis**.

#### Planned Workflow

```text
Cleaned CSV
     ↓
PM4Py
     ↓
Process Discovery
     ↓
Patient Process Map
     ↓
Identify Bottlenecks
     ↓
Analyze Triage → X-Ray → Triage
     ↓
Basic Dashboard
```

The main focus will be understanding the actual patient process and identifying inefficient paths.

---

## 🔮 Future Development

After the initial process analysis, the project can be extended with:

- Detailed process discovery using PM4Py.
- Bottleneck and waiting-time analysis.
- Process deviation analysis.
- Conformance checking.
- Interactive dashboard development.
- Additional data warehouse integration if required.

These components will be added as the project progresses.

---

## 📁 Project Structure

```text
CareFlow-Clinical-Pathway-Analytics/
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

## 👥 GitHub Collaboration

The project is developed collaboratively using Git and GitHub.

Each team member works on their own development branch.

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

The `main` branch contains the reviewed and merged project work.

---

## 📌 Current Project Status

**Current Phase:** Week 1 – Data Preparation

### Status

- ✅ Python event generator
- ✅ Hospital event log generation
- ✅ Raw CSV
- ✅ Event cleaning using `clean_events.py`
- ✅ Cleaned CSV
- 🔄 Data dictionary
- 🔄 Basic EDA
- 🔄 Triage → X-Ray → Triage bottleneck investigation
- 🔄 PM4Py preparation

### Next Major Step

The next phase will begin with the cleaned CSV and use **PM4Py for process discovery and patient workflow analysis**.

---

## 📚 Project Context

CareFlow is being developed as part of the **Infotact Solutions Advanced Data Analytics internship project**.

The implementation is being developed incrementally, with **Week 1 focused on preparing the event data** and **Week 2 focused on process analysis**.
