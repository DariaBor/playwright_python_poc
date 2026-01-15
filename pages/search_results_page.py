import random
from playwright.async_api import  expect
from base import BasePage
import asyncio
class TwitchSearchResultsPage(BasePage):

    STREAM_CARD_SELECTORS = [
        'a[data-a-target="preview-card-channel-link"]',
        'a[data-test-selector*="stream-item"]',
        'div[role="link"][data-test-selector*="stream-item"]',
        'a.tw-link[href^="/"]',
    ]

    async def _get_stream_links_locator(self):

        for selector in self.STREAM_CARD_SELECTORS:
            locator = self.page.locator(selector)
            try:
                await expect(locator.first).to_be_visible(timeout=3000)
                return locator
            except Exception:
                continue

        raise Exception("No stream cards found")

    async def scroll_down(self, times: int = 1):
        for i in range(times):
            await self.scroll("down", 1)
    async def _click_with_retry(self, locator, retries: int = 5, delay: float = 0.2):
        for attempt in range(1, retries + 1):
            try:
                await locator.scroll_into_view_if_needed()
                await locator.click()
                return
            except Exception as e:
                await asyncio.sleep(delay)
        raise Exception("Click failed after maximum retries")        

    async def select_streamer(self, keyword: str | None = None, click_random: bool = False):

        stream_links = await self._get_stream_links_locator()
        count = await stream_links.count()
        if count == 0:
            raise Exception("Stream list resolved but empty")

        valid_links = []

        for i in range(count):
            candidate = stream_links.nth(i)
            href = await candidate.get_attribute("href")
            if not href:
                continue
            if href.startswith("/directory"):
                continue
            if "/" in href[1:]:
                continue

            valid_links.append(candidate)

        if not valid_links:
            raise Exception("No valid streamer links found")
        link_to_click = None
        if click_random:
            link_to_click = random.choice(valid_links)

        elif keyword:
            for candidate in valid_links:
                href = await candidate.get_attribute("href")
                if href and keyword in href:
                    link_to_click = candidate
                    break

        if link_to_click is None:
            link_to_click = valid_links[0]

        href = await link_to_click.get_attribute("href")

        await link_to_click.scroll_into_view_if_needed()
        await link_to_click.click()
        await self.page.wait_for_url(
            lambda url: "/directory" not in url,
            timeout=10000
        )
