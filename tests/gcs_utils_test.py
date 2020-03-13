import pytest
from gcloud_notebook_training import gcs_utils

def test_get_bucket_name_and_path():
    bucket_name, path = gcs_utils.get_bucket_name_and_path('gs://bucket_name/path/to/file.ext')

    assert "bucket_name" == bucket_name
    assert "path/to/file.ext" == path