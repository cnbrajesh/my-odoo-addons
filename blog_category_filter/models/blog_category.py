# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BlogCategory(models.Model):
    _name = 'blog.category'
    _description = 'Blog Category'
    _order = 'sequence, name'

    name = fields.Char(string='Name', required=True)
    slug = fields.Char(string='Slug', required=True, copy=False)
    sequence = fields.Integer(string='Sequence', default=10)

    _sql_constraints = [
        ('unique_slug', 'unique(slug)', 'Slug must be unique!')
    ]

    @api.model
    def create(self, vals):
        if not vals.get('slug') and vals.get('name'):
            vals['slug'] = self._generate_slug(vals['name'])
        return super().create(vals)

    def write(self, vals):
        if vals.get('name') and not vals.get('slug'):
            vals['slug'] = self._generate_slug(vals['name'])
        return super().write(vals)

    def _generate_slug(self, name):
        """Generate a URL-friendly slug from the name."""
        import re
        slug = name.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[-\s]+', '-', slug)
        slug = slug.strip('-_')
        return slug
