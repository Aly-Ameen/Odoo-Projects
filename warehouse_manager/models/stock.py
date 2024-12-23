from odoo import models, fields, api

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

    @api.model
    def create(self, vals):
        # Ensure PO number is a number without commas
        if 'purchasing_order_number' in vals and isinstance(vals['purchasing_order_number'], str):
            vals['purchasing_order_number'] = int(vals['purchasing_order_number'].replace(',', ''))
        return super(InventoryStockStatus, self).create(vals)

    def write(self, vals):
        # Ensure PO number is a number without commas
        if 'purchasing_order_number' in vals and isinstance(vals['purchasing_order_number'], str):
            vals['purchasing_order_number'] = int(vals['purchasing_order_number'].replace(',', ''))
        return super(InventoryStockStatus, self).write(vals)

    @api.onchange('model_color_code')
    def _onchange_model_color_code(self):
        if self.model_color_code:
            self.model_color_code = self.model_color_code.upper()