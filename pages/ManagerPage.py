from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.SetupPage import SetupPage


class ManagerPage(SetupPage):
    url_manager = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    xpath_add_customer_btn = '/html/body/div/div/div[2]/div/div[1]/button[1]'
    xpath_open_account_btn = '/html/body/div/div/div[2]/div/div[1]/button[2]'

    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)
        self.driver.get(self.url_manager)

    def is_url_manager(self):
        return self.is_url(self.url_manager)

    def click_add_customer(self):
        self.driver.find_element(By.XPATH, self.xpath_add_customer_btn).click()

    def click_open_account(self):
        self.driver.find_element(By.XPATH, self.xpath_open_account_btn).click()

    @staticmethod
    def click_alert(open_page):
        WebDriverWait(open_page.driver, 10).until(EC.alert_is_present())
        alert = open_page.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text
