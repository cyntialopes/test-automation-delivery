from ConfigTest import open_page
from pages.AccountPage import AccountPage
from pages.SearchCustomerPage import SearchCustomerPage
from pages.TransactionsPage import TransactionsPage
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
        transactions = TransactionsPage(home_page.driver)
        assert transactions.is_url_transaction(), 'Error Page'
        assert transactions.is_customer_selected() == select_customer, 'Customer is not selected'

        deposit = AccountPage(home_page.driver)
        deposit.click_first_deposit_btn()
        deposit.enter_value_deposit()
        deposit.click_second_deposit_btn()
        transactions.select_withdraw_btn()
        time.sleep(1)  # Mandatory use for this test
        transactions.report_withdraw_amount()
        transactions.click_withdraw()
        assert transactions.withdraw_title() == 'Amount to be Withdrawn :'
        assert transactions.withdraw_msg() == 'Transaction successful'
