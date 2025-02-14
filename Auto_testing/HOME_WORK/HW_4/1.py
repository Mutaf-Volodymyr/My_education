from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService



@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('http://uitestingplayground.com/textinput')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_logo_3(driver):
    a = 'ITCH'
    f = driver.find_element(By.CSS_SELECTOR, '[class="form-control"]')
    f.click()
    f.send_keys(a)
    btn = driver.find_element(By.CSS_SELECTOR, '[id="updatingButton"]')
    btn.click()
    assert btn.text == a
