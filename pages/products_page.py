from reactpy import component, html

from .components import Breadcrumbs, PageTitle, TopPanel
from .components.table_tools import TableTools, AddButton, ToolsGroup, ButtonContainer
from .components.icon import Icon_Gear, Icon_Bin, Icon_Info, Icon_Dots
from .products import ProductsTable, AddProductModal, EditProductModal, DeleteProductModal


@component
def Tool(icon):
    return html.a({'href': '#', 'class_name': 'text-gray-500 hover:text-gray-900 cursor-pointer p-1 hover:bg-gray-100 rounded inline-flex justify-center'},
        icon()
    )


@component
def TableSearch():
    return html.form({'class_name': 'sm:pr-3 mb-4 sm:mb-0', 'action': '#', 'method': 'GET'},
        html.label({'html_for': 'products-search', 'class_name': 'sr-only'}, "Search"),
        html.div({'class_name': 'mt-1 relative sm:w-64 xl:w-96'},
            html.input({'type': 'text', 'name': 'email', 'id': 'products-search', 'class_name': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5', 'placeholder': 'Search for products'})
        )
    )


@component
def Products():
    return html.main(
        TopPanel(
            TopPanel(
                Breadcrumbs(crumbs=['E-commerce', 'Products']),
                PageTitle(title="All Products")
            ),
            TableTools(
                TableSearch(),
                ToolsGroup(
                    ButtonContainer(
                        Tool(Icon_Gear),
                        Tool(Icon_Bin),
                        Tool(Icon_Info),
                        Tool(Icon_Dots),
                    ),
                    AddButton("Add Product")
                )
            )
        ),
        ProductsTable(),
    )
