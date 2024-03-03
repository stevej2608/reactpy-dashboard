from typing import Callable, Any, Coroutine
from playwright.async_api import Page
from .tooling.wait_stable import wait_page_stable

FuncType = Callable[..., Coroutine[Any, Any, Any]]

def wait_page(page: Page) -> Callable[[FuncType], FuncType]:

    def _decorator(decorated_func: FuncType) -> FuncType:

        async def _wrapper( *_args: Any, **_kwargs: Any) -> Any:
            await wait_page_stable(page)
            result = await decorated_func(*_args, **_kwargs)
            await wait_page_stable(page)
            return result

        return _wrapper

    return _decorator

