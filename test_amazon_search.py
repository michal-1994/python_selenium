from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_amazon_search():
	driver = webdriver.Chrome()
	driver.implicitly_wait(10)
	driver.get("https://www.amazon.pl/")

	search = driver.find_element(By.ID, 'twotabsearchtextbox')
	search.send_keys('spodnie męskie', Keys.ENTER)

	expected_text = '"spodnie męskiew"'
	actual_text = driver.find_element(By.XPATH, '//span[@class="a-color-state a-text-bold"]').text

	assert expected_text == actual_text, f"Error. Expected text {expected_text}, but actual text {actual_text}"

	driver.quit()
