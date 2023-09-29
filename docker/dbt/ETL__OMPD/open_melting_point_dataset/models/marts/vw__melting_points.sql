{{ config(
    materialized='view',
    schema='data_warehouse'
    ) }}

select S.key, S.name, S.smiles, S.melting_temperature_C
from {{ ref('vw__stg_bradley_data') }} S
where S.name not in (select name from {{ ref('vw__stg_identify_duplicates') }})
