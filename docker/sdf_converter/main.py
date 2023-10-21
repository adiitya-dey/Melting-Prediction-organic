from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os
from google.cloud import storage
# from flask import request, make_response, jsonify
# import uvicorn

app = FastAPI()


def upload_blob(file_name):

    # Provide path for credentials.
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/secrets/storage-creator"

    # Initiate connection with Cloud.
    client = storage.Client()

    # Bucket Name
    bucket_name = 'datasets-meltingpointprediction'

    # Source and Destination file names.
    source_file_name =  file_name
    destination_blob_name = "SDF/" + file_name
    
    try:
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
    except Exception as e:
        raise HTTPException(status_code=501,
                            detail=[{"msg":f"Upload failed to bucket for {source_file_name}."
                                     }])
    else:
        return f"{source_file_name} uploaded successfully to {destination_blob_name}."
    


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
        
    
    
        # # Check status of open babel conversion.
        # if result.returncode == 0:

        #     # Check if open babel converted smiles to 1 molecule.
        #     if "0 molecules converted" in result.stdout:
        #         raise HTTPException(status_code=500,
        #                             detail=[{"msg": f"{smiles.smiles} Molecule did not convert.",
        #                             "error": result.stdout}]
        #                             )
            
        #     elif "1 molecule converted" in result.stdout:
        #         return f"{file_name} created."
            
        # else:

        #     raise HTTPException(status_code=500,
        #                         detail=[{"msg": "obabel status is failed."}]
        #                         )

    

# if __name__=="__main__":
#     app.run(host="0.0.0.0", port=8080)