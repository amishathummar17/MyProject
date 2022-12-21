from odoo import fields, models,_, api

class StdMark(models.Model):
    _name = "std.mark"

    std_id = fields.Many2one("std.student", string="Std")
    sub = fields.Char(string="Subject")
    total = fields.Float(string="Total")
    percentage = fields.Float(string="Percentage")
    get_mark = fields.Float(string="Get Mark")
    email = fields.Char(string="Email")


