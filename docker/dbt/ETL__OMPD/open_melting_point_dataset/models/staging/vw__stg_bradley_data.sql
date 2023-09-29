{{ config(
    materialized='ephemeral',
    schema='raw_data'
    ) }}

with source_data as (

    select key, name, smiles, melting_temperature_C, csid, donotuse
    from {{ source('raw_data', 'tb_open_melting_point_dataset') }}
    where donotuse is null

)

select *
from source_data

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null