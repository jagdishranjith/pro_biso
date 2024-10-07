

from odoo import fields, models


class OpenItemsReportWizard(models.TransientModel):
    _inherit = "open.items.report.wizard"

    billing_branch_ids = fields.Many2many(
        comodel_name="billing.branch",
    )

    def _prepare_report_open_items(self):
        res = super()._prepare_report_open_items()
        res.update({"billing_branch_ids": self.billing_branch_ids.ids or []})
        return res
