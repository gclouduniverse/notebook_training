import json

def get_container_uri(notebook_path):
    with open(notebook_path, "r") as read_file:
        data = json.load(read_file)
    try:
        uri = data["metadata"]["environment"]["uri"]
    except KeyError:
        return None

    return uri;