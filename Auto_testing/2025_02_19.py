from math import sin, log
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC




@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://crossbrowsertesting.github.io/hover-menu.html') # http://suninjuly.github.io/huge_form.html
    driver.maximize_window()
    yield driver
    # driver.quit()

# def test_alert(driver):
#     inputs_field = driver.find_elements(By.TAG_NAME, 'input')
#     for field in inputs_field:
#         field.click()
#         field.send_keys('Hallo')
#     driver.find_element(By.TAG_NAME, 'button').click()
#     wait = WebDriverWait(driver, 10)
#     alert = wait.until(EC.alert_is_present())
#     assert "Congrats, you've passed the task!" in alert.text

# https://suninjuly.github.io/math.html




# def test_alert(driver):
#     driver.find_element(By.TAG_NAME, 'button').click()
#     driver.switch_to.window(driver.window_handles[-1])
#     x = driver.find_element(By.ID, 'input_value')
#     y = log(abs(12*sin(int(x.text))))
#     answer = driver.find_element(By.ID, 'answer')
#     answer.click()
#     answer.send_keys(str(y))
#     driver.find_element(By.TAG_NAME, 'button').click()
#     wait = WebDriverWait(driver, 10)
#     alert = wait.until(EC.alert_is_present())
#     sleep(300)


def test_action(driver):
    actions = ActionChains(driver)
    elements = driver.find_elements(By.CSS_SELECTOR, '[class="dropdown-toggle"]')
    actions.move_to_element(elements[0])
    actions.perform()
    actions.move_to_element(elements[1])
    actions.perform()
    
    driver.find_element(By.CSS_SELECTOR, '[onclick="handleSecondaryAction()"]').click()
    wait = WebDriverWait(driver, 10)
    res = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'jumbotron secondary-clicked'))).text
    assert res == 'Secondary Page'



