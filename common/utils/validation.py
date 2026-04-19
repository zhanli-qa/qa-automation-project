from jsonschema import validate

def validate_response_status_code(response, expect_status_code=200):

    assert response.status_code == expect_status_code, \
        f"Expected {expect_status_code}, but got {response.status_code}. Response: {response.text}"


def validate_schema(data, schema):

    validate(instance=data, schema=schema)