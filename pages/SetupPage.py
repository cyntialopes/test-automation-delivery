from selenium import webdriver


class SetupPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def is_url(self, url):
        return self.driver.current_url == url

    def close(self):
        self.driver.quit()
