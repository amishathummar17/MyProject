from odoo import fields, models,_, api

class AddressPhone(models.Model):
    _name = "address.phone"
    _rec_name = "address_id"

    type = fields.Selection([('mobile', 'Mobile'), ('work', 'Work'), ('home', 'Home'), ('other', 'Other')], string="Type", default='mobile')
    number = fields.Char(string="Number")
    email = fields.Char(string="Email")
    address_id = fields.Many2one("address.book", string="Address")
    sequence = fields.Integer(string="Sequence")
