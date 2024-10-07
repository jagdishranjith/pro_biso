
from odoo import fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    billing_branch_id = fields.Many2one(
        related="location_id.billing_branch_id",
        store=True,
        check_company=True,
    )
