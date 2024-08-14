from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()

try:
    chrome.get("http://uitestingplayground.com/textinput")
    button_name = chrome.find_element(
        "id", "newButtonName").send_keys("SkyPro")
    confirm_button_name = chrome.find_element("id", "updatingButton").click()
    new_button_name =  chrome.find_element("id", "updatingButton").text

    print(new_button_name)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()