from locators import *

class TestConstructorNavigation:
    def test_go_to_constructor_from_personal_account(self, driver):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*CONSTRUCTOR_BUTTON).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_go_to_constructor_from_logo(self, driver):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LOGO).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
