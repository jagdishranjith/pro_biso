

{
    "name": "Inter Company Module for Purchase to Sale Order with warehouse",
    "summary": "Intercompany PO/SO rules with warehouse",
    'version': '17.0.0.0.0',
    "category": "Purchase Management",
    "website": "https://github.com/OCA/multi-company",
    "author": "Coding Crown",
    "license": "Other proprietary",
    "installable": True,
    "auto_install": False,
    "depends": ["purchase_sale_inter_company", "sale_stock", "purchase_stock"],
    "data": ["views/res_config_view.xml"],
}
