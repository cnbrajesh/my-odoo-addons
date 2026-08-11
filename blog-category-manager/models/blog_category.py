# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BlogCategory(models.Model):
    _inherit = 'blog.category'

    # Add custom fields here
    description = fields.Text(string='Description', help='Detailed description of the category')
    color = fields.Integer(string='Color Index')
    parent_id = fields.Many2one('blog.category', string='Parent Category', ondelete='cascade')
    child_ids = fields.One2many('blog.category', 'parent_id', string='Child Categories')
    
    # SEO Fields
    meta_title = fields.Char(string='Meta Title')
    meta_description = fields.Text(string='Meta Description')
    meta_keywords = fields.Char(string='Meta Keywords')
