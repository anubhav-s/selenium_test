import time
import unittest
from src.selenium import SeleniumSrc


class TestAppSpot(unittest.TestCase):

    def setUp(self):
        self.selenium_obj = SeleniumSrc(browser='firefox')

    def test_app_spot(self):
        self.selenium_obj.open_webpage(url="http://ata123456789123456789.appspot.com/")
        text_1 = self.selenium_obj.find_element_by_xpath(xpath='//*[@id=\"ID_nameField1\"]')
        text_2 = self.selenium_obj.find_element_by_xpath(xpath='//*[@id=\"ID_nameField2\"]')
        text_1.clear()
        self.selenium_obj.send_keys_to_search(text_1, text='7', ret=False)
        text_2.clear()
        self.selenium_obj.send_keys_to_search(text_2, text='4', ret=False)
        euclid = self.selenium_obj.find_element_by_xpath(xpath='//*[@id=\"gwt-uid-7\"]')
        time.sleep(10)
        euclid.click()
        self.selenium_obj.find_element_by_xpath(xpath='//*[@id=\"ID_calculator\"]').click()
        time.sleep(10)
        result = self.selenium_obj.find_element_by_xpath(xpath='//*[@id="ID_nameField3"]').get_attribute('value')
        a, b = 7, 4
        exp = a ** 2 - 2 * (a * b) + b ** 2
        self.assertEqual(exp, int(result))

    def tearDown(self):
        self.selenium_obj.close_driver()


if __name__ == '__main__':
    unittest.main()
