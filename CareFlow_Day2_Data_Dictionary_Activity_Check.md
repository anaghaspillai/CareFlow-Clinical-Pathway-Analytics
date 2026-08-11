# CareFlow – Day 2 Data Dictionary & Activity Validation

## 1. Purpose

This document continues the CareFlow project requirements work from Day 1. The purpose is to validate the data dictionary and check the activities in the patient journey before process mining and dashboard development.

## 2. Data Dictionary

| Field | Data Type | Description | Validation / Check |
|---|---|---|---|
| `Patient_ID` | String | Unique identifier for each patient/case. | Should not be blank and should identify one case. |
| `Activity` | String | Process activity performed for the patient. | Check spelling, naming consistency and valid activity values. |
| `Timestamp` | DateTime | Date and time when the activity occurred. | Should be valid and chronological for each case. |
| `Department` | String | Department handling the patient. | Check missing or inconsistent names. |
| `Doctor_ID` | String | Identifier of the assigned doctor. | Check missing or inconsistent IDs. |
| `Patient_Type` | String | Patient category, such as Emergency or Regular. | Check category names for consistency. |
| `Status` | String | Status of the case/activity. | Check valid values and missing values. |
| `Date` | Date | Date derived from the activity timestamp. | Should match the date portion of `Timestamp`. |
| `Waiting_Time` | Numeric | Time between two process activities. | Calculate from consecutive timestamps. |
| `Process_Time` | Numeric | Total duration of the patient journey. | Calculate from first to final activity. |
| `Process_Deviation` | String | Indicates whether the process differs from the expected flow. | Check repeated, missing or unexpected activities. |

## 3. Key Fields for Process Mining

The three main fields required for process mining are:

1. **Patient_ID** – Case identifier.
2. **Activity** – Event/activity performed.
3. **Timestamp** – Time at which the event occurred.

These fields allow PM4Py to reconstruct the actual patient journey.

## 4. Expected CareFlow Activity Sequence

**Registration → Consultation → Lab Test → Treatment → Discharge**

| Order | Activity | Description |
|---:|---|---|
| 1 | Registration | Patient enters the process and is registered. |
| 2 | Consultation | Patient is assessed by the doctor. |
| 3 | Lab Test | Required laboratory test is performed. |
| 4 | Treatment | Treatment or procedure is provided. |
| 5 | Discharge | Patient completes the process. |

## 5. Activity Validation Checklist

### Activity Names
Check whether the same activity has different names.

Examples:
- `Lab Test`
- `LabTest`
- `Laboratory Test`

If they represent the same activity, standardize them to **Lab Test**.

### Activity Sequence
Check whether activities generally follow:

**Registration → Consultation → Lab Test → Treatment → Discharge**

Use the timestamp to determine the actual order.

### Repeated Activities
Check whether an activity occurs more than once for the same patient.

Example:

**Registration → Consultation → Lab Test → Consultation → Treatment → Discharge**

The repeated Consultation may represent rework/process deviation and should be investigated.

### Missing Activities
Check for journeys where an expected activity is missing.

Example:

**Registration → Lab Test → Treatment → Discharge**

Consultation is missing and should be flagged for investigation.

### Unexpected Sequence
Check for unusual activity sequences.

Example:

**Registration → Treatment → Consultation → Discharge**

Flag such cases for review.

### Timestamp Validation
For each `Patient_ID`:
- Sort events by `Timestamp`.
- Check that timestamps are valid.
- Check chronological order.
- Check duplicate timestamps where relevant.
- Check unusually large waiting intervals.

## 6. Activity Standardization Rules

| Issue | Action |
|---|---|
| Different spelling of same activity | Standardize to one name |
| Extra spaces | Remove extra spaces |
| Different capitalization | Use consistent capitalization |
| Blank activity | Flag for data-quality review |
| Repeated activity | Investigate as possible rework/deviation |
| Missing expected activity | Flag for investigation |
| Invalid timestamp | Correct if source information is available; otherwise flag |

## 7. Validation Checklist

- [ ] All required activity names are identified.
- [ ] Activity names are standardized.
- [ ] `Patient_ID` is available for every event.
- [ ] `Timestamp` is available and valid.
- [ ] Events are sorted chronologically for each patient.
- [ ] Expected process flow is documented.
- [ ] Repeated activities are identified.
- [ ] Missing activities are identified.
- [ ] Unusual sequences are flagged.
- [ ] Data-quality issues are documented.

## 8. Findings to Record

| Validation Area | Finding | Action |
|---|---|---|
| Activity names | To be checked against dataset | Standardize inconsistent names |
| Activity order | Compare with expected CareFlow flow | Flag unusual sequences |
| Repeated activities | Check patient-level event sequences | Investigate possible rework |
| Missing activities | Check each patient journey | Flag for review |
| Timestamps | Check validity and chronological order | Correct/flag data issues |
| Waiting times | Check unusually long intervals | Review as possible bottlenecks |

**Important:** Update the findings after checking the actual event dataset. Do not assume a deviation exists unless it is confirmed in the data.

## 9. Handover to Team

This Day 2 document provides the data dictionary and activity-validation framework for CareFlow. The next step is to apply these checks to the actual event dataset and share confirmed findings with the team before process-mining analysis.

### Project Flow

**Raw Event Data → Data Validation → Activity Checking → Process Mining (PM4Py) → KPI Analysis → Power BI Dashboard**

## 10. Technologies Relevant to This Task

- **Python/Pandas:** Data inspection, cleaning and validation.
- **Google BigQuery:** Store/query event data if used by the team.
- **dbt:** Data transformation and validation if included in the project workflow.
- **PM4Py:** Process discovery and process-deviation analysis.
- **Power BI:** Final KPI and dashboard visualization.

  ## 11. Actual Dataset Validation

After checking the actual event dataset:

- Total patients/cases: **200**
- Total event records: **873**
- Missing values: **0**
- Duplicate records: **0**
- Activities found: **Triage, X-Ray, Doctor Consult, Discharge**

### Actual Process Flow

**Triage → X-Ray → Doctor Consult → Discharge**

### Process Deviation

**73 patients (36.5%)** had a repeated **Triage** activity after X-Ray.

Example:

**Triage → X-Ray → Triage → Doctor Consult → Discharge**

This can be considered a possible process deviation/rework case.

### Waiting Time

The average **X-Ray → Triage** waiting time in these repeated cases was approximately **20.88 minutes**, so it can be checked as a possible bottleneck.

### Observation

The original project documentation mentioned **Lab Test** and **Treatment**, but these activities are not present in the current event dataset. The team should discuss whether the documentation should be aligned with the actual dataset.
