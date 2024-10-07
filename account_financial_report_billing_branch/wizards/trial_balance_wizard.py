

from odoo import fields, models


class TrialBalanceReportWizard(models.TransientModel):
    _inherit = "trial.balance.report.wizard"

    billing_branch_ids = fields.Many2many(
        comodel_name="billing.branch",
    )

    def _prepare_report_trial_balance(self):
        res = super()._prepare_report_trial_balance()
        res.update({"billing_branch_ids": self.billing_branch_ids.ids or []})
        return res
