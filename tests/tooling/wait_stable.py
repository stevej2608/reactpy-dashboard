from playwright.async_api._generated import Page


async def wait_page_stable(page:Page) -> None:
    await page.wait_for_load_state("networkidle")
    await page.wait_for_load_state("domcontentloaded")
