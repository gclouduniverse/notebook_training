import logging
from gcloud import storage
import os
import re
import glob

from google.api_core.exceptions import AlreadyExists, NotFound
from gcloud.exceptions import Conflict

def get_gcs_bucket(project_id, bucket_name):
    check_or_create_bucket(project_id, bucket_name)
    client = storage.Client(project=project_id)
    return client.get_bucket(bucket_name)

def upload(file_path, bucket, gcs_file_path):
    blob = bucket.blob(gcs_file_path)
    blob.upload_from_filename(file_path)

def upload_local_directory_to_gcs(local_path, bucket, gcs_path):
    assert os.path.isdir(local_path)
    for local_file in glob.glob(local_path + '/**'):
        if not os.path.isfile(local_file):
           upload_local_directory_to_gcs(local_file, bucket, gcs_path + "/" + os.path.basename(local_file))
        else:
           remote_path = os.path.join(gcs_path, local_file[1 + len(local_path):])
           upload(local_file, bucket, remote_path)

def download(file_path, project_id, bucket_name, gcs_file_path):
    client = storage.Client(project=project_id)
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(gcs_file_path)
    blob.download_to_filename(file_path)

def check_or_create_bucket(project_id, bucket_name):
    client = storage.Client(project=project_id)
    try:
        client.create_bucket(bucket_name)
    except Conflict:
        logging.info('Bucket {} exists.'.format(bucket_name))

# Given GCS URI return bucket name and path
def get_bucket_name_and_path(uri):
    search_res = re.search(r'^gs://([^\/]+)\/(.*)$', uri)
    return search_res.group(1), search_res.group(2)

def get_top_folder(folder):
    if folder and folder[-1] == '/':
        folder = folder[:-1]
    index = folder.rfind("/")
    top = folder[index + 1:]
    if top == ".":
        top = ""
    return top

def get_notebook_uri_in_folder(notebook, folder, gcsPath):
    if folder and folder[-1] == '/':
        folder = folder[:-1]
    suffix = notebook.replace(folder, "", 1)
    return gcsPath + suffix
