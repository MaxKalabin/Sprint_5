from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import *

class TestPersonalAccount:
    def test_go_to_personal_account(self, driver, registration):
        email, password = registration

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MAIN_PAGE_HEADER))

        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(LOGOUT_BUTTON))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
