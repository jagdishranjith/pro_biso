# Copyright 2019 ForgeFlow S.L.
# Copyright 2019 Serpent Consulting Services Pvt. Ltd.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import _, api, fields, models
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = "stock.picking"

    operating_unit_id = fields.Many2one(
        comodel_name="operating.unit",
        string="Requesting Operating Unit",
        readonly=False,
        compute="_compute_operating_unit_id",
        store=True,
        check_company=False,
    )

    @api.depends("picking_type_id")
    def _compute_operating_unit_id(self):
        for picking in self:
            order = None
            if picking.picking_type_id.name == 'Delivery Orders':
                order = self.env['sale.order'].search([('name', '=', picking.origin)], limit=1)
            elif picking.picking_type_id.name == 'Receipts':
                order = self.env['purchase.order'].search([('name', '=', picking.origin)], limit=1)

            if order:
                # Assign operating unit from order's requesting_operating_unit_id or operating_unit_id
                picking.operating_unit_id = order.operating_unit_id
            else:
                # Log a warning if no matching order was found
                picking.operating_unit_id = False
                _logger.warning(f"No order found for picking {picking.name} with origin {picking.origin}")

                # warehouse = picking.picking_type_id.warehouse_id
                # picking.operating_unit_id = warehouse.operating_unit_id
                # picking.operating_unit_id = order.requesting_operating_unit_id or order.operating_unit_id



    # @api.constrains("operating_unit_id", "picking_type_id")
    # def _check_picking_type_operating_unit(self):
    #     for rec in self:
    #         warehouse = rec.picking_type_id.warehouse_id
    #         if (
    #             warehouse.operating_unit_id
    #             and rec.picking_type_id
    #             and rec.operating_unit_id
    #             and warehouse.operating_unit_id != rec.operating_unit_id
    #         ):
    #             raise UserError(
    #                 _(
    #                     "Configuration error. The Operating Unit of the picking "
    #                     "must be the same as that of the warehouse of the "
    #                     "Picking Type."
    #                 )
    #             )
