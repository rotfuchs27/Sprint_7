import random
import pytest
import string


@pytest.fixture
def generate_random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(10))

@pytest.fixture
def existing_user_payload():
    return {
        "login": "user",
        "password": "password",
        "firstName": "name"
    }