import argparse

def parse_args():
  parser = argparse.ArgumentParser(
        description="Get notebook training args")

  parser.add_argument("--input-notebook", required=True)
  parser.add_argument("--project-id", required=False)
  parser.add_argument("--output-notebook", required=False)
  parser.add_argument("--job-id", required=False)
  parser.add_argument("--region", required=False)
  parser.add_argument("--scale-tier", required=False)
  parser.add_argument("--master-type", required=False)
  parser.add_argument("--bucket-name", required=False)
  parser.add_argument("--max-running-time", required=False)
  parser.add_argument("--container-uri", required=False)
  parser.add_argument("--accelerator-type", required=False)
  parser.add_argument("--service-account", required=False)
  parser.add_argument("--input-folder", required=False)

  args = parser.parse_args()
  return args