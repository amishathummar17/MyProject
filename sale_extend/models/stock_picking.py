from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit = "stock.picking"


    customer_comment = fields.Char(string="Customer Comment")


class Stockmove(models.Model):
    _inherit = "stock.move"

    customer_comment = fields.Char(string="Customer Comment")

    def _get_new_picking_values(self):
        res = super(Stockmove, self)._get_new_picking_values()
        res.update({
            'customer_comment': self.customer_comment
        })
        return res

class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_dest_id, name, origin, company_id,values):
        res = super(StockRule, self)._get_stock_move_values(product_id, product_qty, product_uom, location_dest_id, name, origin, company_id,
                               values)
        res.update({
            'customer_comment': values.get('customer_comment')
        })
        return res

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _prepare_procurement_values(self, group_id=False):
        res = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        res.update({'customer_comment': self.order_id.customer_comment})
        return res
