import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.SetupPage import SetupPage


class SearchCustomerPage(SetupPage):
    url_search_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    id_customer_select = 'userSelect'
    xpath_login = '/html/body/div[1]/div/div[2]/div/form/button'

    def __init__(self, driver):
        super(SearchCustomerPage, self).__init__(driver=driver)
        self.driver.get(self.url_search_customer)

    def is_url_search_customer(self):
        return self.is_url(self.url_search_customer)

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

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_login).click()
