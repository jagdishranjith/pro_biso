
from odoo import _, api, fields, models
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = "stock.picking"

    billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Billing Branch",
        readonly=False,
        # compute="_compute_billing_branch_id",
        store=True,
        check_company=False,
    )

    # @api.depends("picking_type_id")
    # def _compute_billing_branch_id(self):
    #     for picking in self:
    #         order = None
    #         if picking.picking_type_id.name == 'Delivery Orders':
    #             order = self.env['sale.order'].search([('name', '=', picking.origin)], limit=1)
    #         elif picking.picking_type_id.name == 'Receipts':
    #             order = self.env['purchase.order'].search([('name', '=', picking.origin)], limit=1)
    #
    #         if order:
    #             # Assign billing branch from order's requesting_billing_branch_id or billing_branch_id
    #             picking.billing_branch_id = order.billing_branch_id
    #         else:
    #             # Log a warning if no matching order was found
    #             picking.billing_branch_id = False
    #             _logger.warning(f"No order found for picking {picking.name} with origin {picking.origin}")

                # warehouse = picking.picking_type_id.warehouse_id
                # picking.billing_branch_id = warehouse.billing_branch_id
                # picking.billing_branch_id = order.requesting_billing_branch_id or order.billing_branch_id



    # @api.constrains("billing_branch_id", "picking_type_id")
    # def _check_picking_type_billing_branch(self):
    #     for rec in self:
    #         warehouse = rec.picking_type_id.warehouse_id
    #         if (
    #             warehouse.billing_branch_id
    #             and rec.picking_type_id
    #             and rec.billing_branch_id
    #             and warehouse.billing_branch_id != rec.billing_branch_id
    #         ):
    #             raise UserError(
    #                 _(
    #                     "Configuration error. The Billing Branch of the picking "
    #                     "must be the same as that of the warehouse of the "
    #                     "Picking Type."
    #                 )
    #             )
