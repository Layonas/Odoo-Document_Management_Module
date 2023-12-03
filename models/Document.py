from odoo import models, fields, api

class Document(models.Model):
    _name = "document_management.document"
    _description = "A document"

    name = fields.Char(string="Title", required = True)
    description = fields.Text(string='Description')
    company = fields.Char(string='Company', required=True)
    created_by = fields.Many2one('res.users', string='Created by', default=lambda self: self.env.user, readonly=True)
    responsible_users = fields.Many2many('res.users', string='Responsible workers')
