import allure
import pytest
import json
from common.utils.validation import (validate_response_status_code, validate_schema, validate_response_is_json,
                                     validate_keys_exist, validate_response_is_dict)
from api.schemas.user.request.update_user_request_schema import update_user_request_schema
from api.schemas.user.response.update_user_response_schema import update_user_response_schema
from common.logger.logger import get_logger
from common.utils.allure_helper import attach_response, attach_request, attach_status_code

logger = get_logger()

'''
Verify update an existing user successfully
Return 200 with Json format
'''
@allure.feature("User API")
@allure.story("Update user")
def test_update_user(user_service):

    with allure.step("Step 1: Read test data for request payload"):
        user_id = 1
        with open('test_data/api/user/update_exist_user.json', 'r') as file:
            payload = json.load(file)

    with allure.step("Step 2: Validate request schema"):
        validate_schema(payload, update_user_request_schema)

    with allure.step("Step 3: Send request"):
        response = user_service.update_user(payload, user_id)

    # attach request, response and status code to allure report for debugging purpose
    attach_request(payload)
    attach_response(response)
    attach_status_code(response)

    with allure.step("Step 4: Validate status code"):
        validate_response_status_code(response, 200)

    with allure.step("Step 5: Validate response is JSON"):
        data = validate_response_is_json(response)

    with allure.step("Step 6: Validate response fields and dict"):
        validate_keys_exist(data, ["username", "email", "password"])
        validate_response_is_dict(data)

    with allure.step("Step 7: Validate response schema"):
        validate_schema(data, update_user_response_schema)


'''
Negative Test -- update a non-exist user
Return 404 error code 
'''
@allure.feature("User API")
@allure.story("Update User - Negative Cases")
@pytest.mark.skip(reason="temporarily skip")
def test_update_non_exit_user(user_service):

    with allure.step("Step 1: Read test data to generate request payload"):
        user_id = 999
        with open('test_data/api/user/update_exist_user.json', 'r') as file:
            payload = json.load(file)

    with allure.step("Step 2: Validate request schema"):
        validate_schema(payload, update_user_request_schema)

    with allure.step("Step 3: Send request"):
        response = user_service.update_user(payload, user_id)

    # attach response to allure report for debugging purpose
    attach_response(response)

    with allure.step("Validate status code"):
        validate_response_status_code(response, 404)


































