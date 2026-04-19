import pytest
import json
from common.utils.validation import validate_response_status_code, validate_schema
from api.schemas.user.user_schema import user_schema
from api.schemas.user.user_list_schema import user_list_schema

'''
Test get all users
Return 200 with Json format, the value of Json including id and username
'''

def test_get_all_users(api_client):

    response = api_client.get("/users")

    validate_response_status_code(response)

    data = response.json()

    validate_schema(data, user_list_schema)

    assert len(data) > 0


'''
Test get multiple single users
Return 200 with Json format
'''

@pytest.mark.parametrize("user_id", [1,2,3,4])
def test_get_multiple_users(api_client, user_id):

    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200

    validate_response_status_code(response)

    data = response.json()
    print(type(data))   # data type is dict

    validate(instance=data, schema=user_schema)

    assert len(data) > 0


'''
Test add a new user
Return 201 with id
'''
def test_add_a_new_user(api_client):
    with open('test_data/api/user.json', 'r') as file:
        payload = json.load(file)

    # 1, sent request
    response = api_client.post("/users", payload)

    # 2, check the status code of response
    validate_response_status_code(response, 201)

    # 3, decoded the content of return
    data = response.json()

    # 4, assert the value
    assert "id" in data


'''
Negative Test -- user not exist
Return 404 error code 
'''
def test_get_user_not_exit_return_404(api_client):

    response = api_client.get(f"/users/999")

    validate_response_status_code(response, 404)

'''
Negative Test -- missing fields when add new user
Return 400 error code 
'''

def test_add_user_missing_fields_return_400(api_client):

    payload = {
        "username": "test user",
        "email": "test.user@gmail.com"
    }

    response = api_client.post("/users", payload)

    validate_response_status_code(response, 400)

























