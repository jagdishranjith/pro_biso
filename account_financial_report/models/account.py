
from odoo import fields, models


class AccountAccount(models.Model):
    _inherit = "account.account"

    centralized = fields.Boolean(
        help="If flagged, no details will be displayed in "
        "the General Ledger report (the webkit one only), "
        "only centralized amounts per period.",
    )
