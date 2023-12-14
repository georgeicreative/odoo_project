from odoo import models,fields,api

class WebHobyx(models.Model):
    _name='web.hobyx'
    _description='The good models'

    name=fields.Char(string="HNAME")
    idh=fields.Char(string='IDH')
