from selenium.webdriver.common.by import By
from data import *

def test_shop(chrome_browser):
    chrome_browser.get(url_3)
    chrome_browser.find_element(By.ID, "user-name").send_keys("standart_user")
    chrome_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome_browser.find_element(By.ID, "login-button").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    chrome_browser.find_element(By.ID, "shoping_cart_contrainer").click()
    chrome_browser.find_element(By.ID, "checkout").click()
    chrome_browser.find_element(By.ID, "first-name").send_keys("Алина")
    chrome_browser.find_element(By.ID, "last-name").send_keys("Петрова")
    chrome_browser.find_element(By.ID, "postal-code").send_keys("650903")
    chrome_browser.find_element(By.ID, "continue").click()
    total_prise = chrome_browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_prise.text.strip().replace("Total: $", "")

    expected_total = "58.29"
    assert total == expected_total
    print("Итоговая сумма равна $58.29")