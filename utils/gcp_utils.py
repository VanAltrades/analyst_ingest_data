import os
# import json
from google.cloud import bigquery
from google.oauth2 import service_account


def get_gcp_credentials_path():
    config_dir = os.path.join(os.path.dirname(__file__), "../config")
    json_path = os.path.join(config_dir, "gcp_service_account.json")

    # with open(json_path, "r") as json_file:
    #     credentials = json.load(json_file)

    return json_path

def return_client(key_path : str):
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )

    return bigquery.Client(credentials=credentials, project=credentials.project_id,)

key_path = get_gcp_credentials_path()
client = return_client(key_path)