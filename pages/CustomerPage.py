from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.SetupPage import SetupPage


class CustomerPage(SetupPage):
    url_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    id_your_name = 'userSelect'
    xpath_login_btn = '/html/body/div/div/div[2]/div/form/button'

    def __init__(self, driver):
        super(CustomerPage, self).__init__(driver=driver)
        self.driver.get(self.url_customer)

    def is_url_customers(self):
        return self.is_url(self.url_customer)

    def click_your_name(self):
        self.driver.find_element(By.ID, self.id_your_name).click()

    def select_dropdown_value(self, value):
        dropdown = Select(self.driver.find_element(By.ID, self.id_your_name))
        dropdown.select_by_value(value)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_login_btn).click()
