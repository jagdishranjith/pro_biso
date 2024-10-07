
from odoo import _, api, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends("user_id", "company_id", "billing_branch_id")
    def _compute_warehouse_id(self):
        res = super()._compute_warehouse_id()
        for sale in self:
            if sale.warehouse_id.billing_branch_id != sale.billing_branch_id:
                warehouse = self.env["stock.warehouse"].search(
                    [
                        (
                            "billing_branch_id",
                            "=",
                            sale.billing_branch_id.id,
                        ),
                    ],
                    limit=1,
                )
                if warehouse:
                    sale.warehouse_id = warehouse.id
        return res

    @api.constrains("billing_branch_id", "warehouse_id")
    def _check_wh_billing_branch(self):
        for rec in self:
            if (
                rec.warehouse_id.billing_branch_id
                and rec.billing_branch_id
                and rec.billing_branch_id != rec.warehouse_id.billing_branch_id
            ):
                raise ValidationError(
                    _(
                        "Configuration error!\nThe Billing"
                        "Branch in the Sales Order and in the"
                        " Warehouse must be the same."
                    )
                )
