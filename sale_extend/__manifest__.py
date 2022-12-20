# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Sale Extend',
    'version' : '16.1',
    'summary': 'Sale Extend',
    'sequence': 10,
    'description': """
     odoo Training for new developers    """,
    'category': 'Sale',
    'depends' : ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/stock_picking_view.xml',
        'views/purchase_order_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}