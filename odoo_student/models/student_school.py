from odoo import fields, models,_, api

class StudentSchool(models.Model):
    _name = "student.school"

    name = fields.Char("Name")
