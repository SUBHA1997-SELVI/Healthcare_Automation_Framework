from api.api_client import APIClient


def test_get_users_api():
    response = APIClient.get("/users")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert "username" in data[0]