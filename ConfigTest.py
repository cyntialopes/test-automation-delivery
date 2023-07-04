import pytest
from pages.HomePage import HomePage


@pytest.fixture()
def setup():
    home_page = HomePage()
    yield home_page
    home_page.close()
