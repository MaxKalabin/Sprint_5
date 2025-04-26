from locators import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    def test_sauces_section_activation(self, driver):
        element = driver.find_element(*SAUCES_SECTION)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(ACTIVE_SECTION))
        active_section = driver.find_element(*ACTIVE_SECTION).text
        assert active_section == 'Соусы'
        driver.quit()

    def test_fillings_section_activation(self, driver):
        element = driver.find_element(*FILLINGS_SECTION)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(ACTIVE_SECTION))
        active_section = driver.find_element(*ACTIVE_SECTION)
        assert "Начинки" in active_section.text
        driver.quit()

    def test_buns_section_activation(self, driver):
        driver.find_element(*SAUCES_SECTION).click()

        element = driver.find_element(*BUNS_SECTION)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(ACTIVE_SECTION))
        active_section = driver.find_element(*ACTIVE_SECTION)
        assert "Булки" in active_section.text
        driver.quit()