
from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _get_new_picking_values(self):
        """
        Override to add Billing Branchs to Picking.
        """
        values = super()._get_new_picking_values()

        values.update(
            {
                "billing_branch_id": self.sale_line_id.billing_branch_id.id
                or self.billing_branch_id.id
            }
        )

        return values
