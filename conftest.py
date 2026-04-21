import pytest
from api.client.api_client import APIClient

# api_client without Token
@pytest.fixture
def api_client():

    return APIClient()


# api_client with Token
@pytest.fixture
def auth_client(api_client):
    api_client.login("mor_2314", "83r5^_")

    return api_client


# api_client with invalid Token
@pytest.fixture
def invalid_token_client(api_client):
    api_client.set_headers({
        "Authorization": "Bearer invalid_token"
    })
    return api_client


