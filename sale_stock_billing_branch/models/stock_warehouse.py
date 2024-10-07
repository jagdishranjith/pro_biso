
from odoo import _, api, models
from odoo.exceptions import ValidationError


class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    @api.constrains("billing_branch_id")
    def _check_existing_so_in_wh(self):
        for rec in self:
            sales = self.env["sale.order"].search(
                [
                    ("warehouse_id", "=", rec.id),
                    ("billing_branch_id", "!=", rec.billing_branch_id.id),
                ],
                limit=1,
            )
            if sales:
                raise ValidationError(
                    _(
                        "Sales Order records already exist(s) for this warehouse"
                        " and billing branch."
                    )
                )
