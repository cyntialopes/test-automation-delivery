from selenium.webdriver.common.by import By
from pages.SetupPage import SetupPage


class HomePage(SetupPage):
    url_init = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    manager_login_btn = '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/button'
    customer_login_btn = '/html/body/div[1]/div/div[2]/div/div[1]/div[1]/button'
    add_customer_btn = '/html/body/div/div/div[2]/div/div[1]/button[1]'
    xpath_first_name = '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input'
    xpath_last_name = '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input'
    xpath_post_code = '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input'
    register_customer_btn = 'btn-default'

    def __init__(self, browser):
        super(HomePage, self).__init__(browser=browser)
        self.driver.get(self.url_init)

    def is_url_login(self):
        return self.is_url(self.url_init)

    def click_manager_btn(self):
        self.driver.find_element(By.XPATH, self.manager_login_btn).click()

    def click_customer_btn(self):
        self.driver.find_element(By.XPATH, self.customer_login_btn).click()

    def click_add_customer(self):
        self.driver.find_element(By.XPATH, self.add_customer_btn).click()

    def fill_reg_fields(self, first_name='Pernambuco', last_name='Tech', post_code='53.000-000'):
        self.driver.find_element(By.XPATH, self.xpath_first_name).send_keys(first_name)
        self.driver.find_element(By.XPATH, self.xpath_last_name).send_keys(last_name)
        self.driver.find_element(By.XPATH, self.xpath_post_code).send_keys(post_code)
        
    def click_second_add_customer_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.register_customer_btn).click()
