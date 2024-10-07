# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Accounting Fincnaial Report Billing Branch",
    "summary": "Introduces Billing Branch (BB) in financial reports",
    "version": "17.0.1.0.0",
    "author": "Coding Crown",
    "website": "https://codingcrown.com",
    "category": "Accounting & Finance",
    "depends": ["account_financial_report", "account_billing_branch"],
    "license": "Other proprietary",
    "data": [
        "wizards/aged_partner_balance_wizard_view.xml",
        "wizards/general_ledger_wizard_view.xml",
        "wizards/journal_ledger_wizard_view.xml",
        "wizards/open_items_wizard_view.xml",
        "wizards/trial_balance_wizard_view.xml",
        "wizards/vat_report_wizard_view.xml",
    ],
}
