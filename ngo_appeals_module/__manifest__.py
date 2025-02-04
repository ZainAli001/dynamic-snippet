{
    'name': 'NGO Appeals Module',
    'description': """NGO Appeals Module""",
    'depends': ['website','product','website_payment'],
    'data': [
        'views/appeals_view.xml',
        'views/snippets/s_appeals_dynamic.xml',
        'views/snippets/snippets.xml',
        'views/product_customization_view.xml',
        'security/ir.model.access.csv',

    ],
    'assets': {
        'web.assets_frontend': [
            'ngo_appeals_module/static/src/js/dynamic_appeal.js',
        ],

    },
    'demo': [],
    'application': True,
    'auto_install': False,
}
