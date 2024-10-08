# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    invoice_auto_validation = fields.Boolean(
        related="company_id.invoice_auto_validation",
        string="Invoices Auto Validation",
        readonly=False,
        help="When an invoice is created by a multi company rule for "
        "this company, it will automatically validate it.",
    )
    intercompany_invoice_user_id = fields.Many2one(
        related="company_id.intercompany_invoice_user_id",
        readonly=False,
        help="Responsible user for creation of invoices triggered by "
        "intercompany rules. If not set the user initiating the"
        "transaction will be used",
    )
