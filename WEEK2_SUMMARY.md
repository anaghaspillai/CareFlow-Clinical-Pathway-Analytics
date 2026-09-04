# Week 2 Summary — CareFlow

## Overview

Week 2 (Aug 17–21) focused on closing the gap between our Week 1 implementation
and the official project spec, while building out deeper process-mining analysis
ahead of schedule.

## Key Deliverables

### 1. PM4Py Process Discovery (Day 6)

Generated formal Directed Graph and Petri net models using PM4Py's algorithmic
discovery, moving beyond manual pandas calculations. Confirmed the same
Triage→X-Ray→Triage loop-back pattern found in Week 1 EDA.

### 2. BigQuery/dbt Scope Decision (Day 6)

Team decided to defer BigQuery and dbt migration, documented as an intentional
scope decision in README.md rather than an unresolved gap.

### 3. Power BI Dashboard (Days 7, 9, 10)

Built a working dashboard connected to the cleaned event log, including:

- Total Cases, Deviating %, Total Events KPI cards
- Activity Counts bar chart
- Conformance Split pie chart
  Refined based on team feedback (Vaishnavi) for clearer layout and naming.

### 4. Conformance Checking (Day 8)

Built formal conformance-checking logic comparing actual patient paths against
the ideal path. Result: 36.5% of patients deviate — matching the bottleneck
finding from three independent methods (manual EDA, PM4Py, conformance checking).

## Consistency Check

All three analytical methods and the dashboard now show matching figures:

- 200 total patients, 873 total events
- 36.5% deviation / bottleneck rate
- Average loop-back wait time: 20.88 minutes

## Status Going Into Mid-Review (Aug 25–27)

Ahead of the original Week 2 schedule. Ready to present: EDA findings, PM4Py
process discovery, conformance-checking results, and a working Power BI dashboard.
