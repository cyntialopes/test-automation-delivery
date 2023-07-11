from selenium.webdriver.common.by import By
from pages.SetupPage import SetupPage

class ManagerPage(SetupPage):
    url_manager = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    add_customer_btn = '/html/body/div/div/div[2]/div/div[1]/button[1]'
    url_manager_list = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    xpath_customers_btn = '/html/body/div/div/div[2]/div/div[1]/button[3]'
    class_search_customer = 'form-control.ng-pristine.ng-untouched.ng-valid'
    xpath_check_res_customer = '/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]'

    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)
        self.driver.get(self.url_manager)

    def is_url_manager(self):
        return self.is_url(self.url_manager)

    def is_url_manager_list(self):
        return self.is_url(self.url_manager_list)

    def click_add_customer(self):
        self.driver.find_element(By.XPATH, self.add_customer_btn).click()
    def click_customers_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_customers_btn).click()

    def fill_in_search_fields(self, search_customer='Harry'):
        self.driver.find_element(By.CLASS_NAME, self.class_search_customer).send_keys(search_customer)

    def is_check_res_customer(self):
        success_message = self.driver.find_element(By.XPATH, self.xpath_check_res_customer).text
        return "Successful" in success_message

