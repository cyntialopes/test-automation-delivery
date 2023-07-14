from selenium.webdriver.common.by import By
from pages.SetupPage import SetupPage


class AccountPage(SetupPage):
    url_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    xpath_first_deposit_btn = '/html/body/div/div/div[2]/div/div[3]/button[2]'
    xpath_amount_deposit = '/html/body/div/div/div[2]/div/div[4]/div/form/div/input'
    xpath_second_deposit_btn = '/html/body/div/div/div[2]/div/div[4]/div/form/button'
    xpath_deposit_successful_mgs = '/html/body/div/div/div[2]/div/div[4]/div/span'
    xpath_first_withdrawl_btn = '/html/body/div/div/div[2]/div/div[3]/button[3]'
    xpath_amount_withdrawl = '/html/body/div/div/div[2]/div/div[4]/div/form/div/input'
    xpath_second_withdrawl_btn = '/html/body/div/div/div[2]/div/div[4]/div/form/button'
    xpath_withdrawl_failed_mgs = '/html/body/div/div/div[2]/div/div[4]/div/span'
    class_transaction_btn = 'btn-lg'
    class_customer_selected = 'fontBig'
    xpath_withdraw_title = '/html/body/div[1]/div/div[2]/div/div[4]/div/form/div/label'
    xpath_withdraw_msg = '/html/body/div[1]/div/div[2]/div/div[4]/div/span'

    def __init__(self, driver):
        super(AccountPage, self).__init__(driver=driver)
        self.driver.get(self.url_account)

    def is_url_account(self):
        return self.is_url(self.url_account)

    def click_first_deposit_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_first_deposit_btn).click()

    def enter_value_deposit(self, amount='100,00'):
        self.driver.find_element(By.XPATH, self.xpath_amount_deposit).send_keys(amount)

    def click_second_deposit_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_second_deposit_btn).click()

    def deposit_successful_mgs(self):
        success_message = self.driver.find_element(By.XPATH, self.xpath_deposit_successful_mgs).text
        return "Successful" in success_message

    def click_withdrawl_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_first_withdrawl_btn).click()

    def enter_value_withdrawl(self, amount='10000000'):
        self.driver.find_element(By.XPATH, self.xpath_amount_withdrawl).send_keys(amount)

    def click_second_withdrawl_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_second_withdrawl_btn).click()

    def withdrawl_failed_mgs(self):
        return self.driver.find_element(By.XPATH, self.xpath_withdrawl_failed_mgs).text

    def is_customer_selected(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_customer_selected).text

    def click_transaction_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.class_transaction_btn).click()

    def report_withdraw_amount(self, value=5):
        self.driver.find_element(By.XPATH, self.xpath_amount_deposit).send_keys(value)

    def withdraw_title(self):
        return self.driver.find_element(By.XPATH, self.xpath_withdraw_title).text

    def withdraw_msg(self):
        return self.driver.find_element(By.XPATH, self.xpath_withdraw_msg).text
