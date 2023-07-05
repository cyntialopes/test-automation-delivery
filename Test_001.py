from ConfigTest import open_page
import time


class Test001:
    def test_click_manager_btn(self, open_page):
        home_page = open_page
        time.sleep(3)
        assert home_page.is_url_login(), 'Error Page'
        home_page = open_page
        home_page.click_manager_btn()
        assert home_page
        home_page.click_add_customer()
        home_page.fill_reg_fields()
        home_page.click_second_add_customer_btn()
