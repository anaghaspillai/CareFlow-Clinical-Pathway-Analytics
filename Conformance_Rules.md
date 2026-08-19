# CareFlow – Conformance Checking Rules

## 1. Ideal Process Flow

The ideal patient flow used for conformance checking is:

**Triage → X-Ray → Doctor Consult → Discharge**

---

## 2. What Counts as a Conformance Issue

A patient case is considered a conformance issue when its actual activity sequence differs from the defined ideal process flow.

For example:

**Ideal:** Triage → X-Ray → Doctor Consult → Discharge

**Deviation:** Triage → X-Ray → Triage → Doctor Consult → Discharge

The repeated Triage activity is therefore counted as a process deviation.

---

## 3. Waiting Time and Deviation Impact

Waiting time is considered separately from conformance.

A deviation does not automatically mean that it caused a significant delay. Transition and waiting-time analysis can be used to understand the operational impact of each deviation.

This allows the project to distinguish between:

- **Process deviation:** The actual path differs from the ideal flow.
- **Operational impact:** The deviation is associated with additional waiting or transition time.

---

## 4. Current Focus

The repeated Triage path after X-Ray is the main process deviation identified in the current process map.

The conformance-checking results can be used to measure how many patient cases follow this different path and investigate its impact on the overall patient journey.
