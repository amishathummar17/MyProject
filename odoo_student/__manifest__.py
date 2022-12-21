# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Student',
    'version' : '16.1',
    'summary': 'Student',
    'sequence': 10,
    'description': """
     odoo Training for new developers    """,
    'category': 'Sale',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/std_mark_view.xml',
        'views/std_student_view.xml',
        'views/res_partner_view.xml',
        'views/student_school_view.xml',
        'views/configuration_view.xml',
        'report/student_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}