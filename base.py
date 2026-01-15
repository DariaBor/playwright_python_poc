import os
import pytest
from pathlib import Path
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from config import BASE_URL, MOBILE_DEVICE, BROWSER_LAUNCH_OPTIONS, SCREENSHOTS_DIR


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    async def goto(self, url: str):
        await self.page.goto(url)

    async def click(self, selector: str):
        await self.page.click(selector)

    async def fill(self, selector: str, text: str):
        await self.page.fill(selector, text)

    async def screenshot(self, filename: str):
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        filepath = Path(SCREENSHOTS_DIR) / filename
        await self.page.screenshot(path=str(filepath))
        print(f"Screenshot saved: {filepath}")

    async def scroll(self, direction: str = "down", amount: int = 1):
        for _ in range(amount):
            if direction == "down":
                await self.page.evaluate("window.scrollBy(0, window.innerHeight)")
            elif direction == "up":
                await self.page.evaluate("window.scrollBy(0, -window.innerHeight)")
            await self.page.wait_for_timeout(500)

    async def wait_for_load(self):
        try:
            await self.page.wait_for_load_state("domcontentloaded", timeout=15000)
        except:
            print("Warning: DOM load timeout, continuing anyway")


@pytest.fixture
async def browser():
    playwright = await async_playwright().start()
    browser_instance = await playwright.chromium.launch(**BROWSER_LAUNCH_OPTIONS)
    try:
        yield browser_instance
    finally:
        await browser_instance.close()
        await playwright.stop()


@pytest.fixture
async def page(browser):

    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)

    context = await browser.new_context(
        **MOBILE_DEVICE,
        locale="en-US",
        timezone_id="America/New_York",
        extra_http_headers={
            "Accept-Language": "en-US,en;q=0.9",
        },
        record_video_dir=str(videos_dir),
    )
    page_instance = await context.new_page()
    try:
        yield page_instance
    finally:
        await context.close()
