import pytest
from api.client.api_client import APIClient

@pytest.fixture
def api_client():

    return APIClient()


