from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_logo_3(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[id="text"]'), 'Done!'))
    logo3 = driver.find_elements(By.CSS_SELECTOR, '#image-container img')[2]
    assert logo3.get_attribute('alt') == 'award'
