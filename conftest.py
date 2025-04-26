import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from generators import generate_email, generate_password
from locators import *
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    return driver

@pytest.fixture()
def registration(driver):
    email = generate_email()
    password = generate_password()

    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN))
    driver.find_element(*LOGIN_BUTTON_MAIN).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(REGISTER_LINK))
    driver.find_element(*REGISTER_LINK).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(NAME_INPUT))
    driver.find_element(*NAME_INPUT).send_keys("Максим")
    driver.find_element(*EMAIL_INPUT).send_keys(email)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)
    driver.find_element(*REGISTER_SUBMIT).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LOGIN_SUBMIT))
    return email, password