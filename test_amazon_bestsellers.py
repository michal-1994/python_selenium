from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAmazonBestsellers:
	driver = ''

	def setup_method(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(5)
		self.driver.get("https://www.amazon.pl/")

	def test_amazon_bestsellers(self):
		bestseller = self.driver.find_element(By.XPATH, '//div[@id="nav-xshop"]/a[contains(@href, "bestsellers")]')
		bestseller.click()

		expected_links_length = 6
		actual_links = self.driver.find_elements(By.XPATH, '//div[@id="zg_left_colleft"]//div[@class="a-row a-carousel-controls a-carousel-row a-carousel-has-buttons"]')

		assert len(actual_links) == expected_links_length, f"Expected to see 5 bestsellers links, but got {len(actual_links)}"

	def teardown_method(self):
		self.driver.quit()
