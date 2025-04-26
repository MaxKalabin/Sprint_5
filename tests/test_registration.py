from locators import *
from generators import generate_email, generate_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestRegistration:
    def test_successful_registration(self, driver):
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LOGIN_BUTTON_MAIN))
        driver.find_element(*LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(REGISTER_LINK))
        driver.find_element(*REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(NAME_INPUT))
        driver.find_element(*NAME_INPUT).send_keys("Максим")
        driver.find_element(*EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*PASSWORD_INPUT).send_keys(generate_password())
        driver.find_element(*REGISTER_SUBMIT).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(LOGIN_SUBMIT))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.quit()


    def test_invalid_password_error(self, driver):
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LOGIN_BUTTON_MAIN))
        driver.find_element(*LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(REGISTER_LINK))
        driver.find_element(*REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(NAME_INPUT))
        driver.find_element(*NAME_INPUT).send_keys("Максим")
        driver.find_element(*EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*PASSWORD_INPUT).send_keys("123")
        driver.find_element(*REGISTER_SUBMIT).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(REGISTER_SUBMIT))

        assert driver.find_element(*PASSWORD_ERROR).is_displayed()
        driver.quit()