from reactpy import component, html
from reactpy_utils import DocumentTitle

from .components import Breadcrumbs, PageTitle, TopPanel
from .components.icon import ICON
from .components.table_tools import TableTools, AddButton, ExportButton, ToolsGroup, TableToolContainer, ButtonContainer, BreadcrumbsAndTitle, TableTool, SimpleTableSearch
from .users import UsersTable

@component
def UsersPage():

    table = UsersTable()

    return html.main(
        DocumentTitle("Users - reactpy"),
        TopPanel(
            BreadcrumbsAndTitle(
                Breadcrumbs(crumbs=['Users', 'List']),
                PageTitle(title="All Users")
            ),
            TableTools(
                SimpleTableSearch(search=table.search, placeholder="Search for users"),
                ToolsGroup(
                    TableToolContainer(
                        TableTool(ICON.Gear),
                        TableTool(ICON.Bin),
                        TableTool(ICON.Info),
                        TableTool(ICON.Dots),
                    ),
                    ButtonContainer(
                        AddButton("Add User"),
                        ExportButton()
                    )
                )
            )
        ),
        table
    )