

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Billing Branch",
    )

    def _select(self):
        select_str = super()._select()
        select_str += """
            ,line.billing_branch_id
        """
        return select_str
