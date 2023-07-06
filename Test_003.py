from ConfigTest import open_page
import time


class Test003:
    def test_click_customers_btn(self, open_page):
        home_page = open_page
        time.sleep(3)
        assert home_page.is_url_login(), 'Error Page'
        home_page = open_page
        home_page.click_manager_btn()
        time.sleep(2)
        home_page.click_customers_btn()
        assert home_page.is_url_customers(), 'Error Page'
        time.sleep(2)
        home_page.fill_in_search_fields()
        time.sleep(3)
