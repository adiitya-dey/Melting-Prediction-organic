{{ config(
    materialized='view',
    schema='transform_staging'
    ) }}

select S.key, S.name, S.smiles, S.melting_temperature_C
from {{ ref('vw__stg_bradley_data') }} S
where S.key not in (select key from {{ ref('vw__stg_identify_duplicates') }})
