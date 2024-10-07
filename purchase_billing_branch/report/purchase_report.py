

from odoo import fields, models


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Billing Branch",
        readonly=True,
    )

    def _select(self):
        select_str = super()._select()
        select_str += """, po.billing_branch_id"""
        return select_str

    def _group_by(self):
        group_by_str = super()._group_by()
        group_by_str += """, po.billing_branch_id"""
        return group_by_str
