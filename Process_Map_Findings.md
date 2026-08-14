Process Map Findings – CareFlow

1. Process Map Overview

The PM4Py process map shows how patients move through the hospital workflow based on the cleaned event log.

The main process flow is:

Triage → X-Ray → Doctor Consult → Discharge

The process map also shows a repeated Triage path after X-Ray for some patient cases. This loop-back represents a process deviation from the main flow.

---

2. Key Finding

The repeated Triage activity after X-Ray indicates that some patients follow an additional path before continuing to Doctor Consult and Discharge.

The process map helps us understand the actual patient flow and identify repeated activities and process deviations that can be investigated further.

---

3. Data Used

The process map was generated using the cleaned hospital event log with PM4Py.

Input file: "data/hospital_event_log_clean.csv"

Main fields used:

- "Case_ID"
- "Activity_Name"
- "Timestamp"