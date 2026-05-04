import allure
import pytest
from common.utils.validation import (validate_response_status_code, validate_schema, validate_response_is_list,
                                     validate_response_is_dict, validate_key_is_exist, validate_response_is_json,
                                     validate_list_not_empty, validate_keys_exist)
from api.schemas.user.response.user_response_schema import user_response_schema
from api.schemas.user.response.user_list_response_schema import user_list_response_schema
from jsonschema.validators import validate
from common.logger.logger import get_logger
from common.utils.allure_helper import attach_response, attach_status_code

logger = get_logger()
pytestmark = pytest.mark.api

'''
Verify all users can be retrieved successfully
Return 200 with Json format, and validate user list schema
'''

@allure.feature("User API")
@allure.story("Get all users")
def test_get_all_users(user_service):

    with allure.step("Step 1: Send request"):
        response = user_service.get_all_users()

    # attach response and response code to allure report for debugging purpose
    attach_response(response)
    attach_status_code(response)

    with allure.step("Step 2: Validate status code"):
        validate_response_status_code(response)

    with allure.step("Step 3: Validate response is JSON"):
        data = validate_response_is_json(response)

    with allure.step("Step 4: Validate response schema"):
        validate_schema(data, user_list_response_schema)

    with allure.step("Step 5: Validate response is a list"):
        validate_response_is_list(data)

    with allure.step("Step 6: Validate response is not empty"):
        validate_list_not_empty(data)

    with allure.step("Step 7: Validate fields id and username in response"):
        validate_key_is_exist(data[0], "id")
        validate_key_is_exist(data[0], "username")


'''
Verify a single user can be retrieved successfully by user id
Return 200 with JSON format
'''
@allure.feature("User API")
@allure.story("Get user by ID")
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_multiple_users(user_service, user_id):

    with allure.step("Step 1: Send request"):
        response = user_service.get_user_by_id(user_id)

    # attach response and status_code to allure report for debugging purpose
    attach_response(response)
    attach_status_code(response)

    with allure.step("Step 2: Validate status code"):
        validate_response_status_code(response)

    with allure.step("Step 3: Validate response is JSON"):
        data = validate_response_is_json(response)

    with allure.step("Step 4: Validate response schema"):
        validate(data, user_response_schema)

    with allure.step("Step 5: Validate response is dict"):
        validate_response_is_dict(data)

    with allure.step("Step 6: Validate response has the fields id, username and email"):
        validate_keys_exist(data, ["id", "username", "email"])


'''
Negative Test -- user not exist
Return 404 error code 
'''
@allure.feature("User API")
@allure.story("Get User - Negative Cases")
@pytest.mark.skip(reason="temporarily skip")
def test_get_user_not_exit_return_404(user_service):

    with allure.step("Step 1: Send request"):
        response = user_service.get_user_by_id("999")

        # attach response to allure report for debugging purpose
        attach_response(response)

    with allure.step("Step 2: Validate status code"):
        validate_response_status_code(response, 404)

















