import pytest
import json
from common.utils.validation import validate_response_is_json
from common.logger.logger import get_logger
from common.utils.validation import validate_response_status_code, validate_schema, validate_key_is_exist
from api.schemas.user.request.create_user_request_schema import create_user_request_schema
from api.schemas.user.response.create_user_response_schema import create_user_response_schema

logger = get_logger()

'''
Verify a new user can be created successfully
'''
def test_add_a_new_user(user_service):
    logger.info("Start test: create a user:")

    with open('test_data/api/user/add_new_user.json', 'r') as file:
        payload = json.load(file)

    # 1, sent request
    response = user_service.create_user(payload)
    # validate request payload schema
    validate_schema(payload, create_user_request_schema)

    # 2, check the status code of response
    logger.info(f"Status Code: {response.status_code}")
    validate_response_status_code(response, 201)

    # 3, Validate response is JSON
    data = validate_response_is_json(response)
    logger.info(f"Response JSON: {data}")

    # 4, assert the value
    validate_key_is_exist(data, "id")

    # 5, assert the response schema
    validate_schema(data, create_user_response_schema)


'''
Negative Test -- missing fields when add new user
Return 400 error code 
'''
@pytest.mark.skip(reason="temporarily skip")
def test_add_user_missing_fields_return_400(auth_client):

    payload = {
        "username": "test user",
        "email": "test.user@gmail.com"
    }

    response = api_client.post("/users", payload)

    validate_response_status_code(response, 400)


'''
Negative Test -- with invalid token
Return 401/403 error code 
'''
@pytest.mark.skip(reason="temporarily skip")
def test_add_user_missing_token(invalid_token_client):

    payload = {
        "username": "test user with invalid token",
        "email": "test.user1@gmail.com"
    }

    response = api_client.post("/users", payload)

    validate_response_status_code(response, 401)


'''
Negative Test -- create user without token
Return 401 error code 
'''
@pytest.mark.skip(reason="temporarily skip")
def test_add_user_missing_token(api_client):

    payload = {
        "username": "test user without token",
        "email": "test.user2@gmail.com"
    }

    response = api_client.post("/users", payload)

    validate_response_status_code(response, 401)





















