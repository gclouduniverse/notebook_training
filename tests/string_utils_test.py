import pytest
from gcloud_notebook_training import string_utils


def test_build_random_str():
    assert 16 == len(string_utils.build_random_str(16))

def test_str_time_stamp():
    assert 26 == len(string_utils.str_time_stamp())