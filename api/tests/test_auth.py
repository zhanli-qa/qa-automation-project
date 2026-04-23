from common.utils.validation import validate_response_status_code
from common.logger.logger import get_logger

logger = get_logger()

# login / token / auth related test cases

'''
Test login function
Verity if token in the response
'''
def test_login(api_client):
    logger.info("Start test: test_login_with_token:")

    response = api_client.login("mor_2314", "83r5^_")
    logger.info(f"Status Code: {response.status_code}")

    validate_response_status_code(response, 201)

    data = response.json()
    logger.info(f"Response JSON: {data}")

    assert "token" in data

