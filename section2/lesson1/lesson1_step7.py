import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x: int) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    chest = browser.find_element(By.CSS_SELECTOR, "[src*='chest']")
    x = chest.get_attribute("valuex")
    print(x)
    result = calc(x)
    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(result)

    browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]').click()
    browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]').click()
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
