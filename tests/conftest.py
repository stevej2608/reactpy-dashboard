import pytest
from playwright.async_api import Browser
from playwright.async_api import async_playwright, Page
from reactpy.testing import DisplayFixture, BackendFixture
from reactpy.config import REACTPY_TESTING_DEFAULT_TIMEOUT
from tests.page_containers import PicoContainer

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--headed",
        dest="headed",
        action="store_true",
        help="Open a browser window when running web-based tests",
    )


@pytest.fixture(scope="session")
async def display(server: BackendFixture, page: Page):
    async with DisplayFixture(server, page) as display:
        yield display


@pytest.fixture(scope="session")
async def pico_container(display: DisplayFixture):
    return PicoContainer(display)


@pytest.fixture(scope="session")
async def server():
    async with BackendFixture() as server:
        yield server

@pytest.fixture(scope="session")
async def page(browser: Browser):
    pg = await browser.new_page()
    pg.set_default_timeout(REACTPY_TESTING_DEFAULT_TIMEOUT.current * 1000)
    try:
        yield pg
    finally:
        await pg.close()

@pytest.fixture(scope="session")
async def browser(pytestconfig: pytest.Config):
    async with async_playwright() as pw:
        yield await pw.chromium.launch(headless=not bool(pytestconfig.option.headed))
