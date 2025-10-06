import pytest
import requests
import random


@pytest.fixture(scope="session")
def base_url():
    return "https://my-json-server.typicode.com/omoskovko/fake_api/"


@pytest.fixture
def endpoints(request, base_url):
    cfg = request.param
    return {
        "name": cfg["name"],
        "url": f"{base_url}{cfg['name']}",
        "params": cfg.get("params", {}),
    }


@pytest.fixture
def post_template():
    names = ["Alece", "Jon", "Bob", "Charlie"]
    seccond_names = ["Johnson", "Smith", "Brown"]
    user_name = f"{random.choice(names)} {random.choice(seccond_names)}"
    user_email = f"{random.choice(names)}.{random.choice(seccond_names)}@example.com"

    products = {
        "Electronics": "Mechanical Keyboard",
        "Audio": "Noise Cancelling Headphones",
        "Furniture": "Ergonomic Chair",
    }
    cproduct = random.choice(list(products))
    template_dict = {
        "users": {
            "name": user_name,
            "email": user_email,
            "role": random.choice(["admin", "user"]),
            "isActive": random.choice(["true", "false"]),
        },
        "products": {
            "name": products[cproduct],
            "category": cproduct,
            "price": random.choice(["120.99", "33.02", "321.99"]),
            "inStock": random.choice(["true", "false"]),
        },
    }
    return template_dict


@pytest.fixture(scope="session")
def all_db(base_url):
    resp = requests.get(f"{base_url}db")
    assert resp.ok
    return resp.json()


@pytest.fixture
def dataset(request):
    return request.param
