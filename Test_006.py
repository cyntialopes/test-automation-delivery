from ConfigTest import open_page
from pages.SearchCustomerPage import SearchCustomerPage
from pages.AccountPage import AccountPage
import time


class Test006:
    def test_withdraw(self, open_page):
        home_page = open_page
        home_page.click_customer_btn()
        search_customer = SearchCustomerPage(home_page.driver)
        assert search_customer.is_url_search_customer(), 'Error Page'
        search_customer.select_customer()
        select_customer = search_customer.select_customer_random()
        search_customer.click_login_btn()
        withdraw = AccountPage(home_page.driver)
        assert withdraw.is_url_account(), 'Error Page'
        assert withdraw.is_customer_selected() == select_customer, 'Customer is not selected'

        deposit = AccountPage(home_page.driver)
        deposit.click_first_deposit_btn()
        deposit.enter_value_deposit()
        deposit.click_second_deposit_btn()
        withdraw.click_withdrawl_btn()
        time.sleep(1)  # Mandatory use for this test
        withdraw.report_withdraw_amount()
        withdraw.click_second_withdrawl_btn()
        assert withdraw.withdraw_title() == 'Amount to be Withdrawn :'
        assert withdraw.withdraw_msg() == 'Transaction successful'
