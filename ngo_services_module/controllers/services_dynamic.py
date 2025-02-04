from odoo import http
from odoo.http import request

class DynamicAppeals(http.Controller):

    @http.route('/services/', auth="public", type="json", methods=['POST'])
    def all_services(self):
        my_services = request.env['service.template'].sudo().search_read([], [
            'service_name', 'service_image', 'service_url', 'service_icon',
            'banner_heading', 'banner_sub_text', 'banner_image'
        ])
        return my_services
