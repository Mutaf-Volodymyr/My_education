from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC


# span = driver.find_element(By.CSS_SELECTOR, '[name="todo-1"] ~ span')
# text_decoration = driver.execute_script("return window.getComputedStyle(arguments[0]).textDecoration;", span)

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://crossbrowsertesting.github.io/todo-app.html')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_1(driver):
    element = driver.find_element(By.CSS_SELECTOR, '[name="todo-1"]')
    element.click()
    res = driver.find_element(By.CSS_SELECTOR, '[name="todo-1"] ~ span')
    assert res.get_attribute('class') == 'done-true'

def test_2(driver):
    element = driver.find_element(By.CSS_SELECTOR, '[name="todo-1"]')
    element.click()

