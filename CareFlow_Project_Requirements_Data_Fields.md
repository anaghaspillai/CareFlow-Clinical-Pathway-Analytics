# CareFlow – Project Requirements & Data Fields

## 1. Project Overview

CareFlow is a clinical process analytics project that analyzes the patient journey from registration to discharge. The project aims to identify waiting-time bottlenecks, process deviations, and department-level performance using process mining and business intelligence.

## 2. Project Objective

The main objective is to analyze healthcare process data, understand how patients move through different activities, identify delays and deviations, and present actionable insights through a Power BI dashboard.

## 3. Functional Requirements

| Requirement | Description |
|---|---|
| Patient Journey Analysis | Track the patient journey from registration through discharge. |
| Process Flow Analysis | Understand the sequence in which activities are performed. |
| Waiting-Time Analysis | Calculate waiting time between major process stages. |
| Bottleneck Identification | Identify process stages associated with higher waiting times. |
| Department Analysis | Compare process performance across hospital departments. |
| Process Deviation Detection | Identify repeated or unexpected activities in a patient journey. |
| KPI Calculation | Calculate important process and performance metrics. |
| Process Mining | Use PM4Py to analyze event sequences and process behavior. |
| Dashboard & Visualization | Present KPIs, trends, bottlenecks, and insights in Power BI. |

## 4. Non-Functional Requirements

- Data should be consistent and properly formatted.
- `Patient_ID` should uniquely identify a patient case.
- Timestamps should use a consistent date-time format.
- The dashboard should be simple and easy to understand.
- The project should use synthetic/sample data and should not expose real patient information.
- The analysis should be reproducible and clearly documented.

## 5. Data Fields / Data Dictionary

| Field | Data Type | Description | Example | Source |
|---|---|---|---|---|
| `Patient_ID` | String | Unique identifier for each patient/case. | P0001 | Required |
| `Activity` | String | Process activity performed for the patient. | Registration | Required |
| `Timestamp` | DateTime | Date and time when the activity occurred. | 2026-07-01 09:30 | Required |
| `Department` | String | Hospital department handling the patient. | Cardiology | Required |
| `Doctor_ID` | String | Identifier of the assigned doctor. | D101 | Required |
| `Patient_Type` | String | Type/category of patient. | Emergency | Required |
| `Status` | String | Status of the activity or case. | Completed | Required |
| `Date` | Date | Date extracted from the activity timestamp. | 2026-07-01 | Derived |
| `Waiting_Time` | Numeric | Time spent waiting between process activities. | 35 minutes | Derived |
| `Process_Time` | Numeric | Total time taken for the patient journey. | 249 minutes | Derived |
| `Process_Deviation` | String | Indicates whether the journey contains an unexpected/repeated activity. | Yes | Derived |

## 6. Most Important Fields for Process Mining

PM4Py primarily requires three key fields to reconstruct the patient process:

- **Patient_ID** – identifies the case/patient journey.
- **Activity** – identifies what happened.
- **Timestamp** – identifies when it happened.

### Example

| Patient_ID | Activity | Timestamp |
|---|---|---|
| P001 | Registration | 09:00 |
| P001 | Consultation | 09:30 |
| P001 | Lab Test | 10:30 |
| P001 | Treatment | 12:00 |
| P001 | Discharge | 14:00 |

## 7. Expected Patient Process

**Registration → Consultation → Lab Test → Treatment → Discharge**

The process-mining analysis should also identify deviations from this expected flow, such as a repeated Consultation after Lab Test.

Example:

**Registration → Consultation → Lab Test → Consultation → Treatment → Discharge**

The repeated Consultation can be treated as a process deviation/rework case.

## 8. Derived Metrics / KPIs

- **Total Patients:** Count of unique `Patient_ID` values.
- **Average Process Time:** Average time from the first activity to the final activity.
- **Average Waiting Time:** Average waiting duration between process stages.
- **Lab-to-Treatment Wait:** Treatment timestamp minus Lab Test timestamp.
- **Process Deviation Rate:** Percentage of cases containing a repeated/unexpected activity.
- **Emergency Patient Share:** Percentage of cases categorized as Emergency.
- **Department Performance:** Comparison of process time and waiting time across departments.

## 9. Technology Mapping

| Technology | Purpose in CareFlow |
|---|---|
| Google BigQuery | Store raw event data and perform SQL-based analysis/validation. |
| dbt | Clean, transform, test, and create analytics-ready tables. |
| PM4Py | Perform process mining and identify process flows/deviations. |
| Python/Pandas | Support data preparation, exploration, and calculations. |
| Power BI | Build the final interactive dashboard and visualize KPIs. |

## 10. Project Data Flow

**Raw Data → BigQuery → dbt → PM4Py → Power BI → Insights**

## 11. Data Privacy & Limitations

- The project should use synthetic or anonymized data for the internship demonstration.
- No real patient names, medical records, phone numbers, addresses, or other personally identifiable information should be included.
- Waiting times and process behavior in a sample dataset should not be presented as actual hospital performance.

## 12. Handover Note

This document defines the initial project requirements and data dictionary for CareFlow. The fields and requirements can be updated after the team confirms the final dataset, business rules, and dashboard requirements.
