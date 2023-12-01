# -*- coding: utf-8 -*-
# from odoo import http


# class DocumentManagementModule(http.Controller):
#     @http.route('/document_management_module/document_management_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/document_management_module/document_management_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('document_management_module.listing', {
#             'root': '/document_management_module/document_management_module',
#             'objects': http.request.env['document_management_module.document_management_module'].search([]),
#         })

#     @http.route('/document_management_module/document_management_module/objects/<model("document_management_module.document_management_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('document_management_module.object', {
#             'object': obj
#         })
