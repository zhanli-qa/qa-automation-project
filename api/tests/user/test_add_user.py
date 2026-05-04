import allure
import pytest
import json
from common.utils.validation import validate_response_is_json
from common.logger.logger import get_logger
from common.utils.validation import validate_response_status_code, validate_schema, validate_key_is_exist
from api.schemas.user.request.create_user_request_schema import create_user_request_schema
from api.schemas.user.response.create_user_response_schema import create_user_response_schema
from common.utils.allure_helper import attach_response, attach_request, attach_status_code

logger = get_logger()

pytestmark = pytest.mark.api

'''
Verify a new user can be created successfully
'''

@allure.feature("User API")
@allure.story("Create user")
def test_add_a_new_user(user_service):

    with allure.step("Step 1: Read test data for request payload"):
        with open('test_data/api/user/add_new_user.json', 'r') as file:
            payload = json.load(file)

    with allure.step("Step 2: Send request"):
        response = user_service.create_user(payload)

    # attach request, response and status code to allure report for debugging purpose
    attach_request(payload)
    attach_response(response)
    attach_status_code(response)

    with allure.step("Step 3: Validate request schema"):
        validate_schema(payload, create_user_request_schema)

    with allure.step("Step 4: Validate status code"):
        validate_response_status_code(response, 201)

    with allure.step("Step 5: Validate response is JSON"):
        data = validate_response_is_json(response)

    with allure.step("Step 6: Validate response return id"):
        validate_key_is_exist(data, "id")

    with allure.step("Step 7: Validate response schema"):
        validate_schema(data, create_user_response_schema)


'''
Negative Test -- missing fields when add new user
Return 400 error code 
'''
@allure.feature("User API")
@allure.story("Create User - Negative Cases")
@pytest.mark.skip(reason="temporarily skip")
def test_add_user_missing_fields_return_400(auth_client):

    with allure.step("Step 1: Generate a request payload"):
        payload = {
        "username": "test user",
        "email": "test.user@gmail.com"
        }

    with allure.step("Step 2: Send request"):
        response = auth_client.post("/users", payload)

    # attach request, response and status code to allure report for debugging purpose
    attach_request(payload)
    attach_response(response)
    attach_status_code(response)

    with allure.step("Step 3: Validate status code"):
        validate_response_status_code(response, 400)


'''
Negative Test -- with invalid token
Return 401/403 error code 
'''
@allure.feature("User API")
@allure.story("Create User - Negative Cases")
@pytest.mark.skip(reason="temporarily skip")
def test_add_user_invalid_token(invalid_token_client):

    with allure.step("Step 1: Generate a request payload"):
        payload = {
            "username": "test user with invalid token",
            "email": "test.user1@gmail.com"
        }

    with allure.step("Step 2: Send request"):
        response = api_client.post("/users", payload)

    # attach response to allure report for debugging purpose
    attach_response(response)

    with allure.step("Step 3: Validate status code"):
        validate_response_status_code(response, 401)


'''
Negative Test -- create user without token
Return 401 error code 
'''
@allure.feature("User API")
@allure.story("Create User - Negative Cases")
@pytest.mark.skip(reason="temporarily skip")
def test_add_user_missing_token(api_client):

    with allure.step("Step 1: Generate a request payload"):
        payload = {
            "username": "test user without token",
            "email": "test.user2@gmail.com"
        }

    with allure.step("Step 2: Send request"):
        response = api_client.post("/users", payload)

    # attach response to allure report for debugging purpose
    attach_response(response)

    with allure.step("Step 3: Validate status code"):
        validate_response_status_code(response, 401)





















