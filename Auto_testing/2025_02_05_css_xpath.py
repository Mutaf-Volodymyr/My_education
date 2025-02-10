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

site_url = "https://suninjuly.github.io/cats.html"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get(site_url)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_cats_page(driver):
    header = driver.find_element(By.TAG_NAME, "h1")
    assert header.text == "Cat memes"


def test_first_cats_time(driver):
    header = driver.find_element(By.CSS_SELECTOR, '[class="col-sm-4"]:first-child small')
    assert header.text == "9 mins"

def test_i_love_you_so_much(driver):
    header = driver.find_element(By.XPATH, '//*[@class="col-sm-4"][last()]//*[@class="card-text"]')
    assert header.text == "I love you so much"



def test_is_displayed_first_cart(driver):
    header = driver.find_element(By.CSS_SELECTOR, '.col-sm-4:nth-child(1)')
    assert header.is_displayed()


def test_is_displayed_foto_icon(driver):
    header = driver.find_element(By.TAG_NAME, 'svg')
    assert header.is_displayed()

def test_check_all_img(driver):
    all_img = driver.find_elements(By.CSS_SELECTOR,'[class="row"] img')
    assert len(all_img) == 6

def test_check_all_cards(driver):
    crts = driver.find_elements(By.CSS_SELECTOR,'[class="row"] [class="col-sm-4"]')
    assert len(crts) == 6

def test_check_all_cards_displeid(driver):
    crts = driver.find_elements(By.CSS_SELECTOR,'[class="row"] [class="col-sm-4"]')
    assert all(i.is_displayed() for i in crts)



