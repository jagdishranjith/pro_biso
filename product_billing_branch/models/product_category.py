
from odoo import fields, models
from odoo.models import Command


class ProductCategory(models.Model):
    _inherit = "product.category"

    billing_branch_ids = fields.Many2many(
        "billing.branch",
        "product_category_billing_branch_rel",
        string="Billing Branch",
    )

    def write(self, vals):
        res = super().write(vals)
        product_template_obj = self.env["product.template"]
        if vals.get("billing_branch_ids"):
            for rec in self:
                products = product_template_obj.search(
                    [("categ_id", "child_of", rec.id)]
                )
                category_ou_ids = rec.billing_branch_ids
                for product in products:
                    ou_ids = product.billing_branch_ids | category_ou_ids
                    product.billing_branch_ids = [Command.set(ou_ids.ids)]
        return res
