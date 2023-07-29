from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects2.html")

    x = browser.find_element(By.CSS_SELECTOR, "[id=num1]").text
    y = browser.find_element(By.CSS_SELECTOR, "[id=num2]").text
    result = int(x) + int(y)
    print(result)
    select = Select(browser.find_element(By.CSS_SELECTOR, "[id=dropdown]"))
    select.select_by_visible_text(str(result))
    browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
