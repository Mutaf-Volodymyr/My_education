
from random import random
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DELAY_MIN = 3
DELAY_MAX = 7
with open('1.txt') as f, open('check.txt', 'w') as f2:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    for url in f:
        driver.get(url.strip())
        time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))

        try:
            msg_button = driver.find_element(By.XPATH, "//div [text()='Сообщение']")
            msg_button.click()
            wait = WebDriverWait(driver, 20)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-e2e="message-input-area"] [class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')))
            time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))
            send_msg = driver.find_element(By.CSS_SELECTOR, '[data-e2e="message-input-area"] [class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
            send_msg.click()
            send_msg.send_keys()
            time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))
            send = driver.find_elements(By.TAG_NAME, 'use')

            print(f"✅ Подписался на {url}")
            print(url, file=f2)
            time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))
        except:
            print(f"⚠️ Уже подписан или кнопка не найдена на {url}")
    driver.quit()

# [class="css-1mavlr4-UserContainer e1ej9wgb0"]

# https://www.tiktok.com/@bestatter_katharina8?is_from_webapp=1&sender_device=pc