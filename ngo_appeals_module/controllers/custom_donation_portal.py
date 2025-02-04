from odoo import http
from odoo.http import request
from odoo.addons.website_payment.controllers.portal import PaymentPortal as BasePaymentPortal
from odoo.tools.json import scriptsafe as json_safe
from odoo.addons.payment import utils as payment_utils

class CustomPaymentPortal(BasePaymentPortal):


    @http.route('/donation/pay/appeals/<int:appeal_id>', type='http', methods=['GET', 'POST'], auth='public',
                website=True, sitemap=False)
    def custom_donation_pay(self, appeal_id, **kwargs):
        kwargs['is_donation'] = True
        kwargs['currency_id'] = self._cast_as_int(kwargs.get('currency_id')) or request.env.company.currency_id.id
        # custom_amount = self._get_custom_amount(appeal_id)
        kwargs['amount'] = self._cast_as_float(kwargs.get('amount')) or 25.0
        kwargs['donation_options'] = kwargs.get('donation_options', json_safe.dumps(dict(customAmount="freeAmount")))
        print("kwargs['donation_options']", kwargs['donation_options'])
        appeal = request.env['appeal.template'].browse(appeal_id)
        # Add appeal_id to kwargs
        kwargs['appeal_id'] = appeal_id  # Use appeal_id directly from the route parameter
        print("appeal_id", appeal_id)

        context = dict(request.env.context)
        context.update({
            'appeal_id': appeal.id,  # Add appeal_id to context

        })
        request.env = request.env(context=context)  # Set the updated context
        print("Updated context:", request.env.context)
        # Log appeal_id and amount for debugging
        print("appeal_id:", appeal_id, "amount:", kwargs['amount'])
        # Handle public user case
        if request.env.user._is_public():
            kwargs['partner_id'] = request.env.user.partner_id.id
            kwargs['access_token'] = payment_utils.generate_access_token(kwargs['partner_id'], kwargs['amount'],
                                                                         kwargs['currency_id'])

        # Log the appeal_id for debugging
        # _logger.info("Appeal ID provided for donation: %s", appeal_id)

        return self.payment_pay(**kwargs)

