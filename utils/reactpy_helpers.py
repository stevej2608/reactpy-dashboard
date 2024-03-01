from typing import Callable, Any, Union, cast, List, overload

from reactpy import html
from reactpy.core.types import VdomDict

ListCallable = Callable[[Any], VdomDict]
EnumerateCallable = Callable[[int, Any], VdomDict]

@overload
def For(component: EnumerateCallable, iterator: enumerate[Any]) -> VdomDict:
    ...

@overload
def For(component: ListCallable, iterator: list[Any]) -> VdomDict:
    ...


def For(component: Union[ListCallable, EnumerateCallable], iterator: Union[List[Any], enumerate[Any]]) -> VdomDict:
    if isinstance(iterator, enumerate):
        component = cast(EnumerateCallable, component)
        return html._(*[component(index, value) for index, value in iterator])
    else:
        component = cast(ListCallable, component)
        return html._(*[component(value) for value in iterator])
