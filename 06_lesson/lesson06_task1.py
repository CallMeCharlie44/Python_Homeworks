from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
click_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
click_button.click()

waiter = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )

text = waiter.text
print(text)

driver.quit()