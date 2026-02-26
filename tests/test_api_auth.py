from api.api_client import APIClient


def generate_fake_token():
    # Simulating token generation
    return "fake_secure_token_123"


def test_secured_api_call():
    token = generate_fake_token()

    response = APIClient.get_with_token("/users", token)

    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0