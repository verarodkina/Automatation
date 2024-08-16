from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
wait = WebDriverWait(chrome, 40, 0.1)

try:
    chrome.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    wait.until(EC.text_to_be_present_in_element((By.ID, "text"), 'Done'))
    get_attribute = chrome.find_element(By.ID, "award").get_attribute("src")
    print(get_attribute)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()