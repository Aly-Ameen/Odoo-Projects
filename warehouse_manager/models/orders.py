from odoo import models, fields, api

class OrdersDetails(models.Model):
    _name = "orders.list"
    _description = "Describe the technical details for running orders"
    _log_access = False

    client_name = fields.Char('Customer Name', help="Customer brand name for the order")
    model_name = fields.Char('Model Name', help="Name of the garment model")
    model_color_name = fields.Char('Model Color Name', help="Name of the color variant")
    model_color_code = fields.Char('Model Color Code', help="Color code for the garment")

    purchasing_order_number = fields.Integer('PO Number', help="Purchase Order number")
    po_quantity = fields.Integer('PO Quantity', help="Total quantity in the purchase order")
    po_destination = fields.Text('PO Destination', help="Destination of the goods in the PO")

    PO_STATUS = [
        ('production', 'Production'),
        ('packing completed', 'Packing Completed'),
        ('under inspection', 'Under Inspection'),
        ('ready to ship', 'Ready to Ship'),
        ('shipped', 'Shipped'),
    ]
    po_status = fields.Selection(PO_STATUS, string='PO Status', help="Current status of the PO")

    po_inspection_result = fields.Selection([
        ('pass', 'Pass'),
        ('fail', 'Fail')
    ], string='PO Inspection Result', help="Result of the inspection process")

    packing_list = fields.Binary(string='Packing List', help="Upload the packing list PDF file.")
    shipping_invoice = fields.Binary(string='Shipping Invoice', help="Upload the shipping invoice PDF file.")
    packing_list_received = fields.Boolean(string='Packing List Received', default=False)
    shipping_invoice_received = fields.Boolean(string='Shipping Invoice Received', default=False)

    # Relations
    stock_ids = fields.One2many('stock.list', 'purchasing_order_id', string='Stock Items')
    supplies_ids = fields.Many2many('warehouse.supplies', string='Supplies Used')

    @api.model
    def create(self, vals):
        # Debug print
        print("Create method called with vals:", vals)
        # Ensure PO number is a number without commas
        if 'purchasing_order_number' in vals and isinstance(vals['purchasing_order_number'], str):
            vals['purchasing_order_number'] = int(vals['purchasing_order_number'].replace(',', ''))
        return super(OrdersDetails, self).create(vals)

    def write(self, vals):
        # Debug print
        print("Write method called with vals:", vals)
        # Ensure PO number is a number without commas
        if 'purchasing_order_number' in vals and isinstance(vals['purchasing_order_number'], str):
            vals['purchasing_order_number'] = int(vals['purchasing_order_number'].replace(',', ''))
        return super(OrdersDetails, self).write(vals)

    @api.onchange('model_color_code')
    def _onchange_model_color_code(self):
        # Debug print
        print("Onchange method called")
        if self.model_color_code:
            self.model_color_code = self.model_color_code.upper()