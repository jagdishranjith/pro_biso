

from odoo import fields, models


class StockRule(models.Model):
    _inherit = "stock.rule"

    billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
        related="warehouse_id.billing_branch_id",
        check_company=True,
    )
