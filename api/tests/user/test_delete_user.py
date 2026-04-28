import allure
from common.utils.validation import validate_response_status_code
from common.utils.allure_helper import attach_response, attach_status_code
from common.logger.logger import get_logger

logger = get_logger()

'''
Verify delete a user successfully
Return 200 with Json format
'''
@allure.feature("User API")
@allure.story("Delete user")
def test_delete_user(user_service):

    user_id = 10

    with allure.step("Step 1: Send request"):
        response = user_service.delete_user(user_id)

    # attach response and status code to allure report for debugging purpose
    attach_response(response)
    attach_status_code(response)

    with allure.step("Step 2: Validate status code"):
        validate_response_status_code(response, 200)





