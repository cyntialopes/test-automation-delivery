import pytest
from pages.HomePage import HomePage
# from pages.ManagerPage import ManagerPage


@pytest.fixture()
def open_page():
    select_browser = "chrome"
    login_page = HomePage(browser=select_browser)
    yield login_page
    login_page.close()


# @pytest.fixture()
# def menu_manager(open_page):
    # manager_page = ManagerPage(driver=open_page.driver)
