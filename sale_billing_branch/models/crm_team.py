# © 2019 ForgeFlow S.L.
# - Jordi Ballester Alomar
# © 2019 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import SUPERUSER_ID, _, api, models
from odoo.exceptions import ValidationError


class CrmTeam(models.Model):
    _inherit = "crm.team"

    @api.constrains("billing_branch_id")
    def _check_sales_order_billing_branch(self):
        for rec in self:
            orders = (
                self.with_user(SUPERUSER_ID)
                .env["sale.order"]
                .search(
                    [
                        ("team_id", "=", rec.id),
                        ("billing_branch_id", "!=", rec.billing_branch_id.id),
                    ]
                )
            )
            if orders:
                raise ValidationError(
                    _(
                        "Configuration error. It is not "
                        "possible to change this "
                        "team. There are sale orders "
                        "referencing it in other billing "
                        "branch"
                    )
                )
