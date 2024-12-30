from odoo import models, fields, api

class WarehouseSupplies(models.Model):
    _name = 'warehouse.supplies'
    _description = 'Control the warehouse supplies'
    _log_access = False

    item_name = fields.Selection([
        ('carton_box', 'Carton Box'),
        ('tape_roll', 'Tape Roll')
    ], string='Item Name', required=True)

    carton_size = fields.Selection([
        ('36', '36'),
        ('38', '38'),
        ('40', '40')
    ], string='Carton Size', help="Size of the carton box.")

    tape_type = fields.Selection([
        ('transparent', 'Transparent'),
        ('colored', 'Colored'),
        ('printed', 'Printed')
    ], string='Tape Type', help="Type of tape roll.")

    tape_size = fields.Selection([
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large')
    ], string='Tape Size', help="Size of the tape roll.")

    quantity = fields.Integer(string='Item Quantity', required=True, help="Number of items in stock.")

    @api.onchange('item_name')
    def _onchange_item_name(self):
        # Reset fields based on item_name selection
        if self.item_name == 'carton_box':
            self.tape_type = False
            self.tape_size = False
        elif self.item_name == 'tape_roll':
            self.carton_size = False

        # Fields to store `orders.list` data

    customer_name = fields.Char(string='Customer Name')
    model_name = fields.Char(string='Model Name')
    model_color_name = fields.Char(string='Model Color Name')
    model_color_code = fields.Char(string='Model Color Code')
    po_number = fields.Char(string='PO Number')
    po_quantity = fields.Integer(string='PO Quantity')

    # Relation with `orders.list`
    order_id = fields.Many2one('orders.list', string='Order', help="Related Order")

    # Automatically fetch and record data from `orders.list`
    @api.onchange('order_id')
    def _onchange_order_id(self):
        """Fetch related order data when an order is selected."""
        if self.order_id:
            self.customer_name = self.order_id.customer_name
            self.model_name = self.order_id.model_name
            self.model_color_name = self.order_id.model_color_name
            self.model_color_code = self.order_id.model_color_code
            self.po_number = self.order_id.po_number
            self.po_quantity = self.order_id.po_quantity

    # Relations
    stock_ids = fields.Many2many('stock.list', string='Related Stocks')