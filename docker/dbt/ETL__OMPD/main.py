from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()


@app.get('/api/v1/dbt/run/ompd/', status_code=201)
async def home():
    try:
        # subprocess.run(['dbt','deps', '--profiles-dir','.', '--project-dir', '/'], check=True, text=True)
        # subprocess.ßrun(['dbt','debug','--target','prod', '--profiles-dir','.', '--project-dir', 'bradley_clean_data/'], check=True, text=True)
        subprocess.run(['dbt','run','--target','dev', '--profiles-dir','.', '--project-dir', 'open_melting_point_dataset/'], check=True, text=True)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500,
                            detail=[{'msg': "Subprocess failed to run dbt." }]
                            ) 
    else:
        return 0
    

@app.get('/api/v1/dbt/run/ompd/seed/', status_code=201)
async def seed():
    try:
        subprocess.run(['dbt','seed','--target','dev', '--profiles-dir','.', '--project-dir', 'open_melting_point_dataset/'], check=True, text=True)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500,
                            detail=[{'msg': "Subprocess failed to run dbt seed."}]
                            )
    else:
        return 0