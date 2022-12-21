from odoo import fields, models, api, _

class ResPartner(models.Model):
    _inherit = "res.partner"

    student = fields.Char(string="Student")
    student_ids = fields.One2many("std.student", "name_id", string="Student")
