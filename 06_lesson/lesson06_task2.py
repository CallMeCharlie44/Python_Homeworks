from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

Field = driver.find_element(By.CSS_SELECTOR, "input#newButtonName").send_keys("SkyPro")
clic_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

waiter = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
)
print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)



# waiter = WebDriverWait(driver, 20)

# Field = driver.find_element(By.CSS_SELECTOR, "input#newButtonName").send_keys("SkyPro")

# clic_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click

# waiter = WebDriverWait.until(
#     EC.text_to_be_present_in_element( (By.CSS_SELECTOR, "#updatingButton"), "SkyPro" )
# )

# print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)






