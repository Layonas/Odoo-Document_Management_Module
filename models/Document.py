from odoo import models, fields, api

class Document(models.Model):
    _name = "document_management.document"
    _description = "A document"

    name = fields.Char(string="Title", required = True)
    description = fields.Text(string='Description')
    company = fields.Char(string='Company', required=True)
    created_by = fields.Char(string='Created by')
    responsible_users = fields.Many2many('res.users', string='Responsible workers')

# class document_management_module(models.Model):
#     _name = 'document_management_module.document_management_module'
#     _description = 'document_management_module.document_management_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
