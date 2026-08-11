{
    "name": "Blog Category Filter",
    "version": "19.0.1.0.0",
    "summary": "Custom blog category management and filtering",
    "description": """
        Blog Category Filter Module
        ===========================
        * Custom blog.category model with name, slug, and sequence
        * Extended blog.post with category_id field
        * Public controller for filtering blog posts by category
        * Website template for displaying categories and blog posts
    """,
    "author": "Custom",
    "website": "",
    "category": "Website/Blog",
    "depends": ["website_blog"],
    "data": [
        "security/ir.model.access.csv",
        "views/blog_category_views.xml",
        "views/blog_post_views.xml",
        "views/templates.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
