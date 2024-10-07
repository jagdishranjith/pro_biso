

from odoo import _, api, models
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # @api.constrains("billing_branch_id", "picking_type_id")
    # def _check_billing_branch_picking_type(self):
    #     for rec in self:
    #         if (
    #             rec.billing_branch_id
    #             and rec.billing_branch_id
    #             != rec.picking_type_id.warehouse_id.billing_branch_id
    #         ):
    #             raise UserError(
    #                 _(
    #                     "Configuration error. The Billing Branch in "
    #                     "the Purchase and Deliver To must be the same."
    #                 )
    #             )
