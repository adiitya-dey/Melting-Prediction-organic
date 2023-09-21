from google.cloud import storage
 


def check_file_exists(bucket_name, file_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    return blob.exists()

def load_file(bucket_name, file_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(filename)


if __name__ == '__main__':
    status = check_file_exists('datasets-meltingpointprediction', 'BradleyDataset.csv')

    with open('/tmp/log.txt', "w") as f:
        f.write(f"File status:{status}")

    load_file('datasets-meltingpointprediction', '/tmp/log.txt')


