import pytest
from common.utils.validation import validate_response_status_code, validate_schema
from api.schemas.user.user_schema import user_schema
from api.schemas.user.user_list_schema import user_list_schema
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

    data = response.json()
    logger.info(f"Response JSON: {data}")
    validate_schema(data, user_list_schema)

    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "username" in data[0]


'''
Verify a single user can be retrieved successfully by user id
Return 200 with JSON format
'''
@pytest.mark.parametrize("user_id", [1,2,3,4])
def test_get_multiple_users(user_service, user_id):
    logger.info("Start test: get single user:")

    response = user_service.get_user_by_id(user_id)

    logger.info(f"Status Code: {response.status_code}")
    validate_response_status_code(response)

    data = response.json()
    logger.info(f"Response JSON: {data}")
    validate(instance=data, schema=user_schema)

    assert len(data) > 0
    assert isinstance(data, dict)


'''
Negative Test -- user not exist
Return 404 error code 
'''
@pytest.mark.skip(reason="temporarily skip")
def test_get_user_not_exit_return_404(user_service):

    response = user_service.get_user_by_id("999")

    validate_response_status_code(response, 404)

















