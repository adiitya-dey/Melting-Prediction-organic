from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os

# from flask import request, make_response, jsonify
# import uvicorn

app = FastAPI()
    

class Smiles(BaseModel):
    key: str
    smiles: str   


@app.post('/api/smilestosdf/', status_code=201)
async def smiles_to_sdf(smiles: Smiles):

    # Set the sdf file name based on key.
    file_name = smiles.key + '.sdf'

    # Set the smiles to input to open babel.
    smile_name = '-:' + smiles.smiles


    # Run the open babel to convert smiles to sdf file.
    try:

        result = subprocess.run(['obabel', smile_name,'-O', file_name, '--seperate', '--unique', '--gen3D'], \
                        check=True, text=True, capture_output=True)
        
    except Exception as e:
        raise HTTPException(status_code=500, 
                            detail=[{"msg": "obabel subprocess failed.",
                                    "error": e}]
                            )
    
    # Check if file is created.
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        return upload_blob(file_name)
    else:
        raise HTTPException(status_code=500, 
                            detail=[{"msg": f"File does not exists. Conversion failed. Run the obabel for smiles:{smiles.smiles} to check the error."}]
                            )