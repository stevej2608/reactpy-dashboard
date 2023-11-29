from typing import Union, Callable, Any
from reactpy import component, html

IterableComponent = Union[Callable[[Any], Callable], Callable[[int, Any], Callable]]


@component
def For(component: IterableComponent, iterator: Union[list, enumerate]) -> Callable:
    """Apply the iterator to the given component

    Usage:

    ```
        users = ["Test User", "Real User 1", "Real User 2"]

        For(html.h2, iterator=users)

        @component
        def TableRow(index:int, row:Any):
            ...

        For(TableRow, iterator=enumerate(users))
    ```
    """
    if isinstance(iterator, enumerate):
        return html._(*[component(index, value) for index, value in iterator])
    else:
        return html._(*[component(name) for name in iterator])
    