from odoo import fields, api, models


class Websale(models.Model):
    _inherit = 'sale.order'
    _description = "this is order"

    sale_disc = fields.Char(string='sale_disc')
    tqnt=fields.Float(string='Total')



