import flask
import subprocess
import os
from google.cloud import storage
from flask import request

app = flask.Flask(__name__)


def upload_blob(file_name):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/secrets/storage-creator"
    client = storage.Client()
    bucket_name = 'datasets-meltingpointprediction'
    source_file_name =  file_name
    destination_blob_name = "SDF/" + file_name

    try:
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
    except blob.Error as e:
        return f"Error uploading the file: {e}"
    else:
        return f"{source_file_name} uploaded successfully to {destination_blob_name}."
    


@app.route('/', methods=['GET'])
def home():
    smiles = request.args.get('smiles')
    key = request.args.get('key')
    request.encoding_errors

    try:
        file_name = key + '.sdf'
        subprocess.run(['obabel','-:',smiles,'-O', file_name, '--seperate', '--unique', '--gen3D'], \
                       check=True, text=True)
    except subprocess.CalledProcessError as e:
        return f"Error running the subprocess: {e}"
    else:
        upload_blob(file_name)

    

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)