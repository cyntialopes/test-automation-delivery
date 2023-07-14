from selenium.webdriver.common.by import By
from pages.SetupPage import SetupPage


class TransactionsPage(SetupPage):
    url_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    class_transaction_btn = 'btn-lg'
    class_customer_selected = 'fontBig'
    xpath_withdraw_option_btn = '/html/body/div/div/div[2]/div/div[3]/button[3]'
    xpath_withdraw_confirm = '/html/body/div/div/div[2]/div/div[4]/div/form/button'
    xpath_value_field = '/html/body/div/div/div[2]/div/div[4]/div/form/div/input'
    xpath_withdraw_title = '/html/body/div[1]/div/div[2]/div/div[4]/div/form/div/label'
    xpath_withdraw_msg = '/html/body/div[1]/div/div[2]/div/div[4]/div/span'

    def __init__(self, driver):
        super(TransactionsPage, self).__init__(driver=driver)
        self.driver.get(self.url_account)

    def is_url_transaction(self):
        return self.is_url(self.url_account)

    def click_transaction_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.class_transaction_btn).click()

    def is_customer_selected(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_customer_selected).text

    def select_withdraw_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_withdraw_option_btn).click()

    def report_withdraw_amount(self, value=5):
        self.driver.find_element(By.XPATH, self.xpath_value_field).send_keys(value)

    def click_withdraw(self):
        self.driver.find_element(By.XPATH, self.xpath_withdraw_confirm).click()

    def withdraw_title(self):
        return self.driver.find_element(By.XPATH, self.xpath_withdraw_title).text

    def withdraw_msg(self):
        return self.driver.find_element(By.XPATH, self.xpath_withdraw_msg).text
