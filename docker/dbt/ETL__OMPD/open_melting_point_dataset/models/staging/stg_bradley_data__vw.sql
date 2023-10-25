{{ config(
    materialized='ephemeral'
    ) }}

with source_data as (

    select key, chemical_name, smiles, melting_temperature_C
    from {{ ref('bradley_data') }}
    where donotuse is null

)

select *
from source_data

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null