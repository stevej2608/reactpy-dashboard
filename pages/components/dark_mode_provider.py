from reactpy import component, html, use_context
from reactpy.types import VdomChildren
from reactpy_utils import LocalStorageAgent

from .app_store import AppContext


@component
def DarkModeProvider(children: VdomChildren):
    context, _ = use_context(AppContext)

    mode = "dark" if context.dark_mode else "light"
    return html.div({"class_name": mode},
        LocalStorageAgent(ctx=AppContext, storage_key="app-context"),
        children
        )
