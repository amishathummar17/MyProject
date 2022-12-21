from odoo import fields, models,_, api
from dateutil.relativedelta import relativedelta

class AddressBook(models.Model):
    _name = "address.book"
    _rec_name = "address"

    name_id = fields.Many2one('res.partner', string="Name")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    address_ids = fields.One2many("address.phone", 'address_id', string="Address")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    type = fields.Selection([('mobile', 'Mobile'), ('work', 'Work'), ('home', 'Home'), ('other', 'Other')], string="Type", default='mobile')

    @api.onchange('type')
    def _onchange_type(self):
        number = []
        email = []
        for obj in self.address_ids:
            if self.type == obj.type:
                number.append(obj.number)
                email.append(obj.email)
        self.phone = number and number[0] or ''
        self.email = email and email[0] or ''

    @api.onchange('name_id')
    def _onchange_name_id(self):
        self.address = self.name_id.street
        self.city = self.name_id.city
        self.zip = self.name_id.zip
        self.state_id = self.name_id.state_id

    # @api.depends('address_ids')
    # def _compute_phone_email(self):
    #     for rec in self:
    #       number = []
    #       email = []
    #       for obj in self.address_ids:
    #           number.append(obj.number)
    #           email.append(obj.email)
    #       self.phone = number and number[0] or ''
    #       self.email = email and email[0] or ''






