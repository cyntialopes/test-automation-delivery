from ConfigTest import open_page
import time
from pages.ManagerPage import ManagerPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test001:
    def test_manager_page(self, open_page):
        home_page = open_page
        assert home_page.is_url_login(), 'Error Page'

        home_page.click_manager_btn()
        assert ManagerPage.is_url_manager, 'Error Page'

        home_page.ManagerPage.click_add_customer()
        home_page.AddCustomerPage.fill_reg_fields()
        home_page.AddCustomerPage.click_register_customer_btn()

        WebDriverWait(home_page.driver, 10).until(EC.alert_is_present())
        alert = home_page.driver.switch_to.alert
        alert_text = alert.text
        time.sleep(5)
        assert "Customer added successfully with customer id :" in alert_text, "Alert text does not match expectations"
        alert.accept()

