from reactpy import component, html

from .components import Breadcrumbs, PageTitle, TopPanel
from .components.icon import Icon_Gear, Icon_Bin, Icon_Info, Icon_Dots
from .components.table_tools import TableTools, AddButton, ToolsGroup, ButtonContainer, BreadcrumbsAndTitle, TableTool, TableSearch
from .users import UsersTable

@component
def UsersPage():
    return html.main(
        TopPanel(
            BreadcrumbsAndTitle(
                Breadcrumbs(crumbs=['Users', 'List']),
                PageTitle(title="All Users")
            ),
            TableTools(
                TableSearch(),
                ToolsGroup(
                    ButtonContainer(
                        TableTool(Icon_Gear),
                        TableTool(Icon_Bin),
                        TableTool(Icon_Info),
                        TableTool(Icon_Dots),
                    ),
                    AddButton("Add Product")
                )
            )
        ),
        UsersTable()
    )