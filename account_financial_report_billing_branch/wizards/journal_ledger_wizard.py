# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class JournalLedgerReportWizard(models.TransientModel):
    _inherit = "journal.ledger.report.wizard"

    billing_branch_ids = fields.Many2many(
        comodel_name="billing.branch",
    )

    def _prepare_report_journal_ledger(self):
        res = super()._prepare_report_journal_ledger()
        res.update({"billing_branch_ids": self.billing_branch_ids.ids or []})
        return res
