from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.SetupPage import SetupPage


class TransactionsReportPage(SetupPage):
    url_transaction = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'
    xpath_selector_back_btn = '/html/body/div/div/div[2]/div/div[1]/button[1]'
    class_transaction_table = 'table'

    def __init__(self, driver):
        super(TransactionsReportPage, self).__init__(driver=driver)
        self.driver.get(self.url_transaction)

    def is_url_transaction_list(self):
        return self.is_url(self.url_transaction)

    def is_table_displayed(self):
        try:
            table = self.driver.find_element(By.CLASS_NAME, self.class_transaction_table)
            return table.is_displayed()
        except NoSuchElementException:
            return False

    def click_back_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_selector_back_btn).click()
