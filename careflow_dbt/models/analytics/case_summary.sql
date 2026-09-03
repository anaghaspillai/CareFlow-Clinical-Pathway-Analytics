{{ config(materialized='table') }}

with case_stats as (
    select
        Case_ID,
        count(*) as Total_Events,
        min(Timestamp) as Start_Timestamp,
        max(Timestamp) as End_Timestamp,
        array_agg(Activity_Name order by Timestamp limit 1)[offset(0)] as First_Activity,
        array_agg(Activity_Name order by Timestamp desc limit 1)[offset(0)] as Last_Activity,
        countif(Missing_Paperwork = true) as Events_With_Missing_Paperwork,
        count(distinct Activity_Name) as Distinct_Activities
    from {{ ref('patient_events') }}
    group by Case_ID
),

repeated_activity as (
    select
        Case_ID,
        count(*) > count(distinct concat(Activity_Name, '|', cast(Timestamp as string))) as Has_Repeated_Events
    from {{ ref('patient_events') }}
    group by Case_ID
)

select
    c.Case_ID,
    c.Total_Events,
    c.Start_Timestamp,
    c.End_Timestamp,
    timestamp_diff(c.End_Timestamp, c.Start_Timestamp, minute) as Total_Duration_Minutes,
    c.First_Activity,
    c.Last_Activity,
    c.Events_With_Missing_Paperwork,
    c.Distinct_Activities,
    r.Has_Repeated_Events
from case_stats c
left join repeated_activity r
    on c.Case_ID = r.Case_ID