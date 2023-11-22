from typing import Dict, Any
import inspect

def props(include:str='', exclude:str='') -> Dict[str, Any]:
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
