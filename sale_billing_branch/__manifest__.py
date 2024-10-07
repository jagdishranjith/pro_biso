# © 2019 ForgeFlow S.L.
# - Jordi Ballester Alomar
# © 2019 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": "Billing Branch in Sales",
    "version": "17.0.1.0.0",
    "summary": "An billing branch (BB) is an organizational entity part of a "
    "company",
    "author": "Coding Crown",
    "license": "Other proprietary",
    "website": "https://codingcrown.com",
    "category": "Sales Management",
    "depends": ["sale", "account_billing_branch", "sales_team_billing_branch"],
    "data": [
        "security/sale_security.xml",
        "views/sale_view.xml",
        "views/sale_report_view.xml",
    ],
    "installable": True,
}
