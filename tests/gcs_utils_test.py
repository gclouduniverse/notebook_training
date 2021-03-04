import pytest
from gcloud_notebook_training import gcs_utils

def test_get_bucket_name_and_path():
    bucket_name, path = gcs_utils.get_bucket_name_and_path('gs://bucket_name/path/to/file.ext')

    assert "bucket_name" == bucket_name
    assert "path/to/file.ext" == path

def test_get_top_folder():
    assert "to" == gcs_utils.get_top_folder("some/path/to")
    assert "to" == gcs_utils.get_top_folder("some/path/to/")
    assert "to" == gcs_utils.get_top_folder("/to")
    assert "to" == gcs_utils.get_top_folder("to")
    assert "to" == gcs_utils.get_top_folder("./to")
    assert "" == gcs_utils.get_top_folder("./")
    assert "" == gcs_utils.get_top_folder(".")

def test_get_notebook_uri_in_folder():
    path = gcs_utils.get_notebook_uri_in_folder('/some/path/to1/file.ext', '/some/path', "gs://bucketName/new_path")
    assert "gs://bucketName/new_path/to1/file.ext" == path

    path = gcs_utils.get_notebook_uri_in_folder('some/path/to2/file.ext', 'some/path/', "gs://bucketName/new_path")
    assert "gs://bucketName/new_path/to2/file.ext" == path

    path = gcs_utils.get_notebook_uri_in_folder('./some/path/to3/file.ext', '.', "gs://bucketName/new_path")
    assert "gs://bucketName/new_path/some/path/to3/file.ext" == path
