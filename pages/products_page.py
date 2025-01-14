from reactpy import component, html

from reactpy_utils import DocumentTitle

from .components import Breadcrumbs, PageTitle, TopPanel
from .components.icon import Icon_Gear, Icon_Bin, Icon_Info, Icon_Dots
from .components.table_tools import TableTools, AddButton, ToolsGroup, TableToolContainer, BreadcrumbsAndTitle, TableTool, SimpleTableSearch
from .products import ProductsTable

@component
def ProductsPage():

    table = ProductsTable()

    return html.main(
        DocumentTitle("Products - reactpy"),
        TopPanel(
            BreadcrumbsAndTitle(
                Breadcrumbs(crumbs=['E-commerce', 'Products']),
                PageTitle(title="All Products")
            ),
            TableTools(
                SimpleTableSearch(search=table.search, placeholder="Search for products"),
                ToolsGroup(
                    TableToolContainer(
                        TableTool(Icon_Gear),
                        TableTool(Icon_Bin),
                        TableTool(Icon_Info),
                        TableTool(Icon_Dots),
                    ),
                    AddButton("Add Product")
                )
            )
        ),
        table
    )
