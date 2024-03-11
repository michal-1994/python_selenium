from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAmazon:
	driver = ''

	def setup_method(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.driver.get("https://www.amazon.pl/")

	def test_amazon_empty_cart(self):
		cart = self.driver.find_element(By.ID, 'nav-cart')
		cart.click()

		actual_text = self.driver.find_element(By.XPATH, '//div[@id="sc-active-cart"]//h2').text
		expected_text = "Twój koszyk Amazon jest pusty"

		assert expected_text == actual_text, f"Error. Expected text {expected_text}, but actual text {actual_text}"

	def teardown_method(self):
		self.driver.quit()
