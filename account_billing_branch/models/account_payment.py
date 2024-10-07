# © 2019 ForgeFlow S.L.
# © 2019 Serpent Consulting Services Pvt. Ltd.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    billing_branch_id = fields.Many2one(
        check_company=True,
        comodel_name="billing.branch",
        compute="_compute_billing_branch_id",
        store=True,
    )

    # @api.depends("journal_id")
    # def _compute_billing_branch_id(self):
    #     for payment in self.filtered("journal_id"):
    #         payment.billing_branch_id = payment.journal_id.billing_branch_id

    def _prepare_move_line_default_vals(
        self, write_off_line_vals=None, force_balance=None
    ):
        lines = super()._prepare_move_line_default_vals(
            write_off_line_vals, force_balance
        )
        for line in lines:
            line["billing_branch_id"] = self.billing_branch_id.id
        active_model = self._context.get("active_model", False)
        if not active_model or active_model != "account.move":
            return lines
        invoices = self.env[self._context.get("active_model")].browse(
            self._context.get("active_ids")
        )
        invoices_ou = invoices.billing_branch_id
        if invoices and len(invoices_ou) == 1 and invoices_ou != self.billing_branch_id:
            destination_account_id = self.destination_account_id.id
            for line in lines:
                if not line.get("billing_branch_id", False) or (
                    line["account_id"] == destination_account_id
                ):
                    line["billing_branch_id"] = invoices_ou.id
        return lines

class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
    )

    def default_get(self, fields):
        result = super(AccountPaymentRegister, self).default_get(fields)
        billing_branch_id = self.env.context.get('billing_branch_id')

        if billing_branch_id:
            result['billing_branch_id'] = billing_branch_id

        return result

    def _create_payment_vals_from_batch(self, batch_result):
        vals = super()._create_payment_vals_from_batch(batch_result)
        vals.update({
            "billing_branch_id": self.billing_branch_id.id if self.billing_branch_id else False
        })
        return vals

    def _create_payment_vals_from_wizard(self, batch_result):
        vals = super()._create_payment_vals_from_wizard(batch_result)
        vals.update({
            "billing_branch_id": self.billing_branch_id.id if self.billing_branch_id else False
        })
        return vals
