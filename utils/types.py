from typing import Dict, Any, Callable

EventArgs = Dict[str, Any]

Action = Callable[..., None]

Props = Dict[str, Any]

def NO_PROPS() -> Dict[str, Any]:
    return {}

PropsFunc = Callable[...,Dict[str, Any]]
