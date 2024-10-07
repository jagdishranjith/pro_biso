
from odoo import api, fields, models


class BillingBranch(models.Model):
    _name = "billing.branch"
    _description = "Billing Branch"
    _rec_names_search = ["name", "code"]

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        "res.company",
        required=False,
        default=lambda self: self.env.company,
    )
    partner_id = fields.Many2one("res.partner", "Partner", required=False)
    user_ids = fields.Many2many(
        "res.users",
        "billing_branch_users_rel",
        "billing_branch_id",
        "user_id",
        "Users Allowed",
    )

    _sql_constraints = [
        (
            "code_company_uniq",
            "unique (code,company_id)",
            "The code of the billing branch must " "be unique per company!",
        ),
        (
            "name_company_uniq",
            "unique (name,company_id)",
            "The name of the billing branch must " "be unique per company!",
        ),
    ]

    @api.depends("name", "code")
    def _compute_display_name(self):
        for ou in self:
            ou.display_name = f"[{ou.code}] {ou.name}"

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        res.write({"user_ids": [fields.Command.link(self.env.user.id)]})
        self.env.registry.clear_cache()
        return res

    def write(self, vals):
        self.env.registry.clear_cache()
        return super().write(vals)
