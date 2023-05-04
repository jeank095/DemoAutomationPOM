import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.PageObject.Locators import Locators
from selenium import webdriver



driver =webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
wait = WebDriverWait(driver,10)
driver.maximize_window()


ddw = driver.find_element(By.XPATH, "//div[@id='msdd']")
ddw.click()
# driver.execute_script("arguments[0].click();",ddw)
time.sleep(2)

ele=driver.find_elements(By.XPATH, "//section[@id='section']//li//a")
for e in ele:
    if e.text == 'Urdu':
        e.click()

time.sleep(2)