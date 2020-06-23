import unittest
from src.selenium import SeleniumSrc


class TestGoogleMaps(unittest.TestCase):

    def setUp(self):
        self.selenium_obj = SeleniumSrc(browser='chrome')

    def test_google_map(self):
        self.selenium_obj.open_webpage(url="https://www.google.com/maps/")
        elem = self.selenium_obj.find_element_by_xpath(xpath='//*[@id=\"searchboxinput\"]')
        self.selenium_obj.send_keys_to_search(elem, 'Wankhede Stadium')
        self.selenium_obj.take_screen_shot(name='wankhede_ss.png')
        web_text = self.selenium_obj.\
            find_element_by_xpath(text=True,
                                  xpath='//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h1')
        assert "Stadium" in web_text
        rating = self.selenium_obj.\
            find_element_by_xpath(text=True,
                                  xpath='//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/span[1]/span/span')
        print("Rating: %s" % rating)
        num_of_reviews = self.selenium_obj.\
            find_element_by_xpath(text=True,
                                  xpath='//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/span[2]')
        print("Number of reviews: %s" % num_of_reviews)
        assert "Wankhede Stadium - Google Maps" in self.selenium_obj.get_title()

    def tearDown(self):
        self.selenium_obj.close_driver()


if __name__ == '__main__':
    unittest.main()
