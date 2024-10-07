
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class StockLocation(models.Model):
    _inherit = "stock.location"

    billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Billing Branch",
        check_company=True,
    )

    @api.constrains("billing_branch_id")
    def _check_warehouse_billing_branch(self):
        for rec in self:
            warehouse_obj = self.env["stock.warehouse"]
            warehouses = warehouse_obj.search(
                [
                    "|",
                    "|",
                    ("wh_input_stock_loc_id", "=", rec.ids[0]),
                    ("lot_stock_id", "in", rec.ids),
                    ("wh_output_stock_loc_id", "in", rec.ids),
                ]
            )
            for w in warehouses:
                if w.billing_branch_id and rec.billing_branch_id != w.billing_branch_id:
                    raise UserError(
                        _(
                            "Configuration error. This location is "
                            "assigned to a warehouse that belongs to"
                            " a different billing branch."
                        )
                    )

    @api.constrains("billing_branch_id")
    def _check_required_billing_branch(self):
        for rec in self:
            if rec.usage in ("supplier", "customer") and rec.billing_branch_id:
                raise UserError(
                    _(
                        "Configuration error. The billing branch should be "
                        "assigned to internal locations only."
                    )
                )

    @api.constrains("billing_branch_id", "location_id")
    def _check_parent_billing_branch(self):
        for rec in self:
            if (
                rec.location_id
                and rec.location_id.usage == "internal"
                and rec.billing_branch_id
                and rec.billing_branch_id != rec.location_id.billing_branch_id
            ):
                raise UserError(
                    _(
                        "Configuration error. The Parent Stock Location "
                        "must belong to the same Billing Branch."
                    )
                )
