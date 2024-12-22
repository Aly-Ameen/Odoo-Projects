from odoo import models, fields

class InventoryStockStatus(models.Model):
    _name = 'stock.list'
    _description = 'Monitoring the inventory stock level'
    _log_access = False

    client_name = fields.Char('Customer Name', help="Customer brand name for the order")
    model_name = fields.Char('Model Name', help="Name of the garment model")
    model_color_name = fields.Char('Model Color Name', help="Name of the color variant")
    model_color_code = fields.Char('Model Color Code', help="Color code for the garment")

    purchasing_order_number = fields.Integer('PO Number', help="Purchase Order number")
    po_destination = fields.Text('PO Destination', help="Destination of the goods in the PO")
    stock_quantity = fields.Integer('Stock Quantity', help="Total stock quantity in the purchase order number")

    # Relations
    purchasing_order_id = fields.Many2one('orders.list', string='Related Order')
    supplies_ids = fields.Many2many('warehouse.supplies', string='Supplies Used')
