from ConfigTest import open_page
import time
from pages.AddCustomerPage import AddCustomerPage
from pages.ManagerPage import ManagerPage


class Test001:
    def test_manager_page(self, open_page):
        home_page = open_page
        assert home_page.is_url_login(), 'Error Page'

        home_page.click_manager_btn()
        manager_page = ManagerPage(home_page.driver)
        assert manager_page.is_url_manager(), 'Error Page'

        manager_page.click_add_customer()
        add_customer_page = AddCustomerPage(home_page.driver)
        add_customer_page.fill_reg_fields()
        add_customer_page.click_register_customer_btn()

        alert_text = manager_page.click_alert(open_page)
        assert "Customer added successfully with customer id :" \
               in alert_text, "Alert text does not match expectations"
