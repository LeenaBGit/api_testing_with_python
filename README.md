#  API Testing with Python & Pytest

This project demonstrates how to test REST APIs using Python's `requests` library and the `pytest` framework. It covers **GET** and **POST** requests using publicly available endpoints.

---

##  Technologies Used

- **Python**
- **Pytest** — for writing and running test cases
- **Requests** — to send HTTP requests to the API

---

##  What’s Covered

| Test File | What It Tests |
|-----------|----------------|
| `test_get_users.py` | Validates a known user, handles user not found (404), checks email format |
| `test_post_users.py` | Sends JSON data to create a user (POST) and verifies the response |

These tests simulate **real QA scenarios** like:
- Positive & negative responses
- Email format checks using regex
- POST request with JSON payload

---

##  Project Structure

api_testing_with_python/
├── tests/
│ ├── test_get_users.py
│ └── test_post_users.py
├── requirements.txt
└── README.md

---

##  How to Run Tests

1.  Install dependencies:

pip install -r requirements.txt

2.  Run all tests:

pytest

3.  Run a specific test file (e.g. only POST tests):

pytest tests/test_post_users.py
