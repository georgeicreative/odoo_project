from odoo import models,fields,api

class WebStudent(models.Model):
    _name='web.student'
    _description='The good models'

    priority = fields.Selection([('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very High')], string='priority')
    color=fields.Integer(string="color")
    active=fields.Boolean(string="active",default=True)
    progress=fields.Integer(string="Progress",compute="_compute_progress")
    name=fields.Char(string="NAME")
    sid=fields.Char(string='SID')
    doc_id = fields.Many2one("web.hobyx", string="doc_id")
    capitalized_name = fields.Char(string='Capitalized Name',compute='_compute_capitalized_name')

    def _compute_capitalized_name(self):

        self.capitalized_name="george"

    @api.depends('priority')
    def _compute_progress(self):
        for rec in self:
            if rec.priority == '0':
                progress=0
            if rec.priority == '1':
                progress=25
            if rec.priority == '2':
                progress=50
            if rec.priority == '3':
                progress=100
            else:
                progress=0
        self.progress=progress


    @api.onchange('name')
    def _onchange_name(self):
        print("donnneeee")
