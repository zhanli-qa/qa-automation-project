import pytest
import json
from common.utils.validation import validate_response_status_code, validate_schema
from common.utils.validation import (validate_response_status_code, validate_schema, validate_response_is_json,
                                     validate_keys_exist, validate_response_is_dict)
from api.schemas.user.response.user_response_schema import user_response_schema
from common.logger.logger import get_logger

logger = get_logger()

'''
Verify delete a user successfully
Return 200 with Json format
'''
def test_delete_user(user_service):
    user_id = 10

    # 1, sent request
    response = user_service.delete_user(user_id)

    # 2, check the status code of response
    validate_response_status_code(response, 200)

    # 3, get the user which already delete to see if it's deleted from DB





