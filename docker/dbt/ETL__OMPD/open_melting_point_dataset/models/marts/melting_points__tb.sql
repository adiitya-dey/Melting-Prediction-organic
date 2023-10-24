{{ config(
    materialized='table',
    schema='data_warehouse'
    ) }}

select S.key, S.name, S.smiles, S.melting_temperature_C
from {{ ref('stg_bradley_data__vw') }} S
where S.key not in (select key from {{ ref('stg_identify_duplicates__vw') }})
