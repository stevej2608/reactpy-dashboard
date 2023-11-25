from typing import Dict, Any
import inspect


def props(include:str='', exclude:str='') -> Dict[str, Any]:
    """Convert the caller functions arguments into a props dict

    Args:
        include (str, optional): Arguments to include in the returned props. Defaults to ''.
        exclude (str, optional): Arguments to exclude from the returned props. Defaults to ''.

    Returns:
        Dict[str, Any]: The props
    """

    frame = inspect.currentframe().f_back

    all_args = frame.f_locals.copy()
    _props = {}

    for name, value in all_args.items():
        if include=='' or name in include and value is not None:
            _props[name] = value

    if exclude:
        for name in list(_props):
            if name in exclude :
                _props.pop(name)

    return _props
