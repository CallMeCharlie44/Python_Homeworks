from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("http://the-internet.herokuapp.com/inputs")

sleep(3)

text_1 = "Sky"
text_2 = "Pro"

search_input = driver.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys(text_1)
sleep(2)
search_input.clear()
search_input.send_keys(text_2)
sleep(2)
driver.quit()