import pytest
import json
from common.utils.validation import (validate_response_status_code, validate_schema, validate_response_is_json,
                                     validate_keys_exist, validate_response_is_dict)
from api.schemas.user.request.update_user_request_schema import update_user_request_schema
from api.schemas.user.response.update_user_response_schema import update_user_response_schema
from common.logger.logger import get_logger

logger = get_logger()

'''
Verify update an existing user successfully
Return 200 with Json format
'''
def test_update_user(user_service):
    user_id = 1
    logger.info("Start test: update an existing user:")

    with open('test_data/api/user/update_exist_user.json', 'r') as file:
        payload = json.load(file)

    # validate request payload schema
    validate_schema(payload, update_user_request_schema)

    # 1, sent request
    response = user_service.update_user(payload, user_id)

    # 2, check the status code of response
    validate_response_status_code(response, 200)

    # 3, Validate response is JSON
    data = validate_response_is_json(response)

    # 4, assert the value
    validate_keys_exist(data, ["username", "email", "password"])
    validate_response_is_dict(data)

    # 5, assert the response schema
    validate_schema(data, update_user_response_schema)


'''
Negative Test -- update a non-exist user
Return 404 error code 
'''
@pytest.mark.skip(reason="temporarily skip")
def test_update_non_exit_user(user_service):

    user_id = 999

    with open('test_data/api/user/update_exist_user.json', 'r') as file:
        payload = json.load(file)

    # validate request payload schema
    validate_schema(payload, update_user_request_schema)

    # 1, sent request
    response = user_service.update_user(payload, user_id)

    validate_response_status_code(response, 404)


































