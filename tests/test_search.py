"""
These tests cover DuckDuckGo searches.
"""

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_searh(browser):
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

    print(*result_page.result_link_titles())
    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()

    # And the search result links pertain to "panda"
    #for title in result_page.result_link_titles():
    #    try:
    #        assert PHRASE.lower() in title.lower()
    #    except AssertionError:
    #        amount_errors += 1
    #        continue