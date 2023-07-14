from ConfigTest import open_page
from pages.SearchCustomerPage import SearchCustomerPage
from pages.AccountPage import AccountPage
from pages.TransactionsReportPage import TransactionsReportPage


class Test004:
    def test_view_transactions(self, open_page):
        home_page = open_page
        home_page.click_customer_btn()
        search_customer = SearchCustomerPage(home_page.driver)
        assert search_customer.is_url_search_customer(), 'Error Page'

        search_customer.select_customer()
        select_customer = search_customer.select_customer_random()
        customer_name = search_customer.get_selected_customer()
        assert select_customer == customer_name, 'Invalid Customer'

        search_customer.click_login_btn()
        transactions = AccountPage(home_page.driver)
        assert transactions.is_url_account(), 'Error Page'
        assert transactions.is_customer_selected() == customer_name, 'Customer is not selected'

        transactions.click_transaction_btn()
        transactions_list = TransactionsReportPage(home_page.driver)
        assert transactions_list.is_url_transaction_list(), 'Error Page'
        assert transactions_list.is_table_displayed(), 'Table not displayed'

        transactions_list.click_back_btn()
        assert transactions.is_url_account(), 'Error Page'
        assert transactions.is_customer_selected() == customer_name, 'Customer is not selected'
