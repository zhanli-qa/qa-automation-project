import pytest

'''
Test get all carts
Return 200 with Json format, the value of Json including id and products
'''

def test_get_all_cars(api_client):

    response = api_client.get("/carts")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    assert len(data) > 0

    first_cart = data[0]

    assert "id" in first_cart

    assert "products" in first_cart


'''
Test get one single cart
Return 200 with Json format, the value of Json including id and product
'''

@pytest.mark.parametrize("cart_id", [1,2,3])
def test_get_one_cart(api_client, cart_id):

    response = api_client.get(f"/carts/{cart_id}")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)

    assert len(data) > 0

    assert data["id"] == cart_id


