import time
from ConfigTest import open_page
from pages.CustomerPage import CustomerPage
from pages.ManagerPage import ManagerPage


class Test003:
    def test_customers_page(self, open_page):
        home_page = open_page
        home_page.click_manager_btn()

        manager_page = ManagerPage(home_page.driver)
        manager_page.click_customers_btn()
        time.sleep(1)
        assert manager_page.is_url_manager_list(), 'Error Page'
        manager_page.fill_in_search_fields()
        time.sleep(1)



