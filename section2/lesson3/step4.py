import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x: int) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.CSS_SELECTOR, "[id=input_value]").text
    result = calc(int(x))
    browser.find_element(By.CSS_SELECTOR, "[id=answer]").send_keys(str(result))
    browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
