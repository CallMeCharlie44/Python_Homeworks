from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Firefox()
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
hidden_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(hidden_message)

sleep(2)
driver.quit
