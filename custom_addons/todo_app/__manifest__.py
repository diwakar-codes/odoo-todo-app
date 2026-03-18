{
    'name': 'Todo App',
    'version': '1.0',
    'summary': 'Simple To-Do Task Manager',
    'category': 'Productivity',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_views.xml',
        'views/todo_menu.xml',
    ],
    'installable': True,
    'application': True,
}