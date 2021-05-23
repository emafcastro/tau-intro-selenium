"""
These tests cover DuckDuckGo searches.
"""

import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from pages.result_link_page import DuckDuckGoResultLinkPage


@pytest.mark.parametrize('phrase', ['panda', 'python','polar bear'])
def test_basic_duckduckgo_searh(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"
    
    #Given the DuckDuckGo home page is displayed
    search_page.load()

    #When the user searches for "panda"
    search_page.search(PHRASE)

    #Then the search result title contains "panda"
    assert PHRASE in result_page.title()

    #And the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0


def test_duckduckgo_search_manual(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"

    search_page.load()

    search_page.search_manual(PHRASE)

    assert PHRASE in result_page.title()


def test_duckduckgo_click_result(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    result_link_page = DuckDuckGoResultLinkPage(browser)
    PHRASE = "panda"

    search_page.load()
    search_page.search_manual(PHRASE)

    title = result_page.click_result_random()

    assert title in result_link_page.title()

def test_duckduckgo_expand_results(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"

    search_page.load()
    search_page.search_manual(PHRASE)

    count_before_more = result_page.result_link_titles()
    result_page.click_more_results()
    count_after_more = result_page.result_link_titles()

    assert len(count_before_more) < len(count_after_more)

def test_duckduckgo_autocomplete_suggestions(browser):
    search_page = DuckDuckGoSearchPage(browser)
    PHRASE = "panda"

    search_page.load()
    search_page.search_by_letter(PHRASE)

    texts = search_page.get_autocomplete_items_text()
    assert PHRASE in texts

def test_duckduckgo_selecting_autocomplete_sugestion(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"
    
    search_page.load()
    search_page.search_by_letter(PHRASE)
    items = search_page.get_autocomplete_items()
    NEW_PHRASE = search_page.select_random_option(items)


    assert NEW_PHRASE in result_page.title()

    assert NEW_PHRASE == result_page.search_input_value()


    titles = result_page.result_link_titles()
    matches = [t for t in titles if NEW_PHRASE.lower() in t.lower()]
    assert len(matches) > 0

def test_duckduckgo_search_from_result_page(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"
    NEW_PHRASE = "lion"
    
    #Given the DuckDuckGo home page is displayed
    search_page.load()

    #When the user searches for "panda"
    search_page.search(PHRASE)

    result_page.search(NEW_PHRASE)

    #Then the search result title contains "panda"
    assert NEW_PHRASE in result_page.title()

    #And the search result query is "panda"
    assert NEW_PHRASE == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if NEW_PHRASE.lower() in t.lower()]
    assert len(matches) > 0

def test_duckduckgo_image_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"

    search_page.load()
    search_page.search(PHRASE)

    result_page.change_to_image_search()
    images = result_page.get_images()

    assert len(images) > 0

    links_text = result_page.get_images_links_text()
    matches = [t for t in links_text if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

def test_duckduckgo_video_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"

    search_page.load()
    search_page.search(PHRASE)

    result_page.change_to_video_search()

    links_text = result_page.get_video_links_text()
    matches = [t for t in links_text if PHRASE.lower() in t.lower()]
    assert len(matches) > 0


def test_duckduckgo_news_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"

    search_page.load()
    search_page.search(PHRASE)

    result_page.change_to_news_search()

    links_text = result_page.get_news_links_text()
    matches = [t for t in links_text if PHRASE.lower() in t.lower()]
    assert len(matches) > 0