from ConfigTest import open_page
from pages.ManagerPage import ManagerPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Test003:
    def test_customers_page(self, open_page):
        home_page = open_page
        home_page.click_manager_btn()

        manager_page = ManagerPage(home_page.driver)
        manager_page.click_customers_btn()
        wait = WebDriverWait(manager_page.driver, 2)
        wait.until(EC.url_contains('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'))
        assert manager_page.is_url_manager_list(), 'Error Page'
        manager_page.fill_in_search_fields()
        assert 'Harry' == manager_page.is_customer_name()
