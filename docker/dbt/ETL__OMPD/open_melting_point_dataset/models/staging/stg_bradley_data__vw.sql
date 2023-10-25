{{ config(
    materialized='ephemeral',
    -- schema='transform_staging'
    ) }}

with source_data as (

    select key, chemical_name, smiles, melting_point_celcius, csid, donotuse
    from {{ ref('bradley_data') }}
    where donotuse is null

)

select *
from source_data

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null