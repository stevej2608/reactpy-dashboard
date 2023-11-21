import pytest
from _pytest.config import Config
from playwright.async_api import async_playwright
from reactpy.testing import BackendFixture, DisplayFixture

from reactpy.config import REACTPY_TESTING_DEFAULT_TIMEOUT

from utils.logger import log

HEADLESS = False

# Injected into page class


async def custom_wait_for_selector(self, name):

    # TODO: See if a better way can be found for detecting the dom is stable

    async def wait_reactpy_stable():
        await self.wait_for_load_state("networkidle")
        await self.wait_for_load_state("domcontentloaded")

    element_handle = None
    while not element_handle:
        try:
            await wait_reactpy_stable()
            element_handle = await self.query_selector(name)
            await wait_reactpy_stable()
        except Exception as ex:
            log.info('Unable to resolve selector %s', name)
    return element_handle


@pytest.fixture(scope="session")
def anyio_backend():
    return 'asyncio'


@pytest.fixture(scope="session")
async def display(server, page):
    async with DisplayFixture(server, page) as display:
        type(page).custom_wait_for_selector = custom_wait_for_selector
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
async def browser(pytestconfig: Config):
    async with async_playwright() as pw:
        yield await pw.chromium.launch(headless =not bool(pytestconfig.option.headed))

