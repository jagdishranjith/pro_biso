
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class StockMove(models.Model):
    _inherit = "stock.move"

    billing_branch_id = fields.Many2one(
        related="location_id.billing_branch_id",
        string="Billing Branch",
        check_company=True,
    )
    billing_branch_dest_id = fields.Many2one(
        related="location_dest_id.billing_branch_id",
        string="Billing Branch",
        check_company=True,
    )

    @api.constrains("picking_id", "location_id", "location_dest_id")
    def _check_stock_move_billing_branch(self):
        for stock_move in self:
            ou_pick = stock_move.picking_id.billing_branch_id or False
            ou_src = stock_move.billing_branch_id or False
            ou_dest = stock_move.billing_branch_dest_id or False
            if ou_src and ou_pick and (ou_src != ou_pick) and (ou_dest != ou_pick):
                raise UserError(
                    _(
                        "Configuration error. The Stock moves must "
                        "be related to a location (source or destination) "
                        "that belongs to the requesting Billing Branch."
                    )
                )
