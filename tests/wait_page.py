

def wait_page(page):

    def decorator(function):
        async def wrapper(*args, **kwargs):
            await page.wait_page_stable()
            result = await function(*args, **kwargs)
            await page.wait_page_stable()
            return result
        return wrapper

    return decorator
