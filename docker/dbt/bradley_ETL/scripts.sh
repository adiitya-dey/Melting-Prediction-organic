#!/bin/sh
dbt deps --profiles-dir bradley_clean_data/.  # Pulls the most recent version of the dependencies listed in your packages.yml from git
dbt debug --target dev --profiles-dir bradley_clean_data/.
dbt debug --target prod --profiles-dir bradley_clean_data/.
dbt run --target prod --profiles-dir bradley_clean_data/.
dbt test --data --target dev --profiles-dir bradley_clean_data/.