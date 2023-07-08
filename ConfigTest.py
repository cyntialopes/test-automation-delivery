import pytest
from pages.HomePage import HomePage
@pytest.fixture()
def open_page():
    select_browser = "chrome"
    login_page = HomePage(browser=select_browser)
    yield login_page
    login_page.close()
