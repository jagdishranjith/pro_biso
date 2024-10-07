
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = "account.move"

    purchase_ou_domain = fields.Many2many(
        comodel_name="purchase.order", compute="_compute_purchase_ou_domain"
    )

    # Load all unsold PO lines
    @api.onchange("purchase_vendor_bill_id", "purchase_id")
    def _onchange_purchase_auto_complete(self):
        """
        Override to add Billing Branch from Purchase Order to Invoice.
        """
        purchase_id = self.purchase_id
        if self.purchase_vendor_bill_id.purchase_order_id:
            purchase_id = self.purchase_vendor_bill_id.purchase_order_id
        if purchase_id and purchase_id.billing_branch_id:
            # Assign OU from PO to Invoice
            self.billing_branch_id = purchase_id.billing_branch_id.id
        return super()._onchange_purchase_auto_complete()

    @api.depends("billing_branch_id")
    def _compute_purchase_ou_domain(self):
        for rec in self:
            rec.purchase_ou_domain = (
                self.env["purchase.order"]
                .sudo()
                .search([("billing_branch_id", "=", rec.billing_branch_id.id)])
            )


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.constrains("billing_branch_id", "purchase_line_id")
    def _check_invoice_ou(self):
        for line in self:
            if (
                line.purchase_line_id
                and line.billing_branch_id != line.purchase_line_id.billing_branch_id
            ):
                raise ValidationError(
                    _(
                        "The billing branch of the purchase order must "
                        "be the same as in the associated invoices."
                    )
                )
