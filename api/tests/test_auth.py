from common.utils.validation import validate_response_status_code, validate_schema

# login / token / auth related test cases

'''
Test login function
Verity if token in the response
'''
def test_login(api_client):

    response = api_client.login("mor_2314", "83r5^_")

    validate_response_status_code(response, 200)

    data = response.json()

    assert "token" in data

