from selenium import webdriver
from time import sleep

firefox = webdriver.Firefox()
chrome = webdriver.Chrome()

try:
    countС = 0
    countF = 0

    chrome.get("http://uitestingplayground.com/dynamicid")
    firefox.get("http://uitestingplayground.com/dynamicid")

    blue_button = chrome.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    blue_button = firefox.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    for _ in range (3):
        blue_button = chrome.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]').click()
        countС = countС + 1
        blue_button = firefox.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]').click()
        countF = countF + 1
        sleep(2)
        print(countС)
        print(countF)
except Exception as ex:
    print (ex)
finally:
    chrome.quit()
    firefox.quit()