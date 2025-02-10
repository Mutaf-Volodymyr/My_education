from cgitb import handler

from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get('https://suninjuly.github.io/registration1.html')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_complete_registration(driver):
    first_name_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    first_name_input.click()
    first_name_input.send_keys('Vova')

    last_name_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    last_name_input.click()
    last_name_input.send_keys('Mutaf')

    email_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    email_input.click()
    email_input.send_keys('mutaf@example.com')

    submit_btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_btn.click()

    result = driver.find_element(By.CSS_SELECTOR, 'h1')
    assert result.text == 'Congratulations! You have successfully registered!'


def test_complete_all_field_registration(driver):
    first_name_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    first_name_input.click()
    first_name_input.send_keys('Vova')

    last_name_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    last_name_input.click()
    last_name_input.send_keys('Mutaf')

    email_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    email_input.click()
    email_input.send_keys('mutaf@example.com')

    email_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    email_input.click()
    email_input.send_keys('mutaf@example.com')

    phone_input = driver.find_element(By.CSS_SELECTOR, '[placeholder = "Input your phone:"]')
    phone_input.click()
    phone_input.send_keys('12345678')

    phone_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]')
    phone_input.click()
    phone_input.send_keys('Berlin')

    submit_btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_btn.click()

    result = driver.find_element(By.CSS_SELECTOR, 'h1')
    assert result.text == 'Congratulations! You have successfully registered!'




def test_non_complete_registration(driver):
    first_name_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    first_name_input.click()
    first_name_input.send_keys('Vova')

    last_name_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    last_name_input.click()
    last_name_input.send_keys('Mutaf')

    submit_btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_btn.click()
    email_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    email_input.get_attribute("focus")
    assert email_input.get_attribute("validationMessage")== "Заполните это поле.", "Validation message is incorrect"