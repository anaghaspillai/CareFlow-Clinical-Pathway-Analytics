# CareFlow – Dashboard KPI Definitions

## 1. Total Cases

**Definition:** Total number of unique patient cases recorded in the cleaned event log.

**Current value:** 200 cases.

---

## 2. Total Events

**Definition:** Total number of activity records available in the cleaned event log.

**Current value:** 873 events.

---

## 3. Activity Counts

**Definition:** Number of times each hospital activity occurs in the event log.

**Activities:**

- Triage
- X-Ray
- Doctor Consult
- Discharge

This KPI helps compare the frequency of different activities in the patient workflow.

---

## 4. Repeated Triage %

**Definition:** Percentage of patient cases where Triage occurs again after X-Ray.

**Current finding:** 73 out of 200 cases, which is 36.5%.

**Formula:**

Repeated Triage % = Repeated Triage Cases / Total Cases × 100

This KPI helps track the proportion of cases following the repeated Triage path.

---

## 5. Average Waiting Time

**Definition:** Average time between consecutive recorded activities for the same patient case.

The dashboard can show waiting time for transitions such as:

- Triage → X-Ray
- X-Ray → Doctor Consult
- X-Ray → Triage
- Doctor Consult → Discharge

---

## 6. Transition Time

**Definition:** Time taken between one activity and the next activity for the same patient case.

This KPI helps compare different transitions and identify where additional time may be occurring in the process.

---

## 7. Process Deviation %

**Definition:** Percentage of patient cases that do not follow the main expected process flow.

The main expected flow is:

**Triage → X-Ray → Doctor Consult → Discharge**

The repeated Triage path after X-Ray is the main process deviation currently identified.

---

## 8. Activity Performance

**Definition:** Summary of activity frequency and associated transition or waiting times.

This KPI helps compare activities and identify areas that may need further investigation.

---

## 9. Data Source

The KPIs are based on the cleaned hospital event log:

`data/hospital_event_log_clean.csv`

**Main fields used:**

- `Case_ID`
- `Activity_Name`
- `Timestamp`
