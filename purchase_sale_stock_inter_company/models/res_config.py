

from odoo import fields, models


class InterCompanyRulesConfig(models.TransientModel):

    _inherit = "res.config.settings"

    warehouse_id = fields.Many2one(
        comodel_name="stock.warehouse",
        related="company_id.warehouse_id",
        string="Warehouse for Sale Orders",
        help="Default value to set on Sale Orders that will be created "
        "based on Purchase Orders made to this company.",
        readonly=False,
    )
