# Cloud AI Notebook Training

This package allows to run a Jupyter notebook at Google Cloud AI Platform Training Jobs.

Install tool with pip by using `pip install gcloud-notebook-training`

## Syntax

```
gcloud-notebook-training [-h] --input-notebook INPUT_NOTEBOOK
              [--project-id PROJECT_ID]
              [--output-notebook OUTPUT_NOTEBOOK]
              [--job-id JOB_ID]
              [--region REGION]
              [--worker-machine-type WORKER_MACHINE_TYPE]
              [--bucket-name BUCKET_NAME]
              [--max-running-time MAX_RUNNING_TIME]
              [--container-uri CONTAINER_URI]
              [--accelerator-type ACCELERATOR_TYPE]
              [--service-account SERVICE_ACCOUNT]
```

The only required parameter is --input-notebook.

This parameter accepts local path or GCS path.

For example:
```
gcloud-notebook-training --input-notebook /local/path/to/notebook.ipynb
```

or
```
gcloud-notebook-training --input-notebook gs://bucket_name/notebook.ipynb
```

The output-notebook path can be specified explicitely.
Same as the input-notebook, this parameter accepts local path or GCS path.

If the output-notebook is not specified, it will be implied as input-notebook plus 'output' suffix.

If output-notebook is a GCS path, then the tool will only submit the training job and exit.
If output-notebook is a local path, then the tool will wait until the training job succeeds, and then will download the output notebook.

container-uri parameter specifies the container used by training job.
If this parameter is not specified, the tool will try to pull this information from the notebook metadata.
