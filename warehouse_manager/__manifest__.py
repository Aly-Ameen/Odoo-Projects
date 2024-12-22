{
    'name': 'Warehouse Manager',
    'category': 'Warehouse',
    'summary': 'Module for managing warehouse operations',
    'description': """
        A module for managing warehouse operations such as inventory tracking, stock management, and product handling.
    """,
    'author': 'Aly Ameen',
    'license': 'LGPL-3',
    'website': 'https://odoo.com',
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': -10,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/orders_view.xml',
        'views/stock_view.xml',
        'views/supplies_view.xml',
        'views/actions.xml',
        'views/base_menu.xml',
        'views/warehouse_dashboard_view.xml',
             ],

}


