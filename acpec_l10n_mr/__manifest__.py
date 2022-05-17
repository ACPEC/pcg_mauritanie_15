# -*- coding: utf-8 -*-


{
    'name': 'Plan Comptable - Mauritanie',
    'author': 'Med Mahmoud',
    'company': 'ACPEC SARL',
    'version': '15.1.0',
    'license': 'AGPL-3',
    'category': 'Accounting',
    'website': 'https://www.acpec-sarl.com',
    'depends': ['base', 'account'],
    'description': u"""
    Ce module charge un modèle de plan de comptes généraux pour la Mauritanie.
    Il offre un ensemble réduit de comptes et de taxes suffisant pour démarrer avec ODOO. Instructions d'installation:
    Créer une base Odoo vierge. Installer ce module et puis installer le module de la comptabilité. Et c'est tout!""",
    'data': [
        'data/l10n_mr_chart_data.xml',
        'data/account_chart_template_data.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
}
