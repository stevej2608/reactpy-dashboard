from reactpy import component, html
from reactpy_utils import DocumentTitle

from .components import Breadcrumbs, PageTitle, TopPanel
from .components.icon import Icon_Gear, Icon_Bin, Icon_Info, Icon_Dots
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
                        TableTool(Icon_Gear),
                        TableTool(Icon_Bin),
                        TableTool(Icon_Info),
                        TableTool(Icon_Dots),
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