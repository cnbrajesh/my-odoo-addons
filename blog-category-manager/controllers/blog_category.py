# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class BlogCategoryController(http.Controller):

    @http.route(['/blog/category/<model("blog.category"):category_id>'], type='http', auth="public", website=True)
    def blog_category(self, category_id, page=1, **post):
        """Display blog posts filtered by category"""
        domain = [('blog_id', '=', True), ('category_ids', 'in', [category_id.id])]
        
        posts = request.env['blog.post'].sudo().search(domain, limit=9, offset=(int(page) - 1) * 9)
        
        values = {
            'category': category_id,
            'posts': posts,
            'page': int(page),
        }
        
        return request.render("website_blog.blog_posts", values)
