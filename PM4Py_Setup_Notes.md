# PM4Py Setup Notes

## 1. What is PM4Py?

PM4Py is a Python library used for process mining. It helps us understand how a process actually happens from event log data.

For CareFlow, PM4Py can help us:
- Understand the patient process flow.
- Check activity sequences.
- Find repeated activities or process deviations.
- Analyze transitions between activities.

## 2. Installation

Install PM4Py using:

```bash
pip install pm4py
```

## 3. Check Installation

After installation, run:

```python
import pm4py
print(pm4py.__version__)
```

If the version is displayed without an import error, PM4Py is installed correctly.

## 4. Required Event Log Format

For CareFlow, the basic input needs three important fields:

| Field | Purpose |
|---|---|
| `Patient_ID` | Identifies each patient/case |
| `Activity` | Shows the activity performed |
| `Timestamp` | Shows when the activity happened |

In process-mining terms:

- `Patient_ID` = Case ID
- `Activity` = Activity/Event
- `Timestamp` = Time

## 5. Example

```text
Patient_ID   Activity          Timestamp
P001         Triage            09:00
P001         X-Ray             09:15
P001         Doctor Consult    09:40
P001         Discharge         10:10
```

## 6. CareFlow Process

Based on the current event dataset, the observed process flow is:

**Triage → X-Ray → Doctor Consult → Discharge**

## 7. Why We Use PM4Py in CareFlow

PM4Py can be used to:
- Discover the actual process flow.
- Identify repeated activities.
- Find process deviations.
- Analyze activity transitions.
- Support bottleneck analysis.

## 8. Note

The current CareFlow event log should be checked before process mining to make sure the case ID, activity names and timestamps are correctly formatted.

This setup note covers the basic PM4Py installation and input requirements for the project.
