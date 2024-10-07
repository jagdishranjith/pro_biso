
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    def _default_billing_branch(self):
        if self.company_id:
            company = self.company_id
        else:
            company = self.env.company
        for ou in self.env.user.billing_branch_ids:
            if company == self.company_id:
                self.billing_branch_id = ou

    billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Billing Branch",
        default=_default_billing_branch,
        check_company=True,
    )


class StockWarehouseOrderPoint(models.Model):
    _inherit = "stock.warehouse.orderpoint"

    @api.constrains(
        "warehouse_id",
        "location_id",
    )
    def _check_location(self):
        for rec in self:
            if (
                rec.warehouse_id.billing_branch_id
                and rec.warehouse_id
                and rec.location_id
                and rec.warehouse_id.billing_branch_id
                != rec.location_id.billing_branch_id
            ):
                raise UserError(
                    _(
                        "Configuration Error. The Billing Branch of the "
                        "Warehouse and the Location must be the same. "
                    )
                )
