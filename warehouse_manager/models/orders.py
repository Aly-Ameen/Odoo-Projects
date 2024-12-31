from odoo import models, fields, api

class OrdersDetails(models.Model):
    _name = "orders.list"
    _description = "Describe the technical details for running orders"
    _log_access = False

    client_name = fields.Char('Customer Name', help="Customer brand name for the order")
    model_name = fields.Char('Model Name', help="Name of the garment model")
    model_color_name = fields.Char('Model Color Name', help="Name of the color variant")
    model_color_code = fields.Char('Model Color Code', help="Color code for the garment")

    purchasing_order_number = fields.Char('PO Number', help="Purchase Order number")
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

    # Relating with stock model:
    stock_ids = fields.One2many('stock.list', 'purchasing_order_id', string='Stock Items')
    # Relation with `supplies model:
    supplies_ids = fields.One2many(
        'warehouse.supplies', 'order_id', string='Supplies',
        help="Supplies linked to this order.")

    #Customized methods:

    # 1-Odoo will not accept saving the records until specific fields are filled.
    @api.constrains('client_name', 'model_name', 'purchasing_order_number', 'po_quantity', 'po_destination')
    def _check_required_fields(self):
        for record in self:
            if not record.client_name or not record.model_name or not record.purchasing_order_number or not record.po_quantity or not record.po_destination:
                raise models.ValidationError("Client Name, Model Name, PO Number, PO Quantity, and PO Destination are required and cannot be null.")

   # 2-To ensure that the PO field is no longer than 8 digits number (can be customized according to your standard).
    @api.constrains('purchasing_order_number')
    def _check_purchasing_order_number_length(self):
        for record in self:
            if record.purchasing_order_number and len(str(record.purchasing_order_number)) > 8:
                raise models.ValidationError("Purchasing Order Number cannot exceed 8 digits.")

    # 3-To ensure that the Model Color Code field is no longer than 6 digits number (can be customized according to your standard).
    @api.constrains('model_color_code')
    def _check_model_color_code_length(self):
        for record in self:
            if record.model_color_code and len(record.model_color_code) > 6:
                raise models.ValidationError("Model Color Code cannot exceed 6 characters (letters or numbers).")

    # 4-Ensure that the Inspection Result field can't be accessed as long as the PO Status field is one of these options:(Production - Packing Completed
    @api.constrains('po_status', 'po_inspection_result')
    def _check_inspection_result_permission(self):
        for record in self:
            if record.po_inspection_result and record.po_status in ['production', 'packing completed']:
                raise models.ValidationError("You cannot set the PO Inspection Result while the PO Status is 'Production' or 'Packing Completed'.")


