import pytest
from pages.HomePage import HomePage


@pytest.fixture()
def setup_browser():
    home_page = HomePage()
    yield home_page
    home_page.close()
