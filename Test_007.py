import time
from ConfigTest import open_page
from pages.AccountPage import AccountPage
from pages.CustomerPage import CustomerPage

class Test007:
    def test_account_page_deposit(self, open_page):
        home_page = open_page
        home_page.click_customer_btn()

        customer_page = CustomerPage(home_page.driver)
        assert customer_page.is_url_customers(), 'Error Page'
        customer_page.click_your_name()
        customer_page.select_dropdown_value('1')
        customer_page.click_login_btn()

        account_page = AccountPage(home_page.driver)
        assert account_page.is_url_account(), 'Error Page'
        account_page.click_withdrawl_btn()
        account_page.enter_value_withdrawl()
        account_page.click_second_withdrawl_btn()
        time.sleep(2)
        assert account_page.withdrawl_failed_mgs(), 'Message is different than expected'
        time.sleep(1)