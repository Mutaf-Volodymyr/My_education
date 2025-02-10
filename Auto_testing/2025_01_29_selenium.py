from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest


# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# driver.get("https://itcareerhub.de/ru")
# sleep(1)
# # sleep(1)
# # driver.get("https://www.berlin.de")
# # sleep(1)
# # driver.back()
# # sleep(1)
# # driver.forward()
# # sleep(1)
# # driver.refresh()
# # sleep(1)
# # driver.set_window_size(640, 460)
# # sleep(1)
# driver.fullscreen_window()
# about_link = driver.find_element(By.LINK_TEXT, "О нас")
# about_link.click()
# sleep(1)
# driver.save_screenshot("/Users/vladimirmutaf/Documents/IT/My_education/Auto_testing/screen_shots/1.png")
# sleep(15)
# # driver.set_window_size(640, 460)
# # sleep(1)
# # driver.minimize_window()
# # sleep(1)


# fixture

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_open_google(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title


def test_about_page(driver):
    driver.get("https://itcareerhub.de/ru")
    about_link = driver.find_element(By.LINK_TEXT, "О нас")
    about_link.click()
    assert "О нас" in driver.title, "Переход на страницу 'О нас' не выполнен!"


