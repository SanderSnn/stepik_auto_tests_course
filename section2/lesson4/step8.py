import math
import time

import pyperclip as pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x: int) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

home_price = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
browser.find_element(By.ID, "book").click()
x = browser.find_element(By.CSS_SELECTOR, "[id=input_value]").text
result = calc(int(x))
browser.find_element(By.CSS_SELECTOR, "[id=answer]").send_keys(str(result))
browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()
alert = browser.switch_to.alert.text
addToClipBoard = alert.split(': ')[-1]
print(addToClipBoard)
pyperclip.copy(addToClipBoard)
