from pages.SetupPage import SetupPage


class HomePage(SetupPage):
    url_manager = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    add_customer_btn = '/html/body/div/div/div[2]/div/div[1]/button[1]'

    def __init__(self, driver):
        super(HomePage, self).__init__(driver=driver)
        self.driver.get(self.url_manager)

    def is_url_manager(self):
        return self.is_url(self.url_manager)
