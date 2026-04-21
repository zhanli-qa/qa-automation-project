import os

"""
config Environments:Dev & Staging
"""
class config:

    ENV = os.getenv("ENV", "dev")

    Base_URLS = {
        "dev": "https://fakestoreapi.com",
        "staging": "https://staging.fakestoreapi.com"
    }

    Base_URL = Base_URLS[ENV]

    TIMEOUT = 10
