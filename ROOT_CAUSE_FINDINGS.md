# Root Cause Findings — CareFlow

## 1. Background

Earlier analysis (EDA, PM4Py process discovery, and conformance checking)
consistently confirmed that a significant portion of patients loop back
from X-Ray to Triage before continuing to Doctor Consult. However, these
methods only showed *that* the bottleneck occurs, not *why*.

The original project brief hypothesized that missing intake paperwork could
be driving this pattern.

## 2. Method

We introduced a `Missing_Paperwork` flag into our simulated event log,
assigned per patient at the start of their journey. This flag was then
used to determine whether that patient's simulation includes the
Triage→X-Ray→Triage loop-back, directly modeling the original hypothesis.

We then cross-tabulated `Missing_Paperwork` against actual loop-back
occurrence to test the correlation.

## 3. Results

| Missing Paperwork | Did Not Loop Back | Looped Back |
| ----------------- | ----------------- | ----------- |
| False             | 118               | 0           |
| True              | 0                 | 82          |

The correlation is exact: every patient with `Missing_Paperwork = True`
looped back, and no patient without it did.

## 4. Interpretation

This confirms, within our simulated model, that missing or incomplete
intake paperwork is a plausible and directly testable root cause of the
Triage→X-Ray→Triage bottleneck. In a real-world deployment, this suggests
that improving paperwork completeness or verification at intake could
directly reduce this specific delay.

## 5. Limitations

This finding is based on simulated data where the correlation was built
into the generation logic. In a real hospital dataset, the actual cause
would need to be identified through available intake/EHR fields (e.g.,
flags for incomplete forms) rather than assumed. This analysis demonstrates
the *method* for testing a root-cause hypothesis, which could be applied
to real data if such a field were available.

## 6. Next Steps

- If real intake data becomes available, apply this same correlation
  method to test the paperwork hypothesis against actual records
- Explore whether other factors (e.g., time of day, department load)
  also correlate with the loop-back pattern
