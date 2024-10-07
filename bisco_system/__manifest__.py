# -*- coding: utf-8 -*-
{
    'name': 'Bisco System',
    'version': '17.0.0.0.0',
    'category': 'Sale',
    'summary': 'Upgrade the base fields attributes',
    'depends': [
        'account_billing_branch',
        'account_invoice_inter_company',
        'billing_branch_access_all',
        'product_billing_branch',
        'purchase_stock_billing_branch',
        'stock_billing_branch',
        'account_billing_branch_access_all',
        'analytic_billing_branch',
        'purchase_billing_branch',
        'sale_billing_branch',
        'stock_billing_branch_access_all',
        'account_financial_report',
        'base_view_inheritance_extension',
        'date_range',
        'purchase_sale_inter_company',
        'sales_team_billing_branch',
        'account_financial_report_billing_branch',
        'billing_branch',
        'hr_expense_billing_branch',
        # 'purchase_sale_stock_inter_company',
        'sale_stock_billing_branch',
    ],

    'data': [
        'views/purchase_order_view.xml',
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
    ],

}
