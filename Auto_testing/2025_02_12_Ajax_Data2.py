# http://www.uitestingplayground.com/loaddelay


from cgitb import handler

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get('http://www.uitestingplayground.com/loaddelay')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_wait(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="btn btn-primary"]')))
    btn_text = driver.find_element(By.CSS_SELECTOR,'[class="btn btn-primary"]').text
    assert btn_text == 'Button Appearing After Delay'



