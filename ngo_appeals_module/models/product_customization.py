from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_appeal = fields.Boolean(
        string="Appeals",
        default=False,
        help="Check if this product is related to appeals."
    )


class Appeal(models.Model):
    _name = 'appeal.template'
    _description = 'Appeal'

    product_id = fields.Many2one(
        'product.template',
        string="Related Product",
        help="Select the product associated with this appeal."
    )
    name = fields.Char(
        string="Appeal Name",
        required=True,
        help="Enter the name of the appeal."
    )
    start_date = fields.Date(
        string="Start Date",
        required=True,
        help="The date when the appeal starts."
    )
    end_date = fields.Date(
        string="End Date",
        required=True,
        help="The date when the appeal ends."
    )
    goal = fields.Float(
        string="Goal",
        required=True,
        help="The monetary goal for the appeal."
    )
    banner_image = fields.Binary(
        string="Banner Image",
        help="Upload a banner image for the appeal."
    )
    appeal_type = fields.Selection(
        [
            ('annual', 'Annual'),
            ('emergency', 'Emergency'),
            ('goal_oriented', 'Goal-Oriented')
        ],
        string="Appeal Type",
        help="Select the type of appeal for this product.",
        required=True
    )
    partner_ids = fields.One2many(
        'appeal.partners',
        'appeal_id',
        string="Appeal Partners",
        help="List of partners associated with this appeal."
    )
    total_contribution = fields.Float(
        string="Total Contribution",
        default="40"
    )
    total_partners = fields.Integer(
        string="Total Partners",
        compute='_compute_total_partners',
        store=True,
        help="The total number of partners contributing to this appeal."
    )
    # payment_count = fields.Integer(
    #     string="Payment Count",
    #     compute='_compute_payment_count',
    #     store=True,
    #     help="The total number of payments associated with this appeal."
    # )

    # @api.depends('partner_ids')
    # def _compute_payment_count(self):
    #     for appeal in self:
    #         appeal.payment_count = self.env['account.payment'].search_count([
    #             ('id', 'in', appeal.partner_ids.mapped('payment_id').ids)
    #         ])


    @api.depends('partner_ids')
    def _compute_total_partners(self):
        for appeal in self:
            appeal.total_partners = len(appeal.partner_ids)

    # @api.depends('partner_ids.contribution')
    # def _compute_total_contribution(self):
    #     for appeal in self:
    #         appeal.total_contribution = sum(appeal.partner_ids.mapped('contribution'))

    @api.model
    def action_view_source_payments(self):
            return {
                'type': 'ir.actions.act_window',
                'name': 'Source Payments',
                'res_model': 'account.payment',
                'view_mode': 'tree,form',
                'domain': [('id', 'in', self.partner_ids.mapped('payment_id').ids)],
            }


class AppealPartners(models.Model):
    _name = 'appeal.partners'
    _description = 'Appeal Partners'

    partner_id = fields.Many2one(
        'res.partner',
        string="Partner",
        help="The partner associated with the appeal."
    )
    contribution = fields.Float(
        string="Contribution",
        help="The amount contributed by the partner."
    )
    appeal_id = fields.Many2one(
        'appeal.template',
        string="Appeal",
        help="The appeal associated with this partner."
    )
    payment_id = fields.Many2one(
        'payment.transaction',
        string="Payment",
        help="The payment associated with the partner's contribution."
    )
