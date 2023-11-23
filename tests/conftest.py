import pytest
from _pytest.config import Config
from playwright.async_api import async_playwright

from reactpy import component, html
from reactpy.testing import BackendFixture, DisplayFixture
from reactpy.core.component import Component
from reactpy.config import REACTPY_TESTING_DEFAULT_TIMEOUT
from modules.pico import PICO_CSS
from utils.logger import log

HEADLESS = False

# Injected into page class, see below

async def _wait_page_stable(self):
    await self.wait_for_load_state("networkidle")
    await self.wait_for_load_state("domcontentloaded")


@pytest.fixture(scope="session")
def anyio_backend():
    return 'asyncio'


@pytest.fixture(scope="session")
async def display(server, page):
    async with DisplayFixture(server, page) as display:
        type(page).wait_page_stable = _wait_page_stable
        yield display


@pytest.fixture(scope="session")
async def container(display):

    class PicoContainer:

        async def show(self, app:Component):

            @component
            def AppContainer():
                return html._(
                    html.head(
                        html.link(PICO_CSS)
                    ),
                    app()
                )

            await display.show(AppContainer)

    return PicoContainer()


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

