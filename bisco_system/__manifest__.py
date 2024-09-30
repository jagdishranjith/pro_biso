# -*- coding: utf-8 -*-
{
    'name': 'Bisco sys app',
    'version': '17.0.0.0.0',
    'category': 'Sale',
    'summary': 'Upgrade the base fields attributes',
    'depends': ['sale_stock', 'purchase_stock'],

    'data': [
        'views/purchase_order_view.xml',
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
    ],

}
