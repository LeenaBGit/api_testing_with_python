import requests
import re

# ✅ Test 1: User exists
def test_get_user():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()
    assert data["name"] == "Leanne Graham", f"Expected name to be Leanne Graham, got {data['name']}"
    assert data["email"] == "Sincere@april.biz", f"Expected email to be Sincere@april.biz, got {data['email']}"


# ✅ Test 2: Invalid user ID
def test_user_not_found():
    url = "https://jsonplaceholder.typicode.com/users/9999"
    response = requests.get(url)

    assert response.status_code == 404 or response.json() == {}, "Expected 404 or empty JSON for non-existent user"


# ✅ Test 3: Email format check
def test_user_email_format():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    email = response.json().get("email", "")

    pattern = r"[^@]+@[^@]+\.[^@]+"
    assert re.match(pattern, email), f"Email format invalid: {email}"
