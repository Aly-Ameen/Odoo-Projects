from odoo import http
from odoo.http import request

class YourModuleController(http.Controller):

    @http.route('/your_module/custom_page', auth='public', website=True)
    def custom_page(self):
        return request.render('your_module.your_custom_page', {})