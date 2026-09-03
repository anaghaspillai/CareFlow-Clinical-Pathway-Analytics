{{ config(materialized='table') }}

with events as (
    select
        Case_ID,
        Activity_Name,
        Timestamp,
        Missing_Paperwork,
        lead(Activity_Name) over (
            partition by Case_ID
            order by Timestamp
        ) as Next_Activity,
        lead(Timestamp) over (
            partition by Case_ID
            order by Timestamp
        ) as Next_Timestamp
    from {{ ref('patient_events') }}
)

select
    Case_ID,
    Activity_Name,
    Timestamp,
    Missing_Paperwork,
    Next_Activity,
    Next_Timestamp,
    timestamp_diff(Next_Timestamp, Timestamp, minute) as Transition_Duration_Minutes
from events
where Next_Activity is not null