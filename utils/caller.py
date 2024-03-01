import os
import inspect
from pathlib import Path

def calling_module_folder(depth:int=1) -> str:
    """Returns the folder path relative to program root of the calling module

    Args:
        depth (int, optional): The distance down the stack, default=1 (parent).

    Returns:
        str: _description_
    """
    return str(Path(inspect.stack()[depth+1].filename).parent.relative_to(os.getcwd()))
