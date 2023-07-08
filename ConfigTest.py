import pytest
from pages.HomePage import HomePage
@pytest.fixture()
def open_page():
    select_browser = "chrome"
    open_page = HomePage(browser=select_browser)
    yield open_page
    open_page.close()
