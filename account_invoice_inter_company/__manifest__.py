

{
    "name": "Inter Company Invoices",
    "summary": "Intercompany invoice rules",
    "version": "17.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://github.com/OCA/multi-company",
    "author": "Coding Crown",
    "license": "Other proprietary",
    "depends": ["account", "base_setup"],
    "data": [
        "views/account_move_views.xml",
        "views/res_config_settings_view.xml",
    ],
    "demo": [
        "demo/inter_company_demo.xml",
    ],
    "installable": True,
}
