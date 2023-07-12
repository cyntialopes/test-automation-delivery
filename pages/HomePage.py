from selenium.webdriver.common.by import By
from pages.SetupPage import SetupPage

class HomePage(SetupPage):
    url_init = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    xpath_manager_login_btn = '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/button'
    class_register_customer_btn = 'btn-default'
    xpath_customer_login_btn = '/html/body/div/div/div[2]/div/div[1]/div[1]/button'

    def __init__(self, browser):
        super(HomePage, self).__init__(browser=browser)
        self.driver.get(self.url_init)

    def is_url_login(self):
        return self.is_url(self.url_init)

    def click_manager_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_manager_login_btn).click()

    def click_register_customer_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.class_register_customer_btn).click()

    def click_customer_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_customer_login_btn).click()