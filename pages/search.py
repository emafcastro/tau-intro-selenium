"""
This module contains DuckDuckGoSearchPage,
the page object for DuckDuckGo search page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:

    #URL
    URL = "https://www.duckduckgo.com"

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    SEARCH_BUTTON = (By.ID, 'search_button_homepage')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        """the find element method takes two arguments, the locator type and the query
        but SEARCH_INPUT is a tuple, * is a standar python thing that expand tuples
        into positional arguments that can be passed to methods
        """
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def search_manual(self, phrase):
        """the find element method takes two arguments, the locator type and the query
        but SEARCH_INPUT is a tuple, * is a standar python thing that expand tuples
        into positional arguments that can be passed to methods
        """
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)

        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()
