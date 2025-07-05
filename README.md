# API Testing with Python & Pytest

This project demonstrates API testing using Python's `requests` library and the `pytest` framework. It targets a public placeholder API to validate both positive and negative scenarios.

---

## Technologies Used

- **Python**
- **Pytest** — for test execution and structure
- **Requests** — to make HTTP calls

---

## What It Tests

| Test | Description |
|------|-------------|
| `test_get_user` | Checks if a valid user is returned correctly |
| `test_user_not_found` | Ensures proper handling of a non-existent user |
| `test_user_email_format` | Validates the email format using regex |

---

## Project Structure

api_testing_with_python/
├── tests/
│ └── test_users.py
├── requirements.txt
└── README.md


---

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt

2. Run tests with:

```bash
pytest
