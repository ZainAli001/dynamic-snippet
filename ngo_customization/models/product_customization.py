from email.policy import default

from odoo import models, fields, api


class ProductCustomization(models.Model):
    _inherit = 'product.template'

    custom_price =  fields.Boolean(string="Custom Price?")
