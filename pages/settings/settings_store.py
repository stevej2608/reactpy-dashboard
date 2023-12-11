from typing import cast
from pydantic import BaseModel
from reactpy import use_state, create_context

from utils.logger import log


class UserSettings(BaseModel):
    dark_mode = False


class UserState:

    @property
    def dark_mode(self) -> bool:
        log.info('dark_mode=%s', self._settings.dark_mode)
        return self._settings.dark_mode

    def __init__(self, settings, set_settings):
        log.info('UserState(settings [%s])', settings)
        self._settings = settings
        self._set_settings = set_settings


    def update(self, **kwargs):
        new = self._settings.copy(update=kwargs)
        log.info('update new = [%s]', new)
        self._set_settings(new)


    def toggle_dark_mode(self):
        self.update(dark_mode = not self._settings.dark_mode)


SettingsContext = create_context(cast(UserState, None))

# ./solidjs-dashboard/src/settings/settings.ts



# settings, set_settings = use_state(UserSettings())
