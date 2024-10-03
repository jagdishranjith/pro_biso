# Copyright 2016-19 ForgeFlow S.L.
# Copyright 2016-19 Serpent Consulting Services Pvt. Ltd.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).).

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class HrExpenseExpense(models.Model):
    _inherit = "hr.expense"

    operating_unit_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Billing Branch",
        default=lambda self: self.env["res.users"]._get_default_operating_unit(),
    )

    def action_submit_expenses(self):
        ctx = self._context.copy()
        operating_unit_id = self.mapped("operating_unit_id")
        if operating_unit_id and len(operating_unit_id) > 1:
            raise UserError(
                _(
                    "Configuration error. The Operating "
                    "Unit in the Expense sheet and in the "
                    "Expense must be the same."
                )
            )
        ctx.update({"default_operating_unit_id": operating_unit_id.id})
        return super(
            HrExpenseExpense, self.with_context(**ctx)
        ).action_submit_expenses()

    # @api.constrains("operating_unit_id", "company_id")
    # def _check_company_operating_unit(self):
    #     for rec in self:
    #         if (
    #             rec.company_id
    #             and rec.operating_unit_id
    #             and rec.company_id != rec.operating_unit_id.company_id
    #         ):
    #             raise ValidationError(
    #                 _(
    #                     "Configuration error. The Company in "
    #                     "the Expense and in the Operating "
    #                     "Unit must be the same."
    #                 )
    #             )

    @api.constrains("operating_unit_id", "sheet_id")
    def _check_expense_operating_unit(self):
        for rec in self:
            if (
                rec.sheet_id
                and rec.sheet_id.operating_unit_id
                and rec.operating_unit_id
                and rec.sheet_id.operating_unit_id != rec.operating_unit_id
            ):
                raise ValidationError(
                    _(
                        "Configuration error. The Operating "
                        "Unit in the Expense sheet and in the "
                        "Expense must be the same."
                    )
                )

    def _get_default_expense_sheet_values(self):
        sheets = super()._get_default_expense_sheet_values()
        if len(self.mapped("operating_unit_id")) != 1 or any(
            not expense.operating_unit_id for expense in self
        ):
            raise ValidationError(
                _(
                    "You cannot submit the Expenses having "
                    "different Operating Units or with "
                    "no Billing Branch"
                )
            )
        for sheet in sheets:
            sheet.update({"operating_unit_id": self.mapped("operating_unit_id").id})
        return sheets

    def _prepare_payments_vals(self):
        vals = super()._prepare_payments_vals()
        vals.update({
            'operating_unit_id': self.operating_unit_id.id,
            'company_id': self.company_id.id
        })
        return vals

    def _prepare_move_lines_vals(self):
        vals = super()._prepare_move_lines_vals()
        vals.update({
            'operating_unit_id': self.operating_unit_id.id,
            'company_id': self.company_id.id
        })
        return vals


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    operating_unit_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Billing Branch",
        default=lambda self: self.env["res.users"].operating_unit_default_get(),
    )

    @api.onchange("operating_unit_id")
    def _onchange_operating_unit_id(self):
        if self.operating_unit_id:
            self.expense_line_ids.write(
                {"operating_unit_id": self.operating_unit_id.id}
            )

    def _prepare_move_vals(self):
        vals = super()._prepare_move_vals()
        vals.update({
            'operating_unit_id': self.operating_unit_id.id,
            'company_id': self.company_id.id
        })
        return vals

    def _prepare_bills_vals(self):
        vals = super()._prepare_bills_vals()
        vals.update({
            'operating_unit_id': self.operating_unit_id.id,
            'company_id': self.company_id.id
        })
        return vals

    # @api.constrains("operating_unit_id", "company_id")
    # def _check_company_operating_unit(self):
    #     for rec in self:
    #         if (
    #             rec.company_id
    #             and rec.operating_unit_id
    #             and rec.company_id != rec.operating_unit_id.company_id
    #         ):
    #             raise ValidationError(
    #                 _(
    #                     """Configuration error. The company in
    #             the Expense and in the Operating Unit must be the same"""
    #                 )
    #             )
