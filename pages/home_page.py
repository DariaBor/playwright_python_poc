from playwright.async_api import expect
from base import BasePage
from config import MOBILE_DEVICE


class TwitchHomePage(BasePage):
    SEARCH_INPUT_PRIMARY = 'input[data-a-target="tw-input"]'
    COOKIE_REJECT = 'button:has-text("Reject")'
    BROWSE_TAB = 'a[href="/directory"]'
    EXACT_MATCH = 'a[href="/directory/category/starcraft-ii"]'

    async def dismiss_cookie_dialog(self):
        cookie_button = self.page.locator(self.COOKIE_REJECT)

        if await cookie_button.is_visible():
            await cookie_button.click()
        else:
            print("No cookie dialog found")

    async def navigate_to_browse_tab(self):
        if not MOBILE_DEVICE.get("is_mobile", False):
            print("Skipping navigate to Browse - not on mobile device")
            return

        await self.dismiss_cookie_dialog()
        browse_tab = self.page.get_by_role("link", name="Browse")
        await expect(browse_tab).to_be_visible()
        await browse_tab.click()

    async def search_game(self, game_name: str):
        search_input = self.page.locator(self.SEARCH_INPUT_PRIMARY)
        await expect(search_input).to_be_visible()
        await search_input.fill(game_name)
        exact_match = self.page.locator(self.EXACT_MATCH)
        await expect(exact_match).to_be_visible()
        await exact_match.click()
        await self.page.wait_for_load_state("networkidle")
