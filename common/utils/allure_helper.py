import allure
import json


# attach response to the allure report
def attach_response(response):
    try:
        body = response.json()
        attachment_type = allure.attachment_type.JSON
        content = json.dumps(body, indent=2)
    except ValueError:
        attachment_type = allure.attachment_type.TEXT
        content = response.text

    allure.attach(
        content,
        name="response",
        attachment_type=attachment_type
    )

# attach request to the allure report
def attach_request(payload):
    try:
        content = json.dumps(payload, indent=2)
        attachment_type = allure.attachment_type.JSON
    except TypeError:
        content = str(payload)
        attachment_type = allure.attachment_type.TEXT
    allure.attach(
        content,
        name="request",
        attachment_type=attachment_type
    )

# attach status code to the allure report
def attach_status_code(response):
    allure.attach(
        str(response.status_code),
        name="status_code",
        attachment_type=allure.attachment_type.TEXT
    )


def attach_screenshot(page_obj, name="screenshot"):
    """
    Attach current page URL to Allure report.
    """
    screenshot = page_obj.screenshot()

    allure.attach(
        screenshot,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )


def attach_current_url(page_obj, name="current_url"):
    """
    Attach current page screenshot to Allure report.
    """
    allure.attach(
        page_obj.page.url,
        name=name,
        attachment_type=allure.attachment_type.TEXT
    )
