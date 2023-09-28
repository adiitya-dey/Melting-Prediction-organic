/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='view') }}

with duplicate_csids as (

    select csid, count(csid)
    from {{ ref('stg__bradley_data') }}
    group by csid
    having count(csid) > 1

),

duplicate_smiles as (

    select smiles, count(smiles)
    from {{ ref('stg__bradley_data') }}
    group by smiles
    having count(smiles) > 1

),

duplicate_names as (

    select name, count(name)
    from {{ ref('stg__bradley_data') }}
    group by name
    having count(name) > 1

)

select S.key, S.name, S.smiles, S.melting_temperature_C
from {{ ref('stg__bradley_data') }} S
where S.name not in (select name from duplicate_names)
and S.smiles not in (select smiles from duplicate_smiles)
and S.csid not in (select csid from duplicate_csids)

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null