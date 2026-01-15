from base import BasePage
import asyncio
from playwright.async_api import expect
class TwitchStreamerPage(BasePage):
    STREAMER_TITLE = 'h1, [data-test-selector*="stream-title"]'
    STREAMER_PLAYER = 'div[data-a-target="player-overlay-click-handler"]'
    # i couldn't catch any modal when i was openning streamers page, so can't provide proper locstor, logic for handling is below
    SOME_RANDOM_MODAL = 'div[input="nomodal"]'

    async def wait_for_streamer_page_load(self):

        timeout_ms = 10000  # 10 seconds timeout
        timeout_sec = timeout_ms / 1000

        try:
            await self.page.wait_for_load_state("domcontentloaded", timeout=timeout_ms)
            print("DOM content loaded")
        except Exception as e:
            print(f"Warning: DOM load timeout - {e}")

        modal = self.page.locator(self.SOME_RANDOM_MODAL)

        if await modal.count() > 0 and await modal.first.is_visible():
            print("modal detected")
        else:
            print("no modal detected")


        title_locator = self.page.locator(self.STREAMER_TITLE)
        player_locator = self.page.locator(self.STREAMER_PLAYER)

        start_time = asyncio.get_event_loop().time()

        while True:
            try:
                title_visible = (await title_locator.count() > 0) and (await title_locator.first.is_visible())
                player_visible = (await player_locator.count() > 0) and (await player_locator.first.is_visible())

                if title_visible or player_visible:
                    print("Streamer page loaded successfully")
                    break
            except Exception:
                pass  

            elapsed = asyncio.get_event_loop().time() - start_time
            if elapsed > timeout_sec:
                print(f"Warning: Timeout after {timeout_ms}ms, but continuing anyway")
                break

            await asyncio.sleep(0.1) 
    async def take_screenshot(self, filename: str = "streamer_page.png"):
        await self.screenshot(filename)
