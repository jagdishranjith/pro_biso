

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    billing_branch_ids = fields.Many2many(
        "billing.branch",
        "product_billing_branch_rel",
        string="Billing Branch",
        compute="_compute_billing_branch_ids",
        store=True,
        readonly=False,
    )
    categ_id = fields.Many2one(
        default=lambda self: self._get_default_category_id(),
    )

    def _get_default_category_id(self):
        category = self.env["product.category"].search([], limit=1)
        if category:
            return category.id
        else:
            return super()._get_default_category_id()

    @api.constrains("billing_branch_ids", "categ_id")
    def _check_billing_branch(self):
        for record in self:
            if (
                record.billing_branch_ids and record.categ_id.billing_branch_ids
            ) and not all(
                ou in record.billing_branch_ids.ids
                for ou in record.categ_id.billing_branch_ids.ids
            ):
                raise ValidationError(
                    _(
                        "The billing branches of the product must include the "
                        "ones from the category."
                    )
                )

    @api.depends("categ_id")
    def _compute_billing_branch_ids(self):
        for record in self:
            record.billing_branch_ids = [(6, 0, record.categ_id.billing_branch_ids.ids)]
