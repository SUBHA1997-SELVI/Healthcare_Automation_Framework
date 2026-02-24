import csv
import pytest
from pages.login_page import LoginPage


def get_login_data():
    data = []
    with open("testdata/login_data.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append((row["username"], row["password"], row["expected_message"]))
    return data


@pytest.mark.parametrize("username,password,expected_message", get_login_data())
def test_login_data_driven(setup, username, password, expected_message):
    driver = setup
    login = LoginPage(driver)

    login.open_url()
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    assert expected_message in login.get_success_message()