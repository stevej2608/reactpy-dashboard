from typing import cast
from pydantic import BaseModel
from reactpy import create_context



class UserSettings(BaseModel):
    dark_mode = False


class UserState:

    @property
    def dark_mode(self) -> bool:
        return self._settings.dark_mode

    def __init__(self, settings, set_settings):
        self._settings = settings
        self._set_settings = set_settings


    def update(self, **kwargs):
        new = self._settings.copy(update=kwargs)
        self._set_settings(new)


    def toggle_dark_mode(self):
        self.update(dark_mode = not self._settings.dark_mode)


SettingsContext = create_context(cast(UserState, None))
