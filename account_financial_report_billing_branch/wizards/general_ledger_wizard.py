

from odoo import fields, models


class GeneralLedgerReportWizard(models.TransientModel):
    _inherit = "general.ledger.report.wizard"

    billing_branch_ids = fields.Many2many(
        comodel_name="billing.branch",
    )

    def _prepare_report_general_ledger(self):
        res = super()._prepare_report_general_ledger()
        res.update({"billing_branch_ids": self.billing_branch_ids.ids or []})
        return res
