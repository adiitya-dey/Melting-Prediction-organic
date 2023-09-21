/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='view') }}

with source as (
    
    select * 
    from {{ ref('stg_bradley_data') }}
    
 ),
 
 duplicate_csids as (

    select csid, count(csid)
    from {{ ref('stg_bradley_data') }}
    group by csid
    having count(csid) > 1

)

select S.key, S.name, S.smiles, S.melting_temperature_C
from source S
left join duplicate_csids D on S.csid != D.csid 

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null