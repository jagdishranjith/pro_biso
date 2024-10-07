# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class TrialBalanceReport(models.AbstractModel):
    _inherit = "report.account_financial_report.trial_balance"

    def _get_report_values(self, docids, data):
        self = self.with_context(billing_branch_ids=data["billing_branch_ids"])
        return super()._get_report_values(docids, data)

    def _get_initial_balances_bs_ml_domain(
        self,
        account_ids,
        journal_ids,
        partner_ids,
        company_id,
        date_from,
        only_posted_moves,
        show_partner_details,
    ):
        domain = super()._get_initial_balances_bs_ml_domain(
            account_ids,
            journal_ids,
            partner_ids,
            company_id,
            date_from,
            only_posted_moves,
            show_partner_details,
        )
        billing_branch_ids = self.env.context.get("billing_branch_ids", [])
        if billing_branch_ids:
            domain.append(("billing_branch_id", "in", billing_branch_ids))
        return domain

    def _get_initial_balances_pl_ml_domain(
        self,
        account_ids,
        journal_ids,
        partner_ids,
        company_id,
        date_from,
        only_posted_moves,
        show_partner_details,
        fy_start_date,
    ):
        domain = super()._get_initial_balances_pl_ml_domain(
            account_ids,
            journal_ids,
            partner_ids,
            company_id,
            date_from,
            only_posted_moves,
            show_partner_details,
            fy_start_date,
        )
        billing_branch_ids = self.env.context.get("billing_branch_ids", [])
        if billing_branch_ids:
            domain.append(("billing_branch_id", "in", billing_branch_ids))
        return domain

    def _get_period_ml_domain(
        self,
        account_ids,
        journal_ids,
        partner_ids,
        company_id,
        date_to,
        date_from,
        only_posted_moves,
        show_partner_details,
    ):
        domain = super()._get_period_ml_domain(
            account_ids,
            journal_ids,
            partner_ids,
            company_id,
            date_to,
            date_from,
            only_posted_moves,
            show_partner_details,
        )
        billing_branch_ids = self.env.context.get("billing_branch_ids", [])
        if billing_branch_ids:
            domain.append(("billing_branch_id", "in", billing_branch_ids))
        return domain
