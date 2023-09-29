{{ config(
    materialized='view',
    database='transform_staging'
    ) }}

with duplicate_csids as (

    select csid, count(csid)
    from {{ ref('vw__stg_bradley_data') }}
    group by csid
    having count(csid) > 1

),

duplicate_smiles as (

    select smiles, count(smiles)
    from {{ ref('vw__stg_bradley_data') }}
    group by smiles
    having count(smiles) > 1

),

duplicate_names as (

    select name, count(name)
    from {{ ref('vw__stg_bradley_data') }}
    group by name
    having count(name) > 1

)

select name from duplicate_names
union
select name from duplicate_csids
union
select name from duplicate_smiles

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null