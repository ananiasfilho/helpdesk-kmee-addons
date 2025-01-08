
{
    'name': 'Help Desk Ticket  Stage Duration',
    'version': '16.0.1.0.0',
    'summary': 'Shows the duration each ticket spent in each stage',
    'category': 'helpdesk',
    'author': 'Ananias, KMEE',
    'website': 'https://www.kmee.com.br',
    'license': 'AGPL-3',
    'depends': ['helpdesk_mgmt'],
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
    ],
    'installable': True,
    'application': False,
}
