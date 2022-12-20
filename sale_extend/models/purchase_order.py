from odoo import fields, models, api

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    maintain_partner_id = fields.Many2one('res.partner', string="Maintain Partner")