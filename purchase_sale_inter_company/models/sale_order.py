

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    auto_purchase_order_id = fields.Many2one(
        comodel_name="purchase.order",
        string="Source Purchase Order",
        readonly=True,
        copy=False,
    )

    def action_confirm(self):
        for order in self.filtered("auto_purchase_order_id"):
            for line in order.order_line.sudo():
                if line.auto_purchase_line_id:
                    line.auto_purchase_line_id.price_unit = line.price_unit
        return super().action_confirm()
