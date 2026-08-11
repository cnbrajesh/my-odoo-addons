# -*- coding: utf-8 -*-

from odoo import models, fields


class BlogPost(models.Model):
    _inherit = 'blog.post'

    category_id = fields.Many2one(
        comodel_name='blog.category',
        string='Category',
        ondelete='set null',
        index=True
    )
