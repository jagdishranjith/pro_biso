from odoo import models, fields, api
import csv
import base64
from io import StringIO

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    warehouse_id = fields.Many2one('stock.warehouse', check_company=False)




