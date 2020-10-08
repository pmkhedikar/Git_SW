from src.pages.search import DuckDuckGoSearchPage
from src.pages.results import DuckDuckGoResultPage
import pytest

@pytest.mark.parametrize('phrase',['panda','india','parag khedikar'])
def test_basic_duckduckgo_search(browser,phrase):
    search_page = DuckDuckGoSearchPage( browser )
    result_page = DuckDuckGoResultPage( browser )
    #PHRASE = "panda"

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    # Then the search result title contains "panda"
    assert phrase in result_page.title()

    # And the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()

    assert phrase in result_page.title()