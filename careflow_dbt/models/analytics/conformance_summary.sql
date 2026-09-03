{{ config(materialized='table') }}

with case_activities as (
    select
        Case_ID,
        array_agg(Activity_Name order by Timestamp) as Activities
    from {{ ref('patient_events') }}
    group by Case_ID
),

conformance as (
    select
        Case_ID,
        Activities,

        array_to_string(Activities, ' -> ') as Actual_Pathway,

        (
            array_to_string(Activities, ' -> ')
            = 'Triage -> X-Ray -> Doctor Consult -> Discharge'
        ) as Is_Conformant

    from case_activities
)

select
    Case_ID,
    Actual_Pathway,
    Is_Conformant,
    case
        when Is_Conformant then 'Conformant'
        else 'Deviating'
    end as Conformance_Status
from conformance