

from odoo import fields, models


class AgedPartnerBalanceWizard(models.TransientModel):
    _inherit = "aged.partner.balance.report.wizard"

    billing_branch_ids = fields.Many2many(
        comodel_name="billing.branch",
    )

    def _prepare_report_aged_partner_balance(self):
        res = super()._prepare_report_aged_partner_balance()
        res.update({"billing_branch_ids": self.billing_branch_ids.ids or []})
        return res
