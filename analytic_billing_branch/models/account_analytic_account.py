
from odoo import fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    billing_branch_ids = fields.Many2many(
        comodel_name="billing.branch",
        string="Billing Branch",
        check_company=True,
    )
