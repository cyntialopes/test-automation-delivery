from selenium import webdriver
class SetupPage:
    def __init__(self, browser):
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        else:
            raise ValueError("Navegador inválido.")
        self.driver.implicitly_wait(3)

    def is_url(self, url):
        return self.driver.current_url == url

    def close(self):
        self.driver.quit()
