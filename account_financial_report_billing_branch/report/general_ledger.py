# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class GeneralLedgerReport(models.AbstractModel):
    _inherit = "report.account_financial_report.general_ledger"

    def _get_report_values(self, docids, data):
        self = self.with_context(billing_branch_ids=data["billing_branch_ids"])
        return super()._get_report_values(docids, data)

    def _get_initial_balances_bs_ml_domain(
        self, account_ids, company_id, date_from, base_domain, grouped_by, acc_prt=False
    ):
        domain = super()._get_initial_balances_bs_ml_domain(
            account_ids, company_id, date_from, base_domain, grouped_by, acc_prt=acc_prt
        )
        billing_branch_ids = self.env.context.get("billing_branch_ids", [])
        if billing_branch_ids:
            domain.append(("billing_branch_id", "in", billing_branch_ids))
        return domain

    def _get_initial_balances_pl_ml_domain(
        self, account_ids, company_id, date_from, fy_start_date, base_domain
    ):
        domain = super()._get_initial_balances_pl_ml_domain(
            account_ids, company_id, date_from, fy_start_date, base_domain
        )
        billing_branch_ids = self.env.context.get("billing_branch_ids", [])
        if billing_branch_ids:
            domain.append(("billing_branch_id", "in", billing_branch_ids))
        return domain

    def _get_initial_balance_fy_pl_ml_domain(
        self, account_ids, company_id, fy_start_date, base_domain
    ):
        domain = super()._get_initial_balance_fy_pl_ml_domain(
            account_ids, company_id, fy_start_date, base_domain
        )
        billing_branch_ids = self.env.context.get("billing_branch_ids", [])
        if billing_branch_ids:
            domain.append(("billing_branch_id", "in", billing_branch_ids))
        return domain

    @api.model
    def _get_period_domain(
        self,
        account_ids,
        partner_ids,
        company_id,
        only_posted_moves,
        date_to,
        date_from,
        cost_center_ids,
    ):
        domain = super()._get_period_domain(
            account_ids,
            partner_ids,
            company_id,
            only_posted_moves,
            date_to,
            date_from,
            cost_center_ids,
        )
        billing_branch_ids = self.env.context.get("billing_branch_ids", [])
        if billing_branch_ids:
            domain.append(("billing_branch_id", "in", billing_branch_ids))
        return domain
