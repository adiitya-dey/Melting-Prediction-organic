import flask
import subprocess
import os
from google.cloud import storage
from flask import request, make_response, jsonify

app = flask.Flask(__name__)


# def upload_blob(file_name):
#     os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/secrets/storage-creator"
#     client = storage.Client()
#     bucket_name = 'datasets-meltingpointprediction'
#     source_file_name =  file_name
#     destination_blob_name = "SDF/" + file_name
    
#     try:
#         bucket = client.bucket(bucket_name)
#         blob = bucket.blob(destination_blob_name)
#         blob.upload_from_filename(source_file_name)
#     except Exception as e:
#         return f"Error uploading the file: {e}"
#     else:
#         return f"{source_file_name} uploaded successfully to {destination_blob_name}."

    


@app.route('/', methods=['POST'])
def home():
    
    # Validate if the parameters for key and smiles are passed.
    data = request.get_json()
    if data["key"] is None:
        message = {'message': f'Invalid Parameter passed for key.'}
        return make_response(jsonify(message), 400)
    elif data["smiles"] is None:
        message = {'message': f'Invalid Parameter passed for smiles.'}
        return make_response(jsonify(message), 400)
    

    # Set the sdf file name based on key.
    file_name = data["key"] + '.sdf'

    # Set the smiles to input to open babel.
    smile_name = '-:' + data["smiles"]

    # Run the open babel to convert smiles to sdf file.
    result = subprocess.run(['obabel', smile_name,'-O', file_name, '--seperate', '--unique', '--gen3D'], \
                    check=True, text=True, capture_output=True)
    
    # Check status of open babel conversion.
    if result.returncode == 0:

        # Check if open babel converted smiles to 1 molecule.
        if "0 molecules converted" in result.stdout:
            message =  {"message": f"Molecule did not convert successfully. Error: {result.stdout}"}
            return make_response(jsonify(message), 500)
        
    else:
        message =  {"message": f"Open babel failed conversion. Error: {result.stderr}"}
        return make_response(jsonify(message), 500)

    

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)