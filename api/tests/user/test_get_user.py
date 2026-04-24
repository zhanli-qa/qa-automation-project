import pytest
from common.utils.validation import (validate_response_status_code, validate_schema, validate_response_is_list,
                                     validate_response_is_dict, validate_key_is_exist, validate_response_is_json,
                                     validat_list_not_empty, validate_keys_exist)
from api.schemas.user.response.user_response_schema import user_response_schema
from api.schemas.user.response.user_list_response_schema import user_list_response_schema
from jsonschema.validators import validate
from common.logger.logger import get_logger

logger = get_logger()

'''
Verify all users can be retrieved successfully
Return 200 with Json format, and validate user list schema
'''
def test_get_all_users(user_service):
    logger.info("Start test: get all users:")

    response = user_service.get_all_users()

    logger.info(f"Status Code: {response.status_code}")

    validate_response_status_code(response)
    data = validate_response_is_json(response)
    logger.info(f"Response JSON: {data}")

    validate_schema(data, user_list_response_schema)
    validate_response_is_list(data)
    validat_list_not_empty(data)
    validate_key_is_exist(data[0], "id")
    validate_key_is_exist(data[0], "username")


'''
Verify a single user can be retrieved successfully by user id
Return 200 with JSON format
'''
@pytest.mark.parametrize("user_id", [1,2,3])
def test_get_multiple_users(user_service, user_id):
    logger.info("Start test: get single user:")

    response = user_service.get_user_by_id(user_id)

    logger.info(f"Status Code: {response.status_code}")
    validate_response_status_code(response)

    data = validate_response_is_json(response)
    logger.info(f"Response JSON: {data}")
    validate(data, user_response_schema)

    validate_response_is_dict(data)
    validate_keys_exist(data, ["id", "username", "email"])


'''
Negative Test -- user not exist
Return 404 error code 
'''
@pytest.mark.skip(reason="temporarily skip")
def test_get_user_not_exit_return_404(user_service):

    response = user_service.get_user_by_id("999")

    validate_response_status_code(response, 404)

















