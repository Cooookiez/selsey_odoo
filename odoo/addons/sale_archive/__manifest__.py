{
    'name': "sale.order.archive",
    'application': True,
    'sequence': -20,

    'summary': """
    archive orders""",

    'description': """
    Long description of module's purpose""",

    'author': "Selsey",
    'website': "https://selsey.pl/",
    ''

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'sale_management'],

    # always loaded
    'data': [],

    # only loaded in demonstration mode
    'demo': [],
}