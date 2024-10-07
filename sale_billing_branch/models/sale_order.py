# © 2019 ForgeFlow S.L.
# - Jordi Ballester Alomar
# © 2019 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Billing Branch",
        readonly=False,
        store=True,
        check_company=True,
        default=lambda self: self._default_billing_branch()
    )

    @api.model
    def _default_billing_branch(self):
        return self.env["res.users"]._get_default_billing_branch(self.env.user.id)

    # @api.depends("team_id")
    # def _compute_billing_branch_id(self):
    #     for sale in self:
    #         if sale.team_id:
    #             sale.billing_branch_id = sale.team_id.billing_branch_id

    # @api.depends("partner_id", "user_id", "billing_branch_id")
    # def _compute_team_id(self):
    #     res = super()._compute_team_id()
    #     for order in self:
    #         if (
    #             order.team_id
    #             and order.team_id.billing_branch_id != order.billing_branch_id
    #         ):
    #             order.team_id = False
    #     return res

    @api.depends("billing_branch_id")
    def _compute_journal_id(self):
        res = super()._compute_journal_id()
        for sale in self:
            if not sale.journal_id or (
                sale.journal_id
                and sale.billing_branch_id
                and sale.journal_id.billing_branch_id != sale.billing_branch_id
            ):
                sale.journal_id = (
                    self.env["account.journal"]
                    .search(
                        [
                            "|",
                            ("billing_branch_id", "=", sale.billing_branch_id.id),
                            ("billing_branch_id", "=", False),
                            "|",
                            ("company_id", "=", sale.company_id.id),
                            ("company_id", "=", False),
                            ("type", "=", "sale"),
                        ],
                        limit=1,
                    )
                    .id
                )
        return res

    # @api.constrains("team_id", "billing_branch_id")
    # def _check_team_billing_branch(self):
    #     for rec in self:
    #         if rec.team_id and rec.team_id.billing_branch_id != rec.billing_branch_id:
    #             raise ValidationError(
    #                 _(
    #                     "Configuration error. The Billing "
    #                     "Branch of the sales team must match "
    #                     "with that of the quote/sales order."
    #                 )
    #             )

    def _prepare_invoice(self):
        self.ensure_one()
        invoice_vals = super()._prepare_invoice()
        invoice_vals["billing_branch_id"] = self.billing_branch_id.id
        return invoice_vals


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    billing_branch_id = fields.Many2one(
        related="order_id.billing_branch_id",
        string="Billing Branch",
        store=True,
    )
