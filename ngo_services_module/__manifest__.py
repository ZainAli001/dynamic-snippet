{
    'name': 'NGO Services Module',
    'description': """NGO Services Module""",
    'depends': ['website','product','website_payment'],
    'data': [
        'views/services_view.xml',
        'views/snippets/s_services_dynamic.xml',
        'views/snippets/snippets.xml',
        'security/ir.model.access.csv',

    ],
    'assets': {
        'web.assets_frontend': [
            'ngo_services_module/static/src/js/dynamic_service.js',
        ],

    },
    'demo': [],
    'application': True,
    'auto_install': False,
}
