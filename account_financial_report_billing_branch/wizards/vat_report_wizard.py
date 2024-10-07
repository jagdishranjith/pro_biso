

from odoo import fields, models


class VATReportWizard(models.TransientModel):
    _inherit = "vat.report.wizard"

    billing_branch_ids = fields.Many2many(
        comodel_name="billing.branch",
    )

    def _prepare_vat_report(self):
        res = super()._prepare_vat_report()
        res.update({"billing_branch_ids": self.billing_branch_ids.ids or []})
        return res
