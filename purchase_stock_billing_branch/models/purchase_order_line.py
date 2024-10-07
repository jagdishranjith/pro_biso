

from odoo import models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def _prepare_stock_moves(self, picking):
        """Add billing branch from warehouse to picking"""
        picking.billing_branch_id = (
            picking.picking_type_id.warehouse_id.billing_branch_id
        )
        return super()._prepare_stock_moves(picking)
