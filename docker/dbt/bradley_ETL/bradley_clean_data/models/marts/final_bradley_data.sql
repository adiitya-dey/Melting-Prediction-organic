{{ config(materialized='table') }}

select * from {{ ref('stg__remove_duplicates') }}