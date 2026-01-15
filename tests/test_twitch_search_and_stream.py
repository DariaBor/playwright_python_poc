
import pytest
from config import BASE_URL
from pages import TwitchHomePage, TwitchSearchResultsPage, TwitchStreamerPage


class TestTwitchSearchAndStream:
    GAME_NAME = "StarCraft II"

    async def test_search_starcraft_and_visit_streamer(self, page):

        # Step 1: Open Twitch in mobile emulator
        home_page = TwitchHomePage(page)
        await home_page.goto(BASE_URL)
        await home_page.wait_for_load()

        # Step 2: Search for game
        await home_page.navigate_to_browse_tab()
        await home_page.search_game(self.GAME_NAME)

        # Step 4: Scroll down 2 times
        search_results_page = TwitchSearchResultsPage(page)
        await search_results_page.scroll_down(2)

        # Step 5: Select streamer
        await search_results_page.select_streamer(click_random=True)

        # Step 6: Wait for page load and take screenshot
        streamer_page = TwitchStreamerPage(page)
        await streamer_page.wait_for_streamer_page_load()
        await streamer_page.take_screenshot("streamer_page_mobile.png")

