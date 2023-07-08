from ConfigTest import open_page
import time
from pages.AddCustomerPage import AddCustomerPage
from pages.ManagerPage import ManagerPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        time.sleep(2)
        add_customer_page.click_register_customer_btn()

        WebDriverWait(home_page.driver, 10).until(EC.alert_is_present())
        alert = home_page.driver.switch_to.alert
        alert_text = alert.text
        time.sleep(5)
        assert "Customer added successfully with customer id :" in alert_text, "Alert text does not match expectations"
        alert.accept()

