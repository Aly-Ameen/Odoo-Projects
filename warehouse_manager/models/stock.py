from odoo import models, fields, api

class InventoryStockStatus(models.Model):
    _name = 'stock.list'
    _description = 'Monitoring the inventory stock level'
    _log_access = False

    client_name = fields.Char('Customer Name', help="Customer brand name for the order")
    model_name = fields.Char('Model Name', help="Name of the garment model")
    model_color_name = fields.Char('Model Color Name', help="Name of the color variant")
    model_color_code = fields.Char('Model Color Code', help="Color code for the garment")

    purchasing_order_number = fields.Char('PO Number', help="Purchase Order number")
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

    @api.constrains('client_name', 'model_name', 'purchasing_order_number', 'po_quantity', 'po_destination')
    def _check_required_fields(self):
        for record in self:
            if not record.client_name or not record.model_name or not record.purchasing_order_number or not record.po_quantity or not record.po_destination:
                raise models.ValidationError(
                    "Client Name, Model Name, PO Number, PO Quantity, and PO Destination are required and cannot be null.")

    @api.constrains('purchasing_order_number')
    def _check_purchasing_order_number_length(self):
        for record in self:
            if record.purchasing_order_number and len(record.purchasing_order_number) > 8:
                raise models.ValidationError("PO Number cannot exceed 8 digits.")

    @api.constrains('model_color_code')
    def _check_model_color_code_length(self):
        for record in self:
            if record.model_color_code and len(record.model_color_code) > 6:
                raise models.ValidationError("Model Color Code cannot exceed 6 characters (letters or numbers).")
