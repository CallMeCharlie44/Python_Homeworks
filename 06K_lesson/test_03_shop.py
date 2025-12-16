from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_shop():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Анастасия")
    driver.find_element(By.ID, "last-name").send_keys("Васильева")
    driver.find_element(By.ID, "postal-code").send_keys("428038")

    driver.find_element(By.ID, "continue").click()

    element = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label")
    total_price = element.text

    wait = WebDriverWait(driver, 26)

    print(f"Проверка успешна! Итоговая сумма равна {total_price}")
    driver.quit()