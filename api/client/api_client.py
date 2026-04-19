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

    """
    Initialize the API client with GET method.
    """
    def get(self, endpoint):

        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")

        response = requests.get(url, timeout=config.TIMEOUT)

        return response

    """
    Initialize the API client with POST method.
    """
    def post(self, endpoint, data):

        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url} | data={data}")

        response = requests.post(url, json=data, timeout=config.TIMEOUT)

        # equals to print(data), if use print, the cmd need to use -s
        # in order to present INFO log, the cmd command "pytest api/tests/test_user.py -o log_cli=true --log-cli-level=INFO"
        logger.info(f"Response data: {response.json()}")

        return response

    """
    Initialize the API client with PUT method.
    """
    def put(self, endpoint, data):

        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url} | data={data}")

        response = requests.put(url, json=data, timeout=config.TIMEOUT)

        return response


    """
    Initialize the API client with DELETE method.
    """
    def delete(self, endpoint):

        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")

        response = requests.delete(url, timeout=config.TIMEOUT)

        return response






