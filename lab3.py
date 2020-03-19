import time
import unittest

from selenium import webdriver


class RandomNumberTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://psychicscience.org/random")
        self.driver.find_element_by_id("num").send_keys('1', '0')
        self.driver.find_element_by_id("st").send_keys('5')
        self.driver.find_element_by_id("en").send_keys('3', '0')
        self.driver.find_element_by_id("go").click()
        time.sleep(1)
        self.results = self.driver.find_element_by_id("output").get_attribute('value').split("\n", 1)[0].split()

    def test_numbersInRange(self):
        for x in self.results:
            assert 5 <= int(x) <= 30

    def test_numberQuantity(self):
        assert len(self.results) == 10

    def test_onlyDigits(self):
        for x in self.results:
            assert x.isdigit()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
