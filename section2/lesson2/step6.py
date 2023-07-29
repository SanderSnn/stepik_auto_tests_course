import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def calc(x: int) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "[id=input_value]").text
    result = calc(int(x))
    browser.find_element(By.CSS_SELECTOR, "[id=answer]").send_keys(str(result))
    browser.find_element(By.CSS_SELECTOR, "[for=robotCheckbox]").click()
    robots_rule = browser.find_element(By.CSS_SELECTOR, "[for=robotsRule]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
    robots_rule.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
