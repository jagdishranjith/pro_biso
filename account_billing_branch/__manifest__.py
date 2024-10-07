# © 2019 ForgeFlow S.L.
# © 2019 Serpent Consulting Services Pvt. Ltd.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": "Accounting with Billing Branchs",
    "summary": "Introduces Billing Branch (BB) in invoices and "
    "Accounting Entries with clearing account",
    "version": "17.0.1.0.0",
    "author": "Coding Crown",
    "website": "https://codingcrown.com",
    "category": "Accounting & Finance",
    "depends": [
        "account",
        "analytic_billing_branch",
        "base_view_inheritance_extension",
    ],
    "license": "Other proprietary",
    "data": [
        "security/account_security.xml",
        "views/account_move_view.xml",
        "views/account_journal_view.xml",
        "views/company_view.xml",
        "views/account_payment_view.xml",
        "views/account_invoice_report_view.xml",
    ],
}
