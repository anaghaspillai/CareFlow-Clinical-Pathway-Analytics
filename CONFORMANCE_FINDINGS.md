# Conformance Checking Findings — CareFlow

## 1. Overview

Conformance checking compares each patient's actual activity sequence against
the ideal hospital pathway (Triage → X-Ray → Doctor Consult → Discharge) to
quantify how often the real-world process deviates from the expected flow.

## 2. Method

Each of the 200 patient cases was checked against the ideal path. A patient
is marked **conformant** if their recorded activity sequence exactly matches
Triage → X-Ray → Doctor Consult → Discharge, with no repeated or extra steps.

## 3. Results

- **Total patients:** 200
- **Conformant (followed ideal path):** 127 (63.5%)
- **Deviating (loop-back or other):** 73 (36.5%)

## 4. Key Finding

The 36.5% deviation rate exactly matches the bottleneck found in three
independent analyses:

1. Manual EDA (Day 3) — 73/200 patients looped Triage→X-Ray→Triage
2. PM4Py algorithmic process discovery (Day 6) — same loop-back pattern confirmed
3. Formal conformance checking (Day 8) — 36.5% deviation rate confirmed

This consistency across three separate methods strengthens confidence that
the X-Ray→Triage loop-back is a genuine, significant bottleneck in the
hospital's patient flow, not a data artifact.

## 5. Next Steps

- Investigate the root cause of the X-Ray→Triage loop (e.g., missing
  paperwork, as hypothesized in the original project brief)
- Incorporate conformance results into the PowerBI dashboard
- Use this as a foundation for Week 3-4 conformance-checking refinements
