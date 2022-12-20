# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Address Book',
    'version' : '16.1',
    'summary': 'Address Book',
    'sequence': 10,
    'description': """
     odoo Training for new developers    """,
    'category': 'Sale',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/address_book_view.xml',
        'views/address_phone_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}