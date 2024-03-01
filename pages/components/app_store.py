from typing import cast, Any, Callable
from pydantic import BaseModel
from reactpy import create_context


class UserSettings(BaseModel):
    dark_mode: bool = False

class AppState:

    @property
    def dark_mode(self) -> bool:
        return self.settings.dark_mode

    def __init__(self, settings: UserSettings, set_settings: Callable[[UserSettings], None]):
        self.settings = settings
        self.set_settings = set_settings


    def update(self, **kwargs:Any):
        new_settings = self.settings.model_copy(update=kwargs)
        self.set_settings(new_settings)


    def toggle_dark_mode(self):
        self.update(dark_mode = not self.settings.dark_mode)


AppContext = create_context(cast(AppState, None))
