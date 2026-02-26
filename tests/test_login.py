import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected_text",
    [
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
        ("wronguser", "wrongpass", "Your username is invalid!")
    ]
)
def test_login_data_driven(setup, username, password, expected_text):

    driver = setup
    login = LoginPage(driver)

    login.open_login_page()
    login.login(username, password)

    message = login.get_success_message()

    # 🔥 Temporary failure simulation
    assert expected_text in message