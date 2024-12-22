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

    # Relations
    order_ids = fields.Many2many('orders.list', string='Related Orders')
    stock_ids = fields.Many2many('stock.list', string='Related Stocks')
