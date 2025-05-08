{
    'name': 'Helpdesk Dependency Tracking',
    'version': '16.0.1.0.0',
    'summary': 'Track team dependencies in helpdesk tickets',
    'description': """
        Adds team dependency tracking to helpdesk tickets with history log
    """,
    'author': 'KMEE Tecnologia',
    'website': 'https://kmee.com.br',
    'depends': ['helpdesk_mgmt'],
    'category': 'Services/Helpdesk',
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
	'security/helpdesk_dependency_security.xml',
    ],
    'installable': True,
    'application': False,
}
