from odoo import api,fields,models

class saleOrder(models.Model):
    _inherit='sale.order.line'

    total=fields.Float(string='Total123',compute='_compute_total',)

    def _compute_total(self):
        for rec in self:
            rec.total=rec.product_template_id.qty_available