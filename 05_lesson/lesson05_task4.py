from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

username = "tomsmith"
password = "SuperSecretPassword!"

search_input_username = driver.find_element(By.CSS_SELECTOR, "input#username")
search_input_username.send_keys(username)

sleep(2)

search_input_password = driver.find_element(By.CSS_SELECTOR, "input[id='password']")
search_input_password.send_keys(password)

sleep(2)

buttom_login = driver.find_element(By.CSS_SELECTOR, ".fa" )
buttom_login.click()

sleep(2)
hidden_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success").text
print(hidden_message)

sleep(2)
driver.quit()
