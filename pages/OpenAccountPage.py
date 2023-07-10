import random
from selenium.webdriver.common.by import By
from pages.SetupPage import SetupPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenAccountPage(SetupPage):
    url_open_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'
    id_customer_select = 'userSelect'
    id_currency_select = 'currency'
    xpath_process = '/html/body/div[1]/div/div[2]/div/div[2]/div/div/form/button'

    def __init__(self, driver):
        super(OpenAccountPage, self).__init__(driver=driver)
        self.driver.get(self.url_open_account)

    def is_url_open_account(self):
        return self.is_url(self.url_open_account)

    def select_customer(self):
        self.driver.find_element(By.ID, self.id_customer_select).click()

    def select_customer_random(self):
        customer_select = self.driver.find_element(By.ID, self.id_customer_select)
        select = Select(customer_select)
        options = select.options
        random_index = random.randint(1, len(options) - 1)
        selected_option = options[random_index]
        customer_name = selected_option.text
        selected_option.click()
        return customer_name

    def get_selected_customer(self):
        customer_select = self.driver.find_element(By.ID, self.id_customer_select)
        selected_option = Select(customer_select).first_selected_option
        return selected_option.text

    def select_currency(self):
        self.driver.find_element(By.ID, self.id_currency_select).click()

    def select_currency_random(self):
        currency_select = self.driver.find_element(By.ID, self.id_currency_select)
        select = Select(currency_select)
        options = select.options
        random_index = random.randint(1, len(options) - 1)
        selected_option = options[random_index]
        currency = selected_option.text
        selected_option.click()
        return currency

    def get_selected_currency(self):
        select_currency = self.driver.find_element(By.ID, self.id_currency_select)
        selected_option = Select(select_currency).first_selected_option
        return selected_option.text

    def click_process(self):
        self.driver.find_element(By.XPATH, self.xpath_process).click()

    def click_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text
