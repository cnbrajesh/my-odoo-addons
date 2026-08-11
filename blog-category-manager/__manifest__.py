{
    'name': 'Blog Category Manager',
    'version': '16.0.1.0.0',
    'category': 'Website/Blog',
    'summary': 'Enhanced blog category management',
    'description': """
        This module provides enhanced category management features for Odoo Blog.
        - Custom category organization
        - Advanced filtering options
        - SEO improvements
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': ['website_blog'],
    'data': [
        'security/ir.model.access.csv',
        'views/blog_category_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
