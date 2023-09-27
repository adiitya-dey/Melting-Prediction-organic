/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='view') }}

with source_data as (

    select key, name, smiles, melting_temperature_C, csid, donotuse
    from {{ source('dataset001_meltingpointprediction', 'tb_bradley_data_meltingpointprediction') }}
    where donotuse is null

)

select *
from source_data

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null