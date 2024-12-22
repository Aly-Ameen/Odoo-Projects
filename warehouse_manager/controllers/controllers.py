# -*- coding: utf-8 -*-
# from odoo import http


# class WarehouseManager(http.Controller):
#     @http.route('/warehouse_manager/warehouse_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/warehouse_manager/warehouse_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('warehouse_manager.listing', {
#             'root': '/warehouse_manager/warehouse_manager',
#             'objects': http.request.env['warehouse_manager.warehouse_manager'].search([]),
#         })

#     @http.route('/warehouse_manager/warehouse_manager/objects/<model("warehouse_manager.warehouse_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('warehouse_manager.object', {
#             'object': obj
#         })

