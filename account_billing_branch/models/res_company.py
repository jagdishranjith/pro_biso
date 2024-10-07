

from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class ResCompany(models.Model):
    _inherit = "res.company"

    inter_ou_clearing_account_id = fields.Many2one(
        comodel_name="account.account",
        string="Inter-billing branch clearing account",
    )
    ou_is_self_balanced = fields.Boolean(
        string="Billing Branchs are self-balanced",
        help="Activate if your company is "
        "required to generate a balanced"
        " balance sheet for each "
        "billing branch.",
    )

    @api.constrains("ou_is_self_balanced", "inter_ou_clearing_account_id")
    def _inter_ou_clearing_acc_required(self):
        for rec in self:
            if rec.ou_is_self_balanced and not rec.inter_ou_clearing_account_id:
                raise UserError(
                    _(
                        "Configuration error. Please provide an "
                        "Inter-billing branch clearing account."
                    )
                )
