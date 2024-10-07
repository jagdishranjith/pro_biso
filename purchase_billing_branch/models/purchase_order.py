
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # READONLY_STATES = {
    #     "purchase": [("readonly", True)],
    #     "done": [("readonly", True)],
    #     "cancel": [("readonly", True)],
    # }

    billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Billing Branch",
        # states=READONLY_STATES,
        default=lambda self: (
            self.env["res.users"]._get_default_billing_branch(self.env.uid)
        ),
    )

    requesting_billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Requesting Billing Branch",
        # states=READONLY_STATES,
        default=lambda self: (
            self.env["res.users"]._get_default_billing_branch(self.env.uid)
        ),
    )

    # @api.constrains("billing_branch_id", "company_id")
    # def _check_company_billing_branch(self):
    #     for record in self:
    #         if (
    #             record.company_id
    #             and record.billing_branch_id
    #             and record.company_id != record.billing_branch_id.company_id
    #         ):
    #             raise ValidationError(
    #                 _(
    #                     "Configuration error. The Company in the Purchase Order "
    #                     "and in the Billing Branch must be the same."
    #                 )
    #             )

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals["billing_branch_id"] = self.billing_branch_id.id
        return invoice_vals


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    billing_branch_id = fields.Many2one(
        related="order_id.billing_branch_id", string="Billing Branch"
    )
