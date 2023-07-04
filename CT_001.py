class CT001:
    def test_click_manager_btn(self, setup):
        home_page = setup
        home_page.click_manager_btn()
        assert home_page.is_url_login(), 'Error Page'
