from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    billing_branch_ids = fields.One2many(
        comodel_name="billing.branch",
        compute="_compute_billing_branch_ids",
        inverse="_inverse_billing_branch_ids",
        string="Allowed Billing Branch",
        compute_sudo=True,
    )

    assigned_billing_branch_ids = fields.Many2many(
        comodel_name="billing.branch",
        string="Billing Branch",
        default=lambda self: self._default_billing_branch(),
    )

    default_billing_branch_id = fields.Many2one(
        comodel_name="billing.branch",
        string="Billing Branch",
        default=lambda self: self._default_billing_branch(),
        domain="[('company_id', '=', current_company_id)]",
    )

    @api.model
    def _get_default_billing_branch(self, uid2=False):
        if not uid2:
            uid2 = self.env.user.id
        user = self.env["res.users"].browse(uid2)
        # check if the company of the default OU is active
        if user.default_billing_branch_id:
            return user.default_billing_branch_id
        else:
            # find an OU of the main active company
            for ou in user.assigned_billing_branch_ids:
                if ou.sudo().company_id in self.env.company:
                    return ou
            # find an OU of any active company
            for ou in user.assigned_billing_branch_ids:
                if ou.sudo().company_id in self.env.companies:
                    return ou
        return False

    @api.model
    def _default_billing_branch(self):
        return self._get_default_billing_branch()

    @api.model
    def default_get(self, fields):
        vals = super().default_get(fields)
        if (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("base_setup.default_user_rights", "False")
            == "True"
        ):
            default_user = self.env.ref("base.default_user")
            vals[
                "default_billing_branch_id"
            ] = default_user.default_billing_branch_id.id
            vals["billing_branch_ids"] = [(6, 0, default_user.billing_branch_ids.ids)]
        return vals

    @api.depends("groups_id", "assigned_billing_branch_ids")
    def _compute_billing_branch_ids(self):
        for user in self:
            if user._origin.has_group("billing_branch.group_manager_billing_branch"):
                if self.env.context.get("allowed_company_ids"):
                    dom = [
                        "|",
                        ("company_id", "=", False),
                        ("company_id", "in", self.env.context["allowed_company_ids"]),
                    ]
                else:
                    dom = []

                user.billing_branch_ids = self.env["billing.branch"].sudo().search(dom)
            else:
                user.billing_branch_ids = user.assigned_billing_branch_ids

    def _inverse_billing_branch_ids(self):
        for user in self:
            user.assigned_billing_branch_ids = user.billing_branch_ids
        self.env.registry.clear_cache()

    @api.onchange("billing_branch_ids")
    def _onchange_billing_branch_ids(self):
        for record in self:
            if (
                record.default_billing_branch_id
                and record.default_billing_branch_id
                not in record.billing_branch_ids._origin
            ):
                record.default_billing_branch_id = False

    def billing_branches(self):
        return self.env.user.billing_branch_ids
