{{ config(materialized='table') }}

select
    Case_ID,
    Activity_Name,
    Timestamp,
    Missing_Paperwork
from {{ ref('stg_hospital_event_log') }}