from odoo import models, fields

class ServiceTemplate(models.Model):
    _name = 'service.template'
    _description = 'Service Template'

    service_name = fields.Char(string='Name', required=True)
    service_image = fields.Binary(string='Service Image')
    service_url = fields.Char(string="Service URL", required=True)
    service_icon = fields.Binary(string='Icon')
    banner_heading = fields.Char(string='Banner Heading')
    banner_sub_text = fields.Text(string='Banner Sub Text')
    banner_image = fields.Binary(string='Banner Image')