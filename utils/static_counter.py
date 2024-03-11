from typing import Callable, Any, TypeVar

# pylint: disable=E1101

T = TypeVar("T")


def static_vars(**kwargs: Any) -> Callable[[T], T]:
    def decorate(func: T) -> T:
        for k, v in kwargs.items():
            setattr(func, k, v)
        return func

    return decorate


@static_vars(counter=0)
def id() -> int:
    id.counter += 1 # type: ignore
    return id.counter # type: ignore
