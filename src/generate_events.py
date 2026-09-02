import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

def generate_patient_journey(patient_id, start_time):
    events = []
    current_time = start_time

    # NEW: Simulate root cause - some patients have missing/incomplete paperwork
    missing_paperwork = random.random() < 0.4  # 40% of patients affected

    current_time += timedelta(minutes=random.randint(1, 15))
    events.append((patient_id, "Triage", current_time, missing_paperwork))

    current_time += timedelta(minutes=random.randint(5, 20))
    events.append((patient_id, "X-Ray", current_time, missing_paperwork))

    if missing_paperwork:  # CHANGED: now driven by the root cause, not a raw coin-flip
        current_time += timedelta(minutes=random.randint(10, 30))
        events.append((patient_id, "Triage", current_time, missing_paperwork))

    current_time += timedelta(minutes=random.randint(5, 25))
    events.append((patient_id, "Doctor Consult", current_time, missing_paperwork))

    current_time += timedelta(minutes=random.randint(5, 15))
    events.append((patient_id, "Discharge", current_time, missing_paperwork))

    return events

all_events = []
base_time = datetime(2026, 8, 5, 8, 0)
for i in range(200):
    patient_start = base_time + timedelta(minutes=random.randint(0, 480))
    all_events.extend(generate_patient_journey(f"P{i:03d}", patient_start))

# CHANGED: added Missing_Paperwork column
df = pd.DataFrame(all_events, columns=["Case_ID", "Activity_Name", "Timestamp", "Missing_Paperwork"])
df = df.sort_values(["Case_ID", "Timestamp"])
df.to_csv("data/hospital_event_log.csv", index=False)
print("Event log generated:", len(df), "events for", 200, "patients")