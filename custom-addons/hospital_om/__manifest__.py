# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': 'Productivity',
    'description': 'Hospital Management Software',
    'summary': 'Hospital Management Software',
    'sequence': '10',
    'author': 'Odoo Mates',
    'company': 'Odoo Mates',
    'maintainer': 'Odoo Mates',
    'website': 'https://www.odoomates.tech',
    'depends': ['sale', 'mail'],
    'demo': [],
    'data': [
        'views/patient.xml',
        'views/sale.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
