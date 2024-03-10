from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAmazon:
	driver = ''

	def setup_method(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.driver.get("https://www.amazon.pl/")

	def test_amazon_search_spodnie_meskie(self):
		search = self.driver.find_element(By.ID, 'twotabsearchtextbox')
		search.send_keys('spodnie męskie', Keys.ENTER)

		expected_text = '"spodnie męskie"'
		actual_text = self.driver.find_element(By.XPATH, '//span[@class="a-color-state a-text-bold"]').text

		assert expected_text == actual_text, f"Error. Expected text {expected_text}, but actual text {actual_text}"

	def test_amazon_search_buty(self):
		search = self.driver.find_element(By.ID, 'twotabsearchtextbox')
		search.send_keys('buty', Keys.ENTER)

		expected_text = '"buty"'
		actual_text = self.driver.find_element(By.XPATH, '//span[@class="a-color-state a-text-bold"]').text

		assert expected_text == actual_text, f"Error. Expected text {expected_text}, but actual text {actual_text}"

	def teardown_method(self):
		self.driver.quit()
