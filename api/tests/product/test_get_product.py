import pytest
import json
from common.utils.validation import validate_response_status_code
'''
Test get all products
Return 200 with Json format, the value of Json including id and price
'''


def test_get_all_products(api_client):

    response = api_client.get("/products")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    assert len(data) > 0

    first_product = data[0]

    assert "price" in first_product

    assert "id" in first_product


'''
Test get multiple single product
Return 200 with Json format, the value of Json including price
'''

@pytest.mark.parametrize("product_id", [1,2,3,4])
def test_get_multiple_price(api_client, product_id):

    response = api_client.get(f"/products/{product_id}")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)

    assert len(data) > 0

    assert data["id"] == product_id


'''
Test post a new product
Return 201 with id
'''
def test_add_new_product(api_client):

    with open('test_data/api/product.json', 'r') as file:
        payload = json.load(file)

    response = api_client.post("/products", payload)

    validate_response_status_code(response, 201)

    data = response.json()

    assert "id" in data



