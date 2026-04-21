import requests
from common.config.config import config
from common.logger.logger import get_logger

logger = get_logger()


class APIClient:

    """
    Initialize the API client with the base URL from configuration.

    This ensures all API requests use a centralized and configurable
    base URL, making it easier to switch between environments
    (e.g., dev, staging, production).
    """
    def __init__(self):
        self.base_url = config.Base_URL
        self.headers = {"Content-Type": "application/json"}

    """
    Initialize the API client Headers.
    """
    def set_headers(self, headers: dict):
        self.headers.update(headers)

    """
    Create the Function: Auth Login and get Token
    Set header as "Authorization: Bearer {token}“
    """
    def login(self, username, password):
        url = f"{self.base_url}/auth/login"

        payload = {
            "username": username,
            "password": password
        }

        logger.info(f"POST {url} | login request for user={username}")

        response = requests.post(url, json=payload, timeout=config.TIMEOUT)

        logger.info(f"Login response status: {response.status_code}")

        if response.ok:
            token = response.json().get("token")
            if token:
                self.set_headers({"Authorization": f"Bearer {token}"})
                logger.warning("Login succeeded but no token found in response")
                logger.info(f"Current headers after login: {self.headers}")
            else:
                logger.warning("Login failed, Authorization header not set")

        return response

    """
    Initialize the API client with GET method.
    """
    def get(self, endpoint):

        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")

        response = requests.get(url, headers=self.headers, timeout=config.TIMEOUT)

        return response

    """
    Initialize the API client with POST method.
    """
    def post(self, endpoint, data):

        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url} | data={data}")

        response = requests.post(url, json=data, headers=self.headers, timeout=config.TIMEOUT)

        # equals to print(data), if use print, the cmd need to use -s
        # in order to present INFO log, the cmd command "pytest api/tests/test_user.py -o log_cli=true --log-cli-level=INFO"
        try:
            logger.info(f"Response data: {response.json()}")
        except Exception:
            logger.info(f"Response text: {response.text}")

        return response

    """
    Initialize the API client with PUT method.
    """
    def put(self, endpoint, data):

        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url} | data={data}")

        response = requests.put(url, json=data, headers=self.headers, timeout=config.TIMEOUT)

        return response


    """
    Initialize the API client with DELETE method.
    """
    def delete(self, endpoint):

        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")

        response = requests.delete(url, headers=self.headers, timeout=config.TIMEOUT)

        return response






