import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get("/hello")
    assert response.status_code == 200
    data = response.json
    assert data == {'hello': "World"}

def test_get_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    data = response.json
    assert len(data) > 0

def test_get_product(client):
    response = client.get("/product/my-product-id")
    assert response.status_code == 200
    data = response.json
    assert data.get('title')

def test_update_product(client):
    product = {
        'price': 99.99,
        'units_sold': 100
    }
    response = client.put("/product/my-product-id", json=product)
    assert response.status_code == 200
    data = response.json
    assert data

def test_create_product(client):
    product = {
        'title': "my new product",
        'price': 99.99,
        'shipping_price': 7.99,
        'units_sold': 100,
        'rating': 4.9,
        'image_url': "https://imgur.com/gallery/YUJYQ",
        'store_name': "Viva Naturals"
    }
    response = client.post("/products", json=product)
    assert response.status_code == 201
    data = response.json
    assert data
