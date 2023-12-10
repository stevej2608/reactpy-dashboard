from reactpy import component, html

from .components import Breadcrumbs, PageTitle, TopPanel
from .components.icon import Icon_Gear, Icon_Bin, Icon_Info, Icon_Dots
from .components.table_tools import TableTools, AddButton, ToolsGroup, ButtonContainer, BreadcrumbsAndTitle, TableTool, TableSearch
from .products import ProductsTable

@component
def ProductsPage():
    return html.main(
        TopPanel(
            BreadcrumbsAndTitle(
                Breadcrumbs(crumbs=['E-commerce', 'Products']),
                PageTitle(title="All Products")
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
        ProductsTable()
    )
