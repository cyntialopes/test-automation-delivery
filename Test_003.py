from ConfigTest import open_page
from pages.ManagerPage import ManagerPage
from pages.CustomerPage import CustomerPage


class Test003:
    def test_click_customers_btn(self, open_page):
        home_page = open_page
        assert home_page.is_url_login(), 'Error Page'

        home_page.click_manager_btn()
        manager_page = ManagerPage(home_page.driver)
        assert manager_page.is_url_manager(), 'Error Page'

        customer_page = CustomerPage(home_page.driver)
        customer_page.click_customers_btn()
        assert customer_page.is_url_customers(), 'Error Page'
        customer_page.fill_in_search_fields()
