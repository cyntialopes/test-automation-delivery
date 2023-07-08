from selenium.webdriver.common.by import By
from pages.SetupPage import SetupPage


class AddCustomerPage(SetupPage):
    url_add_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    xpath_first_name = '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input'
    xpath_last_name = '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input'
    xpath_post_code = '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input'
    css_add_customer_btn = 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button'

    def __init__(self, driver):
        super(AddCustomerPage, self).__init__(driver=driver)
        self.driver.get(self.url_add_customer)

    def click_register_customer_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_add_customer_btn).click()

    def fill_reg_fields(self, first_name='Pernambuco', last_name='Tech', post_code='53.000-000'):
        self.driver.find_element(By.XPATH, self.xpath_first_name).send_keys(first_name)
        self.driver.find_element(By.XPATH, self.xpath_last_name).send_keys(last_name)
        self.driver.find_element(By.XPATH, self.xpath_post_code).send_keys(post_code)
