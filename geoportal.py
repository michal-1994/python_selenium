from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://michal-1994.github.io/proj-map/")

configurator = driver.find_element(By.XPATH, '//a[@href="/proj-map/configurator"]')

print(configurator.text)
configurator.click()

driver.quit()
