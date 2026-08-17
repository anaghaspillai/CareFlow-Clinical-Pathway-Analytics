# Process Map Findings – CareFlow

## 1. Process Map Overview

The PM4Py process map shows how patients move through the hospital workflow based on the cleaned event log.

The main process flow is:

**Triage → X-Ray → Doctor Consult → Discharge**

The process map also shows a repeated **Triage** path after **X-Ray** for some patient cases. This loop-back represents a process deviation from the main flow.

---

## 2. Common Path

The main path visible in the process map is:

**Triage → X-Ray → Doctor Consult → Discharge**

This represents the most direct sequence of the recorded activities in the patient journey.

---

## 3. Key Finding

The repeated **Triage** activity after **X-Ray** indicates that some patients follow an additional path before continuing to **Doctor Consult** and **Discharge**.

This repeated Triage path is the main unusual pattern visible in the process map and represents a process deviation from the main flow.

The process map shows the deviation visually, but it does not by itself confirm the reason for the repeated Triage or whether it causes a waiting-time bottleneck. Further transition and waiting-time analysis can help investigate this.

---

## 4. Other Observations

The process map makes the actual patient flow easier to understand and highlights repeated activities and different paths followed by some patient cases.

The repeated Triage loop can be used as a starting point for further process analysis and conformance checking.

---

## 5. Data Used

The process map was generated using the cleaned hospital event log with **PM4Py**.

**Input file:** `data/hospital_event_log_clean.csv`

**Main fields used:**

- `Case_ID`
- `Activity_Name`
- `Timestamp`
