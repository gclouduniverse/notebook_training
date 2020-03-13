import logging
from gcloud import storage
import os
import re

from google.api_core.exceptions import AlreadyExists, NotFound
from gcloud.exceptions import Conflict

def upload(file_path, project_id, bucket_name, gcs_file_path):
    client = storage.Client(project=project_id)
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(gcs_file_path)
    blob.upload_from_filename(file_path)

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