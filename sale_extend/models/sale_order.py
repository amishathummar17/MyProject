from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_comment = fields.Char(string="Customer Comment")
    maintain_partner_id = fields.Many2one('res.partner', string="Maintain Partner")

