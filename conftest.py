
import pytest
import sys
from base import browser, page

__all__ = ["browser", "page"]

def pytest_configure(config):
    if sys.platform == "darwin":
        import asyncio
        try:
            asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
        except:
            pass
