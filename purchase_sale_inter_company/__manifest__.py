

{
    "name": "Inter Company Module for Purchase to Sale Order",
    "summary": "Intercompany PO/SO rules",
    'version': '17.0.0.0.0',
    "category": "Purchase Management",
    "website": "https://github.com/OCA/multi-company",
    "author": "Coding Crown",
    "license": "Other proprietary",
    "installable": True,
    "depends": ["sale", "purchase_stock", "account_invoice_inter_company"],
    "data": [
        "views/res_config_view.xml",
        "views/purchase_order_view.xml"
    ],
}
