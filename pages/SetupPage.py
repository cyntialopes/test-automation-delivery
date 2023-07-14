from selenium import webdriver


class SetupPage:
    def __init__(self, driver=None, browser='chrome'):
        if driver:
            self.driver = driver
        elif browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        else:
            raise ValueError("Invalid browser.")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def is_url(self, url):
        return self.driver.current_url == url

    def close(self):
        self.driver.quit()
