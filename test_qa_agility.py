import unittest
from src.selenium import SeleniumSrc


class TestQaAgility(unittest.TestCase):

    def setUp(self):
        self.selenium_obj = SeleniumSrc(browser='chrome')

    def test_qa_agility(self):
        self.selenium_obj.open_webpage(url="https://www.qaagility.com")
        assert "QAAgility" in self.selenium_obj.get_title()
        logo_elem = self.selenium_obj.\
            find_element_by_xpath(xpath='//*[@id=\"site-navigation\"]/div/div[1]/div[1]/a/img')
        size = self.selenium_obj.get_size_of_element(logo_elem)
        print("Height: %d" % size['height'])
        print("Width: %d" % size['width'])
        footer = self.selenium_obj.find_element_by_xpath(text=True, xpath='/html/body/div[2]/footer/div/div')
        self.assertEqual(footer, "QAAgility Technologies © 2020. All Rights Reserved")

    def tearDown(self):
        self.selenium_obj.close_driver()


if __name__ == '__main__':
    unittest.main()
