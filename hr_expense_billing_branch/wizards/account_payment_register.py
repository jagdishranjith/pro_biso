

from odoo import models


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    def _get_reconciled_moves(self, payment):
        expenses = payment.move_id.line_ids.mapped("expense_id")
        return (
            expenses.mapped("sheet_id.account_move_id")
            if expenses
            else super()._get_reconciled_moves(payment)
        )
