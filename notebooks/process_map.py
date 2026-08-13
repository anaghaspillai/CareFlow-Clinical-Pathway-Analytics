import pandas as pd
import pm4py

# Load the cleaned hospital event log
df = pd.read_csv("data/hospital_event_log_clean.csv")

# Convert Timestamp to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Prepare the event log for PM4Py
event_log = pm4py.format_dataframe(
    df,
    case_id="Case_ID",
    activity_key="Activity_Name",
    timestamp_key="Timestamp"
)

# Discover the process map using Inductive Miner
process_tree = pm4py.discover_process_tree_inductive(event_log)

# Convert the process tree to a Petri net
net, initial_marking, final_marking = pm4py.convert_to_petri_net(process_tree)

# Save the process map as an image
pm4py.save_vis_petri_net(
    net,
    initial_marking,
    final_marking,
    "process_map.png"
)

print("Process map generated successfully!")