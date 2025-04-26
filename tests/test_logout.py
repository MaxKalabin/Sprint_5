from locators import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:
    def test_successful_logout(self, driver, registration):
        email, password = registration

        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT).click()
        WebDriverWait(driver, 3).until(ec.url_to_be("https://stellarburgers.nomoreparties.site/"))

        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(LOGOUT_BUTTON))
        driver.find_element(*LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.quit()