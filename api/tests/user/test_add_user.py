import pytest
import json
from common.utils.validation import validate_response_status_code
from common.logger.logger import get_logger

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

    # 2, check the status code of response
    logger.info(f"Status Code: {response.status_code}")
    validate_response_status_code(response, 201)

    # 3, decoded the content of return
    data = response.json()
    logger.info(f"Response JSON: {data}")

    # 4, assert the value
    assert "id" in data


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





















