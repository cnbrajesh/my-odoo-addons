# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_blog.controllers.main import Blog


class BlogCategoryController(Blog):

    @http.route(['/blog-category'], type='http', auth='public', website=True, sitemap=True)
    def blog_category_index(self, **post):
        """List all published blog posts."""
        return self.blog_category_list(category_slug=None, **post)

    @http.route(['/blog-category/<string:category_slug>'], type='http', auth='public', website=True, sitemap=True)
    def blog_category_list(self, category_slug=None, **post):
        """List published blog posts filtered by category."""
        values = {}
        
        # Get all categories for the sidebar/buttons
        categories = request.env['blog.category'].sudo().search([], order='sequence, name')
        values['categories'] = categories
        
        # Get current category if specified
        current_category = None
        if category_slug:
            current_category = request.env['blog.category'].sudo().search([('slug', '=', category_slug)], limit=1)
            if not current_category:
                return request.redirect('/blog-category')
        
        values['current_category'] = current_category
        
        # Build domain for published blog posts
        domain = [('website_published', '=', True)]
        if current_category:
            domain.append(('category_id', '=', current_category.id))
        
        # Get blog posts
        blog_posts = request.env['blog.post'].sudo().search(domain, order='write_date desc')
        values['blog_posts'] = blog_posts
        
        # Render template
        return request.render('blog_category_filter.blog_category_template', values)
