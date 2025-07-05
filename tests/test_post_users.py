import requests

def test_create_user():
    url = "https://jsonplaceholder.typicode.com/users"
    payload = {
        "name": "Leena QA",
        "username": "leena.qa",
        "email": "leena.qa@example.com"
    }

    response = requests.post(url, json=payload)

    # Check status code for created (should be 201 for real APIs, this one gives 201 or 200)
    assert response.status_code in [200, 201], f"Unexpected status code: {response.status_code}"

    # Check if data was returned
    data = response.json()
    assert data.get("name") == "Leena QA", "Name mismatch in response"
    assert data.get("email") == "leena.qa@example.com", "Email mismatch in response"
