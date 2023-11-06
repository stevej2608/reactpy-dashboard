from typing import Generator
import asyncio
import pytest
from playwright.async_api import async_playwright
from reactpy.testing import BackendFixture, DisplayFixture

from reactpy.config import REACTPY_TESTING_DEFAULT_TIMEOUT

HEADLESS = False

@pytest.fixture(scope="session")
def anyio_backend():
    return 'asyncio'

@pytest.fixture(scope="session", autouse=False)
def event_loop(_request) -> Generator:  # : indirect usage
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def browser(pytestconfig):
    async with async_playwright() as pw:
        yield await pw.chromium.launch(headless= not pytestconfig.getoption('--headed'))


@pytest.fixture(scope="session")
async def page(browser):
    pg = await browser.new_page()
    pg.set_default_timeout(REACTPY_TESTING_DEFAULT_TIMEOUT.current * 1000)
    try:
        yield pg
    finally:
        await pg.close()

@pytest.fixture(scope="session")
async def server():
    async with BackendFixture() as server:
        yield server

@pytest.fixture(scope="session")
async def display(server, page):
    async with DisplayFixture(server, page) as display:
        yield display
