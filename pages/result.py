"""
This module contains DuckDuckGoResultPage
this page object for the DuckDuckGo search result page.
"""
from selenium.webdriver.common.by import By
import random

class DuckDuckGoResultPage:

    RESULT_LINKS = (By.CSS_SELECTOR, 'div#links > div > div > h2 > a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    RESULT_MORE = (By.CSS_SELECTOR, 'div.result.result--more')

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title

    def click_result_random(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        random_link = links[random.randint(0,len(links)-1)]
        random_link.click()
        return random_link.text

    def click_more_results(self):
        result_more = self.browser.find_element(*self.RESULT_MORE)
        result_more.click()
        
