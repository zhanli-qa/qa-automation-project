from jsonschema import validate, ValidationError

# validate response status code
def validate_response_status_code(response, expect_status_code=200):

    assert response.status_code == expect_status_code, \
        f"Expected {expect_status_code}, but got {response.status_code}. Response: {response.text}"

# validate response is json
def validate_response_is_json(response):
    try:
        return response.json()
    except ValidationError:
        raise AssertionError(f"Response is not valid JSON. Response text: {response.text}")

# validate response type
def validate_type(data, expected_type):

    assert isinstance(data, expected_type),  \
        f"Expected type {expected_type.__name__}, but got {type(data).__name__}. Data: {data}"

# validate response is list
def validate_response_is_list(data):

    assert isinstance(data, list), f"Expected list, but got {type(data)}"

# validate response is dict
def validate_response_is_dict(data):

    assert isinstance(data, dict), f"Expected dict, but got {type(data)}"


# validate a key exist
def validate_key_is_exist(data, key):

    assert key in data, f"Expected key '{key}' not found in response: {data}"


# validate multiple keys exist
def validate_keys_exist(data, keys):
    missing_keys = [key for key in keys if key not in data]
    assert not missing_keys, f"Missing keys: {missing_keys}. Data: {data}"


# validate multiple keys exist
def validat_list_not_empty(data):
    validate_response_is_list(data)
    assert len(data) > 0, f"Expected list not empty, but got empty list"


# validate schema
def validate_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as error:
        raise AssertionError(f"Schema validation failed: {error.message}")


# validate response time
def validate_response_time(response, max_time_seconds=2):
    assert response.elapsed.total_seconds() <= max_time_seconds, (
        f"Response time exceeded {max_time_seconds}s. "
        f"Actual: {response.elapsed.total_seconds()}s"
    )


