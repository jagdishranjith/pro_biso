

{
    "name": "Billing Branch in Purchase Orders",
    "summary": "Adds the concecpt of billing branch (BB) in purchase order "
    "management",
    "version": "17.0.1.2.0",
    "author": "Coding Crown",
    "website": "https://codingcrown.com",
    "category": "Purchase Management",
    "depends": ["purchase", "account_billing_branch"],
    "license": "Other proprietary",
    "data": [
        "security/purchase_security.xml",
        "report/purchase_report_view.xml",
        "views/purchase_order_view.xml",
        "views/purchase_order_line_view.xml",
        "views/account_move_view.xml",
    ],
    "demo": ["demo/purchase_order_demo.xml"],
    "installable": True,
}
