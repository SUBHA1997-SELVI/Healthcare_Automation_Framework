import csv
import pytest
from pages.login_page import LoginPage
from api.api_client import APIClient


def get_login_data():
    data = []
    with open("testdata/login_data.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(
                (
                    row["username"],
                    row["password"],
                    row["expected_message"]
                )
            )
    return data


@pytest.mark.parametrize(
    "username,password,expected_message",
    get_login_data()
)
def test_login_data_driven(setup, username, password, expected_message):

    driver = setup
    login = LoginPage(driver)

    # 🔹 UI Steps
    login.open_url()
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    ui_message = login.get_success_message()

    # 🔹 UI Validation
    assert expected_message in ui_message

    # 🔥 Backend API Validation (Only for valid login case)
    if "secure area" in expected_message:
        response = APIClient.get("/users")

        assert response.status_code == 200

        api_data = response.json()

        assert isinstance(api_data, list)
        assert len(api_data) > 0