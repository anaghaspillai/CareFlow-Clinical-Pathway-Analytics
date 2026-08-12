# Testing Notes – CareFlow

## 1. Purpose

This document records the testing performed on the CareFlow project by following the **How to Run** instructions from the beginning.

The purpose of this testing is to verify that a new team member can:

- Clone the repository.
- Install the required dependencies.
- Generate the hospital event log.
- Clean the generated event data.
- Perform basic exploratory data analysis (EDA).
- Analyze hospital activities and the Triage → X-Ray → Triage loop.
- Prepare the cleaned data for the PM4Py process mining phase.

---

## 2. Testing Environment

- **Project:** CareFlow – Clinical Pathway Process Mining
- **Operating System:** Windows
- **Python:** Python 3.12
- **IDE:** Visual Studio Code
- **Package Manager:** pip
- **Repository:** CareFlow-Clinical-Pathway-Analytics

---

## 3. Step 1 – Clone the Repository

### Method Used

The repository was cloned directly using the **Clone Git Repository** option in Visual Studio Code.

The repository was opened in the following local directory:

```text
D:\Infotact solution\Careflow-Clinical-Pathway-Analytics\CareFlow-Clinical-Pathway-Analytics
```

### Purpose

This verifies that a team member can obtain the project from GitHub and open it locally.

### Result

**Status: PASS**

The repository was successfully cloned using Visual Studio Code and opened locally.
---
### Alternative Command

The repository can also be cloned using Git from the terminal:

```bash
git clone https://github.com/anaghaspillai/CareFlow-Clinical-Pathway-Analytics
cd CareFlow-Clinical-Pathway-Analytics
```

### Purpose

This step verifies that a new team member can obtain the project from GitHub and open the project locally.

### Result

**Status: PASS**

The repository was successfully cloned using Visual Studio Code and opened locally.
---

## 4. Step 2 – Install Dependencies

### Command Used

```bash
pip install -r requirements.txt
```

### Purpose

This installs the Python libraries required for the current project.

### Result

**Status: PASS**

The dependencies were successfully checked/installed.

The terminal showed:

```text
Requirement already satisfied: pandas
Requirement already satisfied: matplotlib
```

The installed versions reported during testing included:

- Pandas: `2.2.3`
- Matplotlib: `3.10.1`

### Observation

The following message appeared:

```text
Defaulting to user installation because normal site-packages is not writeable
```

This did not cause a failure. The required packages were available and the installation command completed successfully.

---

## 5. Step 3 – Generate the Hospital Event Log

### Command Used

```bash
python src/generate_events.py
```

### Purpose

The event generator creates simulated hospital patient event data representing patient journeys through different hospital activities.

### Result

**Status: PASS**

The event generator executed successfully.

The terminal output was:

```text
Event log generated: 883 events for 200 patients
```

### Generated Data

The generator successfully created:

- **200 unique patients**
- **883 hospital events**

---

## 6. Step 4 – Clean the Event Log

### Command Used

```bash
python src/clean_events.py
```

### Purpose

The cleaning script prepares the generated hospital event log for further analysis.

It checks for missing values, invalid timestamps, duplicate rows, and organizes the event data for analysis.

### Result

**Status: PASS**

The cleaning script executed successfully.

### Missing Values

No missing values were found.

```text
Case_ID          0
Activity_Name    0
Timestamp        0
```

Rows dropped due to missing values:

```text
0
```

### Timestamp Validation

The timestamps were successfully converted and validated.

Rows dropped due to invalid timestamps:

```text
0
```

### Duplicate Check

Duplicate rows removed:

```text
0
```

### Cleaning Summary

```text
Original rows: 883
Final cleaned rows: 883
Total rows removed: 0
Unique patients (Case_ID): 200
Unique activities: ['Triage', 'X-Ray', 'Doctor Consult', 'Discharge']
```

### Output

The cleaned event log was successfully saved to:

```text
data/hospital_event_log_clean.csv
```

---

## 7. Step 5 – Basic Exploratory Data Analysis

### Notebook Used

```text
notebooks/eda.ipynb
```

### Purpose

The EDA notebook is used to understand the cleaned hospital event data before moving to process mining.

The analysis covers:

- Total number of event records.
- Total number of unique patients.
- Distribution of hospital activities.
- Average number of events per patient.
- Patients with repeated Triage activities.
- Investigation of the **Triage → X-Ray → Triage** loop-back.
- Average waiting time from X-Ray to the following Triage in loop-back cases.
- Basic visualization of activity counts.

### Result

**Status: PASS**

The EDA notebook is used to perform the initial analysis of the cleaned event log and investigate the potential bottleneck pattern.

The detailed EDA results are available in:

```text
notebooks/eda.ipynb
```

---

## 8. Complete Week 1 Workflow

The complete Week 1 workflow is:

```text
Clone Repository
       ↓
Install Dependencies
       ↓
Generate Event Log
       ↓
Raw CSV
       ↓
Clean Event Log
       ↓
Cleaned CSV
       ↓
EDA
       ↓
Activity Analysis
       ↓
Triage → X-Ray → Triage Analysis
       ↓
Ready for PM4Py (Week 2)
```

---

## 9. Testing Summary

| Step | Test | Result |
|---|---|---|
| 1 | Clone repository using VS Code | ✅ PASS |
| 2 | Install dependencies | ✅ PASS |
| 3 | Generate hospital event log | ✅ PASS |
| 4 | Check missing values | ✅ PASS |
| 5 | Validate timestamps | ✅ PASS |
| 6 | Check duplicate rows | ✅ PASS |
| 7 | Generate cleaned CSV | ✅ PASS |
| 8 | Run basic EDA using `eda.ipynb` | ✅ PASS |
| 9 | Activity analysis | ✅ PASS |
| 10 | Triage loop-back analysis | ✅ PASS |
| 11 | X-Ray → Triage waiting-time analysis | ✅ PASS |
| 12 | Activity visualization | ✅ PASS |

---

## 10. Final Testing Status

**Overall Status: ✅ PASSED**

The current Week 1 workflow was successfully tested from repository cloning through data preparation and basic EDA.

The complete workflow is:

```text
Clone Repository
       ↓
Install Dependencies
       ↓
Generate Event Log
       ↓
Raw CSV
       ↓
Clean Event Log
       ↓
Cleaned CSV
       ↓
EDA
       ↓
Activity Analysis
       ↓
Bottleneck Analysis
       ↓
Ready for PM4Py
```

The cleaned event log is successfully generated at:

```text
data/hospital_event_log_clean.csv
```

The EDA analysis is available in:

```text
notebooks/eda.ipynb
```

---

