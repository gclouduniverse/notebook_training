import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gcloud-notebook-training",
    version="0.0.12",
    author="Yuri Chernikov",
    author_email="chernikov@google.com",
    description="Execute Jupyter notebooks in Google Cloud AI training jobs",
    long_description="This package allows to run a Jupyter notebook at Google Cloud AI Platform Training Jobs",
    long_description_content_type="text/markdown",
    url="https://github.com/gclouduniverse/notebook_training.git",
    download_url="https://github.com/gclouduniverse/notebook_training/archive/0.0.12.tar.gz",
    packages=setuptools.find_packages(),
    install_requires=[
        'gcloud>=0.18.3',
        'oauth2client>=4.1.3',
        'google-api-python-client>=1.7.11',
        'importlib-metadata>=1.5.0',
        'google-api-core>=1.16.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points = {
        'console_scripts': ['gcloud-notebook-training=gcloud_notebook_training.app:main'],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)