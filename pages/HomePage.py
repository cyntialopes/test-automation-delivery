from selenium.webdriver.common.by import By
from pages.SetupPage import SetupPage


class HomePage(SetupPage):
    url_login = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    manager_login_btn = '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/button'
    customer_login_btn = '/html/body/div[1]/div/div[2]/div/div[1]/div[1]/button'

    def __init__(self):
        super(HomePage, self).__init__()
        self.driver.get(self.url_login)

    def is_url_login(self):
        return self.is_url(url=self.url_login)

    def click_manager_btn(self):
        self.driver.find_element(By.XPATH, self.manager_login_btn).click()

    def click_customer_btn(self):
        self.driver.find_element(By.XPATH, self.customer_login_btn).click()
