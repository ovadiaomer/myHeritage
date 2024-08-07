import pytest
from src.pages.login_page import LoginPage

# Note, username \ password can either
# - Parametrize the test function to receive multiple sets of username and password or
# - Taken from conftest as fixture or
# - Directly from Credentials.USERNAME \ Credentials.USERNAME
@pytest.mark.parametrize("username, password", [
    ("john_doe@company.con", "123456")
])
def test_login_functionality(page, username, password):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(username, password)

    # Add a check to verify if login was successful
