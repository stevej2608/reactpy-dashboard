from typing import  Any, Dict

def var_name(obj: Any, namespace: Dict[str, Any]) -> str:
    """Return var name as a string

    Args:
        obj (Any): Variable to be named
        namespace (Dict[str, Any]): _description_

    Returns:
        str: The objects name

    Usage:
    ```
        from utils.var_name import var_name
        
        app = FastAPI(...)

        app_name = var_name(app, globals())
    ```
    """
    return [name for name in namespace if namespace[name] is obj][0]
