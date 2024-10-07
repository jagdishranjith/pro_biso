

from odoo import api, models


class IrRule(models.Model):
    _inherit = "ir.rule"

    @api.model
    def _eval_context(self):
        res = super()._eval_context()
        res.update(
            {
                "billing_branch_ids": self.env.user.billing_branches().ids,
                "billing_branch_id": self.env.user.default_billing_branch_id.id,
            }
        )
        return res
