from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_ich_payment(driver):
    driver.get("https://itcareerhub.de/ru")
    about_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    about_link.click()
    sleep(2)
    driver.save_screenshot("/Users/vladimirmutaf/Documents/IT/My_education/Auto_testing/screen_shots/1.png")
