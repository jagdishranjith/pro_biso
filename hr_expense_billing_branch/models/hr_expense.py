

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class HrExpenseExpense(models.Model):
    _inherit = "hr.expense"

    billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Billing Branch",
        default=lambda self: self.env["res.users"]._get_default_billing_branch(),
    )

    def action_submit_expenses(self):
        ctx = self._context.copy()
        billing_branch_id = self.mapped("billing_branch_id")
        if billing_branch_id and len(billing_branch_id) > 1:
            raise UserError(
                _(
                    "Configuration error. The Billing "
                    "Branch in the Expense sheet and in the "
                    "Expense must be the same."
                )
            )
        ctx.update({"default_billing_branch_id": billing_branch_id.id})
        return super(
            HrExpenseExpense, self.with_context(**ctx)
        ).action_submit_expenses()

    # @api.constrains("billing_branch_id", "company_id")
    # def _check_company_billing_branch(self):
    #     for rec in self:
    #         if (
    #             rec.company_id
    #             and rec.billing_branch_id
    #             and rec.company_id != rec.billing_branch_id.company_id
    #         ):
    #             raise ValidationError(
    #                 _(
    #                     "Configuration error. The Company in "
    #                     "the Expense and in the Billing "
    #                     "Branch must be the same."
    #                 )
    #             )

    @api.constrains("billing_branch_id", "sheet_id")
    def _check_expense_billing_branch(self):
        for rec in self:
            if (
                rec.sheet_id
                and rec.sheet_id.billing_branch_id
                and rec.billing_branch_id
                and rec.sheet_id.billing_branch_id != rec.billing_branch_id
            ):
                raise ValidationError(
                    _(
                        "Configuration error. The Billing "
                        "Branch in the Expense sheet and in the "
                        "Expense must be the same."
                    )
                )

    def _get_default_expense_sheet_values(self):
        sheets = super()._get_default_expense_sheet_values()
        if len(self.mapped("billing_branch_id")) != 1 or any(
            not expense.billing_branch_id for expense in self
        ):
            raise ValidationError(
                _(
                    "You cannot submit the Expenses having "
                    "different Billing Branchs or with "
                    "no Billing Branch"
                )
            )
        for sheet in sheets:
            sheet.update({"billing_branch_id": self.mapped("billing_branch_id").id})
        return sheets

    def _prepare_payments_vals(self):
        vals = super()._prepare_payments_vals()
        vals.update({
            'billing_branch_id': self.billing_branch_id.id,
            'company_id': self.company_id.id
        })
        return vals

    def _prepare_move_lines_vals(self):
        vals = super()._prepare_move_lines_vals()
        vals.update({
            'billing_branch_id': self.billing_branch_id.id,
            'company_id': self.company_id.id
        })
        return vals


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Billing Branch",
        default=lambda self: self.env["res.users"]._default_billing_branch(),
    )

    @api.onchange("billing_branch_id")
    def _onchange_billing_branch_id(self):
        if self.billing_branch_id:
            self.expense_line_ids.write(
                {"billing_branch_id": self.billing_branch_id.id}
            )

    def _prepare_move_vals(self):
        vals = super()._prepare_move_vals()
        vals.update({
            'billing_branch_id': self.billing_branch_id.id,
            'company_id': self.company_id.id
        })
        return vals

    def _prepare_bills_vals(self):
        vals = super()._prepare_bills_vals()
        vals.update({
            'billing_branch_id': self.billing_branch_id.id,
            'company_id': self.company_id.id
        })
        return vals

    # @api.constrains("billing_branch_id", "company_id")
    # def _check_company_billing_branch(self):
    #     for rec in self:
    #         if (
    #             rec.company_id
    #             and rec.billing_branch_id
    #             and rec.company_id != rec.billing_branch_id.company_id
    #         ):
    #             raise ValidationError(
    #                 _(
    #                     """Configuration error. The company in
    #             the Expense and in the Billing Branch must be the same"""
    #                 )
    #             )
