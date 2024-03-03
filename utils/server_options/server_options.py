from typing import Any, List, Self

from pydantic import BaseModel, ValidationError, field_validator, ValidationInfo
from reactpy import html
from reactpy.core.types import VdomDict



class ServerOptions(BaseModel):
    """options to be passed to the web server

    Args:
        head (List[Any]): List of page header options, css, script, title, etc
        asset_root (str): root path for assets (static, assets, etc). Default 'assets'
        asset_folder (str): path to assets folder relative to application root

    """

    head: List[Any] = []
    asset_root: str = "assets"
    asset_folder: str = "assets"


    @field_validator("head")
    @classmethod
    def validate_head(cls, value: List[str | VdomDict], info: ValidationInfo) -> List[VdomDict]:
        vals: List[VdomDict] = []
        for v in value:
            if isinstance(v, str):
                if v.endswith(".css"):
                    link = html.link({"rel": "stylesheet", "href": v})
                    vals.append(link)
                elif v.endswith(".js"):
                    script = html.script({"src": v})
                    vals.append(script)
                else:
                    raise ValidationError("Invalid asset extension expected [.css|.js]")

            else:
                if v["tagName"] in ["link", "script", "meta", "title"]:
                    vals.append(v)
                else:
                    raise ValidationError(f"Type {v['tagName'] } cannot be included in header")

        return vals

    def __add__(self, other: Self):
        model = self.model_copy()
        model.head = model.head.copy() + other.head.copy()

        if model.asset_root != other.asset_root:
            model.asset_root = other.asset_root

        if model.asset_folder != other.asset_folder:
            model.asset_folder = other.asset_folder

        return model
