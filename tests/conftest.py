import pytest
from playwright.async_api import async_playwright
from reactpy.testing import BackendFixture, DisplayFixture

from reactpy.config import REACTPY_TESTING_DEFAULT_TIMEOUT

HEADLESS = False


@pytest.fixture(scope="session")
def anyio_backend():
    return 'asyncio'


@pytest.fixture(scope="session")
async def display(server, page):
    async with DisplayFixture(server, page) as display:
        yield display


@pytest.fixture(scope="session")
async def server():
    async with BackendFixture() as server:
        yield server


@pytest.fixture(scope="session")
async def page(browser):
    pg = await browser.new_page()
    pg.set_default_timeout(REACTPY_TESTING_DEFAULT_TIMEOUT.current * 1000)
    try:
        yield pg
    finally:
        await pg.close()


@pytest.fixture(scope="session")
async def browser():
    async with async_playwright() as pw:
        yield await pw.chromium.launch(headless = True)

