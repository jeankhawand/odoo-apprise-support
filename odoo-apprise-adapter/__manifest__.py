# -*- coding: utf-8 -*-
{
    'name': "Apprise",

    'summary': """
        Odoo Apprise Adapter""",

    'description': """
        This module will add extra notebook page in contacts form view to send notification using apprise
    """,

    'author': "Jean Khawand",
    'website': "https://github.com/jeankhawand/odoo-apprise-adapter",

    # Categories can be used to filter modules in modules listing
    'category': 'Extra Tools',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    'data': [
        'views/apprise_views.xml',
    ],

    "application": True,
    "installable": True,
    "auto_install": False,
    "auto_cleanup": True,
    'license': 'LGPL-3',
    'external_dependencies': {
        'python': ['apprise']
    }
}