from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()


@app.get('/api/ompd/v1/', status_code=201)
def home():
    try:
        # subprocess.run(['dbt','deps', '--profiles-dir','.', '--project-dir', '/'], check=True, text=True)
        # subprocess.ßrun(['dbt','debug','--target','prod', '--profiles-dir','.', '--project-dir', 'bradley_clean_data/'], check=True, text=True)
        subprocess.run(['dbt','run','--target','prod', '--profiles-dir','.', '--project-dir', 'open_melting_point_dataset/'], check=True, text=True)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=501,
                            detail=[{'msg': "Subprocess failed to run dbt.",
                                     'error': e}]) 
    else:
        return 0