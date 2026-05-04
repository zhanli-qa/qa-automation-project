from common.utils.validation import (validate_response_status_code, validate_response_is_dict,
                                     validate_key_is_exist)
from common.logger.logger import get_logger
import allure
import pytest

logger = get_logger()
pytestmark = pytest.mark.api

'''
Test login function
Verity if return token
'''
@allure.feature("Auth API")
@allure.story("Login")
def test_login(api_client):
    logger.info("Start test: test_login_with_token")

    response = api_client.login_response("mor_2314", "83r5^_")
    logger.info(f"Status Code: {response.status_code}")
    validate_response_status_code(response, 201)

    data = response.json()
    logger.info(f"Response JSON: {data}")

    validate_response_is_dict(data)
    validate_key_is_exist(data, "token")

