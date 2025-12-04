from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("--start-maximized")

service = EdgeService("/Users/dartcharlie/Downloads/edgedriver_mac64/msedgedriver")
driver = webdriver.Edge(service=service, options=options)


def test_first_name():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, 'first-name').send_keys('Иван')
    driver.find_element(By.NAME, 'last-name').send_keys('Петров')
    driver.find_element(By.NAME, 'address').send_keys('Ленина, 55-3')
    driver.find_element(By.NAME, 'e-mail').send_keys('test@skypro.com')
    driver.find_element(By.NAME, 'phone').send_keys('+7985899998787')
    driver.find_element(By.NAME, 'zip-code').send_keys('')
    driver.find_element(By.NAME, 'city').send_keys('Москва')
    driver.find_element(By.NAME, 'country').send_keys('Россия')
    driver.find_element(By.NAME, 'job-position').send_keys('QA')
    driver.find_element(By.NAME, 'company').send_keys('SkyPro')
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    wait = WebDriverWait(driver, 26)



zip_code_field = driver.find_element(By.ID, 'zip-code')
assert 'alert-danger' in zip_code_field.get_attribute('class')

green_fields = [
        'first-name', 'last-name', 'address', 'e-mail', 'phone',
        'city', 'country', 'job-position', 'company']

for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        assert 'alert-success' in field.get_attribute('class')

driver.quit()






