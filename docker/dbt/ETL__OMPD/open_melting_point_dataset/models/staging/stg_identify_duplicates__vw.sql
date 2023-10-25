{{ config(
    materialized='view',
    -- schema='transform_staging'
    ) }}

with duplicate_csids as (

    select csid, count(csid)
    from {{ ref('stg_bradley_data__vw') }}
    group by csid
    having count(csid) > 1

),

duplicate_smiles as (

    select smiles, count(smiles)
    from {{ ref('stg_bradley_data__vw') }}
    group by smiles
    having count(smiles) > 1

),

duplicate_names as (

    select name, count(name)
    from {{ ref('stg_bradley_data__vw') }}
    group by name
    having count(name) > 1

)

select key from {{ ref('stg_bradley_data__vw') }}
where name in (select name from duplicate_names) 
or smiles in (select smiles from duplicate_smiles)
 or csid in (select csid from duplicate_csids)