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
    amount_errors = 0
    
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

    texts = search_page.get_autocomplete_items()
    assert PHRASE in texts