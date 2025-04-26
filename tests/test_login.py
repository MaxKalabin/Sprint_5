from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestLogin:
    def test_login_from_main_page(self, driver, registration):
        email, password = registration
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LOGIN_BUTTON_MAIN))
        driver.find_element(*LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(LOGIN_SUBMIT))

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MAIN_PAGE_HEADER))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()


    def test_login_from_personal_account(self, driver, registration):
        email, password = registration
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(LOGIN_SUBMIT))

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MAIN_PAGE_HEADER))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

    def test_login_from_registration_form(self, driver, registration):
        email, password = registration
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LOGIN_BUTTON_MAIN))
        driver.find_element(*LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(REGISTER_LINK))
        driver.find_element(*REGISTER_LINK).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LOGIN_LINK))
        driver.find_element(*LOGIN_LINK).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MAIN_PAGE_HEADER))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

    def test_login_from_recovery_pass_form(self, driver, registration):
        email, password = registration
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LOGIN_BUTTON_MAIN))
        driver.find_element(*LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(RECOVERY_LINK))
        driver.find_element(*RECOVERY_LINK).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LOGIN_LINK))
        driver.find_element(*LOGIN_LINK).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MAIN_PAGE_HEADER))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()
