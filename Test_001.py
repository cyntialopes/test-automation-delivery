from ConfigTest import open_login_page
class Test_001:
    def test_click_manager_btn(self, open_login_page):
        home_page = open_login_page
        home_page.click_manager_btn()
        home_page.click_add_customer()
        home_page.efetuar_cadastro()
        home_page.click_second_add_customer_btn()
