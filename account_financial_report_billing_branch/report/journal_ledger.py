# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class JournalLedgerReport(models.AbstractModel):
    _inherit = "report.account_financial_report.journal_ledger"

    def _get_report_values(self, docids, data):
        self = self.with_context(billing_branch_ids=data["billing_branch_ids"])
        return super()._get_report_values(docids, data)

    def _get_move_lines_domain(self, move_ids, wizard, journal_ids):
        domain = super()._get_move_lines_domain(move_ids, wizard, journal_ids)
        billing_branch_ids = self.env.context.get("billing_branch_ids", [])
        if billing_branch_ids:
            domain.append(("billing_branch_id", "in", billing_branch_ids))
        return domain
