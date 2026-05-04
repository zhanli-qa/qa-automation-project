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
        self.base_url = config.API_BASE_URL
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

        if not response.ok:
            logger.warning("Login failed")
            raise Exception(f"Login failed with status  code {response.status_code}")

        data = response.json()
        token = data.get("token")

        if not token:
            logger.warning("Login succeeded but no token found in response")
            raise Exception("Token not found in login response")

        logger.info("Login succeeded and token received")
        return token

    """
    Initialize the login itself 
    """
    def login_response(self, username, password):

        url = f"{self.base_url}/auth/login"

        payload = {
            "username": username,
            "password": password
        }

        response = requests.post(url, json=payload, timeout=config.TIMEOUT)

        return response


    """
    Initialize the API client with GET method.
    """
    def get(self, endpoint):

        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        logger.info(f"Headers: {self.headers}")

        response = requests.get(url, headers=self.headers, timeout=config.TIMEOUT)
        logger.info(f"Response Status: {response.status_code}")

        return response

    """
    Initialize the API client with POST method.
    """
    def post(self, endpoint, data):

        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url} | data={data}")
        logger.info(f"Headers: {self.headers}")

        response = requests.post(url, json=data, headers=self.headers, timeout=config.TIMEOUT)
        logger.info(f"Response Status: {response.status_code}")

        # equals to print(data), if use print, the cmd need to use -s
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
        logger.info(f"Headers: {self.headers}")

        response = requests.put(url, json=data, headers=self.headers, timeout=config.TIMEOUT)
        logger.info(f"Response Status: {response.status_code}")

        return response


    """
    Initialize the API client with DELETE method.
    """
    def delete(self, endpoint):

        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        logger.info(f"Headers: {self.headers}")

        response = requests.delete(url, headers=self.headers, timeout=config.TIMEOUT)
        logger.info(f"Response Status: {response.status_code}")

        return response






