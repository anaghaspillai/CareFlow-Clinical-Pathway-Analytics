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
- **Conformant (followed ideal path):** 122 (61.0%)
- **Deviating (loop-back or other):** 78 (39.0%)

## 4. Key Finding

The 39.0% deviation rate exactly matches the bottleneck found in three
independent analyses:

1. Manual EDA (Day 3) — 78/200 patients looped Triage→X-Ray→Triage
2. PM4Py algorithmic process discovery (Day 6) — same loop-back pattern confirmed
3. Formal conformance checking (Day 8) — 39.0% deviation rate confirmed

This consistency across three separate methods strengthens confidence that
the X-Ray→Triage loop-back is a genuine, significant bottleneck in the
hospital's patient flow, not a data artifact.

**Note on updated numbers (added Day 14):** The figures above reflect the
final, stable dataset (878 events, seed=42), not the original figures from
when this doc was first written (73/200, 36.5%). The count moved in two
steps: first from 73→82 after the Day 11 root-cause fix (which tied the
loop-back directly to the `Missing_Paperwork` flag), then from 82→78 after
the Day 13 fix that added a fixed random seed to `generate_events.py` for
reproducibility. The 78/200 (39.0%) figure is now final and will not change
on future runs.

## 5. Next Steps

- Investigate the root cause of the X-Ray→Triage loop (e.g., missing
  paperwork, as hypothesized in the original project brief) — **completed,
  see ROOT_CAUSE_FINDINGS.md**
- Incorporate conformance results into the PowerBI dashboard
- Use this as a foundation for Week 3-4 conformance-checking refinements
