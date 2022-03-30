import urllib3
import json
from dotenv import load_dotenv
import os

http = urllib3.PoolManager()


class RequestToData:

    def __init__(self):
        pass

    @classmethod
    def configure(cls):
        load_dotenv()

    @classmethod
    def get_auth_token(cls) -> str:
        """
        get an auth token
        """
        # http = urllib3.PoolManager()
        url: str = os.getenv('bearer_token_endpoint')

        response = http.request('GET', url)

        return json.loads(response.data.decode("utf-8").replace("'", '"'))['token']

    @classmethod
    def get_response_json_object(cls, auth_token: str, ml_model_id: str, training_model_id: str):
        """
        returns json object with info
        """
        url_asd = os.getenv('request_endpoint') + f"MLModelId={ml_model_id}&MLTrainingModelId={training_model_id}"
        response = http.request(
            'GET',
            url_asd,
            headers={"Authorization": f"Bearer {auth_token}"}
        )

        return json.loads(response.data.decode("utf-8").replace("'", '"'))
