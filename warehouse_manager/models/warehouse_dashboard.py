from odoo import models, fields, api


class WarehouseDashboard(models.Model):
    _name = 'warehouse.dashboard'
    _description = 'Warehouse Dashboard'

    total_orders = fields.Integer(string='Total Orders', compute='_compute_total_orders')
    total_stock = fields.Integer(string='Total Stock', compute='_compute_total_stock')
    total_supplies = fields.Integer(string='Total Supplies', compute='_compute_total_supplies')

    def _compute_total_orders(self):
        # Count all orders in the 'orders.list' model
        self.total_orders = self.env['orders.list'].search_count([])

    def _compute_total_stock(self):
        # Count all stock records in the 'stock.list' model
        self.total_stock = self.env['stock.list'].search_count([])

    def _compute_total_supplies(self):
        # Count all supplies in the 'warehouse.supplies' model
        self.total_supplies = self.env['warehouse.supplies'].search_count([])

