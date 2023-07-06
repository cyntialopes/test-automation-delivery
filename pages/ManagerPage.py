from selenium.webdriver.common.by import By
from pages.SetupPage import SetupPage


class ManagerPage(SetupPage):
    url_manager = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    add_customer_btn = '/html/body/div/div/div[2]/div/div[1]/button[1]'

    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)
        self.driver.get(self.url_manager)

    def is_url_manager(self):
        return self.is_url(self.url_manager)

    def click_add_customer(self):
        self.driver.find_element(By.XPATH, self.add_customer_btn).click()
