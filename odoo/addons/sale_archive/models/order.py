from odoo import models, fields


class SaleOrderArchive(models.Model):
    _name = 'sale.order.archive'
    _description = "Sale Order Archives"

    # name (text), Order create Date, Count of order lines (int)
    display_name = fields.Char(string='Display Name')
    create_date = fields.Datetime(string='Order create date')
    order_lines = fields.Integer(string='Count of Order Lines')
