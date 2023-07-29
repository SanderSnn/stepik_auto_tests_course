import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def calc(x: int) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'info.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.CSS_SELECTOR, "[name=firstname]").send_keys("Sander")
    browser.find_element(By.CSS_SELECTOR, "[name=lastname]").send_keys("Kaiser")
    browser.find_element(By.CSS_SELECTOR, "[name=email]").send_keys("2@test.com")
    print(file_path)
    browser.find_element(By.CSS_SELECTOR, "[id=file]").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
