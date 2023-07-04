import pytest
from pages.HomePage import HomePage


@pytest.fixture()
def open_login_page(request):
    select_browser = "chrome"
    login_page = HomePage(select_browser)
    yield login_page
    login_page.close()



