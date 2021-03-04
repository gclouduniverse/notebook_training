import pytest
from gcloud_notebook_training import utils

def test_get_notebook_name_absolute():
    assert 'notebook.ipynb' == utils.get_notebook_name('/some/path/for/notebook.ipynb')

def test_get_notebook_name_local():
    assert 'notebook.ipynb' == utils.get_notebook_name('notebook.ipynb')

def test_get_notebook_name_gcs():
    assert 'notebook.ipynb' == utils.get_notebook_name('gs://bucket_name/path/to/notebook.ipynb')

def test_is_gcs_uri_true():
    assert utils.is_gcs_uri("gs://gcs/path")

def test_is_gcs_uri_false():
    assert not utils.is_gcs_uri("/local/path")

def test_get_job_id():
    assert "job_Notebook_ipynb_2019_23_05_12_34_4535_34545" \
        == utils.get_job_id("Notebook.ipynb", "2019/23/05-12:34:4535.34545")

def test_get_output_notebook_with_extension():
    assert "/local/path/notebook_output.ipynb" \
        == utils.get_output_notebook("/local/path/notebook.ipynb")

def test_get_output_notebook_with_wrong_extension():
    assert "/local/path/notebook.ipynbak_output" \
        == utils.get_output_notebook("/local/path/notebook.ipynbak")

def test_get_output_notebook_without_extension():
    assert "/local/path/notebook_output" \
        == utils.get_output_notebook("/local/path/notebook")

def test_notebook_is_in_path():
    assert utils.notebook_is_in_path("/local/path/notebook.ipynb", "/local/path")
    assert utils.notebook_is_in_path("/local/path/notebook.ipynb", "/local")
    assert not utils.notebook_is_in_path("/local/path/notebook.ipynb", "/remote")
    assert utils.notebook_is_in_path("gs://local/path/notebook.ipynb", "gs://local")

