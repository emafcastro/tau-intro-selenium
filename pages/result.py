"""
This module contains DuckDuckGoResultPage
this page object for the DuckDuckGo search result page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

class DuckDuckGoResultPage:

    RESULT_LINKS = (By.CSS_SELECTOR, 'div#links > div > div > h2 > a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    RESULT_MORE = (By.CSS_SELECTOR, 'div.result.result--more')
    DUCKBAR_SEARCH_MENU_ELEMENTS = (By.CSS_SELECTOR, 'div#duckbar > div > ul > li > a')
    IMAGES = (By.TAG_NAME, 'img')
    RESULT_IMAGES_LINKS = (By.CSS_SELECTOR, 'div#zero_click_wrapper > div > div > div > div > div > a')
    RESULT_VIDEOS_LINKS = (By.CSS_SELECTOR, '#zci-videos > div > div > div > div > div > h6 > a')
    RESULT_NEWS_LINKS = (By.CSS_SELECTOR, 'h2 > a.result__a')

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
        
    def search(self, phrase):
        """the find element method takes two arguments, the locator type and the query
        but SEARCH_INPUT is a tuple, * is a standar python thing that expand tuples
        into positional arguments that can be passed to methods
        """
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(phrase + Keys.RETURN)

    def change_to_image_search(self):
        menu_elements = self.browser.find_elements(*self.DUCKBAR_SEARCH_MENU_ELEMENTS)
        menu_elements[1].click()

    def get_images(self):
        images = self.browser.find_elements(*self.IMAGES)
        return images

    def get_images_links_text(self):
        images_links = self.browser.find_elements(*self.RESULT_IMAGES_LINKS)
        texts = [link.text for link in images_links]
        return texts


    def change_to_video_search(self):
        menu_elements = self.browser.find_elements(*self.DUCKBAR_SEARCH_MENU_ELEMENTS)
        menu_elements[2].click()

    def get_video_links_text(self):
        video_links = self.browser.find_elements(*self.RESULT_VIDEOS_LINKS)
        texts = [link.text for link in video_links]
        return texts


    def change_to_news_search(self):
        menu_elements = self.browser.find_elements(*self.DUCKBAR_SEARCH_MENU_ELEMENTS)
        menu_elements[3].click()

    def get_news_links_text(self):
        news_links = self.browser.find_elements(*self.RESULT_NEWS_LINKS)
        texts = [link.text for link in news_links]
        return texts