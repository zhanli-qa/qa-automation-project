import os

"""
config Environments:Dev & Staging
"""
class config:

    ENV = os.getenv("ENV", "dev")

    # API URLs
    API_BASE_URLS = {
        "dev": "https://fakestoreapi.com",
        "staging": "https://staging.fakestoreapi.com"
    }

    API_BASE_URLS = API_BASE_URLS[ENV]

    # UI URLs
    UI_BASE_URLS = {
        "dev": "https://www.saucedemo.com",
        "staging": "https://staging.saucedemo.com"
    }

    UI_BASE_URL = UI_BASE_URLS[ENV]

    TIMEOUT = 10
