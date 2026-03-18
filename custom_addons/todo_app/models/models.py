# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class todo_app(models.Model):
#     _name = 'todo_app.todo_app'
#     _description = 'todo_app.todo_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    deadline = fields.Date(string='Deadline')
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
    ], string='Priority', default='0')
    is_done = fields.Boolean(string='Done', default=False)
    active = fields.Boolean(default=True)