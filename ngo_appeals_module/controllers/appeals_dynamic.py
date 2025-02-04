from odoo import http
from odoo.http import request


class DynamicAppeals(http.Controller):

    @http.route('/appeals/', auth="public", type="json", methods=['POST'])
    def all_appeals(self):
        my_appeals = http.request.env['appeal.template'].sudo().search_read([],  ['name', 'start_date', 'banner_image','end_date','goal','total_contribution','total_partners'])
        # print(my_appeals)
        # for appeal in my_appeals:
        #     appeal['donation_button'] = request.env['ir.ui.view']._render_template("website_payment.s_donation_button", {'appeal': appeal})
        return my_appeals
