from odoo import fields, models,_, api

class StdStudent(models.Model):
    _name = "std.student"
    _rec_name = "name_id"

    name_id = fields.Many2one('res.partner', string="Name")
    std = fields.Char(string="Standard")
    school_id = fields.Many2one("student.school", string="School")
    total = fields.Float(string="Total", compute="_compute_total_percentage", store=True)
    percentage = fields.Float(string="Percentage", compute="_compute_total_percentage", store=True)
    mark_ids = fields.One2many("std.mark", 'std_id', string="Mark")
    sub = fields.Char(string="Subject")
    get_mark = fields.Float(string="Get Mark")
    phone = fields.Char(string="Phone")
    type = fields.Selection([('distinction', 'Distinction'), ('first class', 'First Class'), ('second class', 'Second Class'), ('pass class', 'Pass Class'), ('fail', 'Fail')], compute="_compute_type", string="Type")

    @api.depends('percentage')
    def _compute_type(self):
        for record in self:
            if record.percentage > 80:
                record.type = 'distinction'
            if record.percentage < 80:
                record.type = 'first class'
            if record.percentage < 60:
                record.type = 'second class'
            if record.percentage < 50:
                record.type = 'pass class'
            if record.percentage < 35:
                record.type = 'fail'

    @api.onchange('name_id')
    def _onchange_name_id(self):
        self.phone = self.name_id.phone

    @api.depends('mark_ids')
    def _compute_total_percentage(self):
        for record in self:
            record.total = sum(record.mark_ids.mapped('get_mark'))
            perc = sum(record.mark_ids.mapped('total'))
            if record.total != 0:
                record.percentage = (record.total * 100) / perc





