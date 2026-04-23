import pytest
from api.client.api_client import APIClient
from api.services.user_service import UserService


@pytest.fixture
def api_client():
    """
    Create a basic API client without authentication
    """
    return APIClient()


@pytest.fixture
def auth_client(api_client):
    """
    Create an authenticated API client
    """
    client = APIClient()
    token = client.login("mor_2314", "83r5^_")
    client.set_headers({"Authorization": f"Bearer {token}"})
    return client


@pytest.fixture
def user_service(auth_client):
    """
    User service with authenticated client
    """
    return UserService(auth_client)


@pytest.fixture
def invalid_token_client(api_client):
    """
    Create an API client with invalid token
    """
    client = APIClient()

    client.set_headers({
        "Authorization": "Bearer invalid_token"
    })
    return client



