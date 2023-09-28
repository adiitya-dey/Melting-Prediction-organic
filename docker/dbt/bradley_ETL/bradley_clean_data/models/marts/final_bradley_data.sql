{{ config(materialized='view') }}

select * from {{ ref('stg__remove_duplicates') }}