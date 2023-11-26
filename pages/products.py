from reactpy import component, html

from .components import Breadcrumbs, PageTitle, TopPanel
from .table import TableTools, AddButton
from .products import ProductsTable, AddProductModal, EditProductModal, DeleteProductModal

@component
def Products():
    return html.main(
        TopPanel(
            Breadcrumbs(crumbs=['Products']),
            PageTitle(title="All Products"),
            TableTools(
                AddButton("Add Product")
            )
        ),
        ProductsTable(),
        AddProductModal(),
        EditProductModal(),
        DeleteProductModal()
    )
