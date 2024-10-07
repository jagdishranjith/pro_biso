

from odoo import fields, models


class InterCompanyRulesConfig(models.TransientModel):
    _inherit = "res.config.settings"

    so_from_po = fields.Boolean(
        related="company_id.so_from_po",
        string="Create Sale Orders when buying to this company",
        help="Generate a Sale Order when a Purchase Order with this company "
        "as supplier is created.\n The intercompany user must at least be "
        "Sale User.",
        readonly=False,
    )
    sale_auto_validation = fields.Boolean(
        related="company_id.sale_auto_validation",
        string="Sale Orders Auto Validation",
        help="When a Sale Order is created by a multi company rule for "
        "this company, it will automatically validate it.",
        readonly=False,
    )
    intercompany_sale_user_id = fields.Many2one(
        comodel_name="res.users",
        related="company_id.intercompany_sale_user_id",
        string="Intercompany Sale User",
        help="User used to create the sales order arising from a purchase "
        "order in another company.",
        readonly=False,
    )
