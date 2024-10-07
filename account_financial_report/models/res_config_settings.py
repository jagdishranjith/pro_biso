

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    default_age_partner_config_id = fields.Many2one(
        "account.age.report.configuration",
        string="Intervals configuration",
        default_model="aged.partner.balance.report.wizard",
    )
