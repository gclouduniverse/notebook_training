from google.api_core import retry

from .job_still_running_exception import JobStillRunningException
from . import constants

import time

def wait_predicate(ex):
  return retry.if_transient_error(ex) or retry.if_exception_type(JobStillRunningException)

class CaipJobExecutor:
  def __init__(self, jobs, project_id, job_id):
    self.__jobs = jobs
    self.__project_id = project_id
    self.__job_id = job_id

  @retry.Retry(predicate = retry.if_transient_error)
  def __execute_request(self, request):
    return request.execute()

  @retry.Retry(predicate = wait_predicate, deadline = constants.DEFAULT_JOB_MAX_RUNNING_TIME_IN_SECONDS)
  def __wait_for_job_completion(self, request):
    response = request.execute()

    if response["state"] in constants.TRAINING_JOB_STATES_TO_WAIT:
      print('.', end ='', flush=True)
      raise JobStillRunningException()
    return constants.TRAINING_JOB_STATES_SUCCEEDED == response["state"]

  def submit_training_job(self, image_uri, region, input_notebook_uri,
                          output_notebook_uri, accelerator_type,
                          max_run_time, service_account):
      # Prepare the CAIP training payload
      training_inputs = {
          'scaleTier': 'CUSTOM',
          'masterType': 'complex_model_m',
          'workerType': 'complex_model_m',
          'masterConfig': {
            "imageUri": image_uri
          },
          'parameterServerType': 'large_model',
          'workerCount': 1,
          'region': region,
          'pythonVersion': '3.7',
          'scheduling': {'maxRunningTime': '{}s'.format(max_run_time)},
          "args": [
            "nbexecutor",
            "--input-notebook", input_notebook_uri,
            "--output-notebook", output_notebook_uri
          ],
      }

      if not accelerator_type is None:
        training_inputs['masterConfig']['acceleratorConfig'] = {
            "count": 1,
            "type": accelerator_type
          }

      if not service_account is None:
        training_inputs['serviceAccount'] = service_account

      job_spec = {'jobId': self.__job_id, 'trainingInput': training_inputs}

      # Build CAIP training request
      request = self.__jobs.create(body=job_spec,
              parent='projects/{}'.format(self.__project_id))

      self.__execute_request(request)

  def wait_for_job_completion(self):
      self.__wait_for_training_start()

      get_request = self.__jobs.get(name=self.__get_job_name())
      return self.__wait_for_job_completion(get_request)

  def __get_job_name(self):
      return "projects/{}/jobs/{}".format(self.__project_id, self.__job_id)

  # It takes a constant time for a job to start. Let's wait for it.
  def __wait_for_training_start(self):
      print('.', end ='', flush=True)
      time.sleep(constants.TRAINING_JOB_PREPARATION_TIME_IN_SECONDS / 2)