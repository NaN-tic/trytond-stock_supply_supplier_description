# This file is part of the stock_supply_supplier_description module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['ProductSupplier']
__metaclass__ = PoolMeta


class ProductSupplier:
    __name__ = 'purchase.product_supplier'

    supplier_name = fields.Function(fields.Char('Supplier Name'),
        'on_change_with_supplier_name')

    @fields.depends('code', 'name', 'product')
    def on_change_with_supplier_name(self, name=None):
        if self.code and self.name:
            return '[' + self.code + '] ' + self.name
        elif self.code and not self.name:
            return '[' + self.code + '] ' + self.product.name
        elif self.name:
            return self.name
        return
