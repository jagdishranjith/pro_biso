
from odoo import fields, models


class CrmTeam(models.Model):
    _inherit = "crm.team"

    billing_branch_id = fields.Many2one(
        "billing.branch",
        default=lambda self: self.env["res.users"]._get_default_billing_branch(),
        check_company=True,
    )
