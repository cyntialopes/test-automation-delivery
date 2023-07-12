from ConfigTest import open_page
from pages.ManagerPage import ManagerPage
from pages.OpenAccountPage import OpenAccountPage
import time


class Test002:
    def test_open_account_page(self, open_page):
        home_page = open_page
        home_page.click_manager_btn()
        manager_page = ManagerPage(home_page.driver)
        manager_page.click_open_account()
        open_account = OpenAccountPage(home_page.driver)
        assert open_account.is_url_open_account(), 'Error Page'

        open_account.select_customer()
        selected_customer = open_account.select_customer_random()
        customer_name = open_account.get_selected_customer()
        assert selected_customer == customer_name, 'Invalid customer'

        open_account.select_currency()
        selected_currency = open_account.select_currency_random()
        currency = open_account.get_selected_currency()
        assert selected_currency == currency, 'Invalid currency'

        open_account.click_process()
        time.sleep(3)
        alert_text = open_account.click_alert()
        assert "Account created successfully with account Number :" \
               in alert_text, "Alert text does not match expectations"
