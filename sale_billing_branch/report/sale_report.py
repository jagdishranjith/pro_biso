

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    billing_branch_id = fields.Many2one("billing.branch", "Billing Branch")

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """, s.billing_branch_id"""
        return res

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res["billing_branch_id"] = "s.billing_branch_id"
        return res
