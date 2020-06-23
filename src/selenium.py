import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class SeleniumSrc(object):
    def __init__(self, browser='chrome'):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def find_element_by_xpath(self, text=False, xpath=""):
        """
        Finds the webpage element by XPATH
        :param xpath: XPath expression
        :param text: Gets the text from the element
        :return:
        """
        elem = self.driver.find_element(By.XPATH, '%s' % xpath)
        if text:
            return elem.text
        return elem

    def take_screen_shot(self, name):
        """
        Takes the screen shot of the webpage
        :return:
        """
        self.driver.save_screenshot(name)

    def close_driver(self):
        """
        Closes the webdriver
        :return:
        """
        self.driver.close()

    def open_webpage(self, url):
        """
        Opens the webpage
        :param url:
        :return:
        """
        self.driver.get(url)

    def get_title(self):
        """
        Returns the title of the webpage
        :return:
        """
        return self.driver.title

    def get_size_of_element(self, elem):
        """

        :param elem:
        :return:
        """
        return elem.size

    def send_keys_to_search(self, driver_elem, text, ret=True):
        """
        Searches for the text
        :param driver_elem:
        :param text:
        :return:
        """
        driver_elem.send_keys(text)
        if ret:
            driver_elem.send_keys(Keys.RETURN)
        time.sleep(10)
