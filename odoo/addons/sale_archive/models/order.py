from odoo import models, fields


class SaleOrderArchive(models.Model):
    _name = 'sale.order.archive'
    _description = "Sale Order Archives"

    display_name = fields.Char(string='Display Name')
    create_date = fields.Datetime(string='Order create date')
    client_order_ref = fields.Reference([('res.partner', 'testy')], string='Customer Reference')
    member_ids = fields.Reference([('res.user', 'testy2')], string='SalePerson')
    currency_id = fields.Reference([('res.currency', 'testy3')], string='Order Currency')
    amount_total = fields.Monetary('Order Total Amount', currency_field="currency_id", string="Order Total Amount", store=True)
    order_lines = fields.Integer(string='Count of Order Lines')
