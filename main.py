from request_to_data import *

if __name__ == '__main__':
    RequestToData.configure()
    token = RequestToData.get_auth_token()
    data = RequestToData.get_response_json_object(auth_token=token, ml_model_id='acc149d7-e60d-4be9-81e7-9799aac208da',
                                                  training_model_id='49e21268-198c-47c8-99b9-82577fc83834')
