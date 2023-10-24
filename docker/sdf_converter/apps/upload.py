from google.cloud import storage
import os
from fastapi import HTTPException


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