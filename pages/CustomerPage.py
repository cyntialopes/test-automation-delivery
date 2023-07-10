from selenium.webdriver.common.by import By
from pages.SetupPage import SetupPage


class CustomerPage(SetupPage):
    url_customers = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    xpath_customers_btn = '/html/body/div/div/div[2]/div/div[1]/button[3]'
    class_search_customer = 'form-control.ng-pristine.ng-untouched.ng-valid'

    def __init__(self, driver):
        super(CustomerPage, self).__init__(driver=driver)
        self.driver.get(self.url_customers)

    def is_url_customers(self):
        return self.is_url(self.url_customers)

    def click_customers_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_customers_btn).click()

    def fill_in_search_fields(self, search_customer='Harry'):
        self.driver.find_element(By.CLASS_NAME, self.class_search_customer).send_keys(search_customer)

