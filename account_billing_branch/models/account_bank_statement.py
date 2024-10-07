
from odoo import models


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    def _prepare_move_line_default_vals(self, counterpart_account_id=None):
        result = super()._prepare_move_line_default_vals(
            counterpart_account_id=counterpart_account_id
        )
        result[0][
            "billing_branch_id"
        ] = self.statement_id.journal_id.billing_branch_id.id
        result[1][
            "billing_branch_id"
        ] = self.statement_id.journal_id.billing_branch_id.id
        return result
