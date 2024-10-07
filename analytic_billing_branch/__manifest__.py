
{
    "name": "Analytic Billing Branch",
    "version": "17.0.1.0.0",
    "author": "Coding Crown",
    "license": "Other proprietary",
    "website": "https://codingcrown.com",
    "category": "Sales",
    "depends": ["analytic", "billing_branch"],
    "data": [
        "security/analytic_account_security.xml",
        "views/analytic_account_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "analytic_billing_branch/static/src/components/analytic_distribution.esm.js",
        ],
    },
    "installable": True,
}
