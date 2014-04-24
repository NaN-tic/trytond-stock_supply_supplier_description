# This file is part of the stock_supply_supplier_description module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['ProductSupplier']
__metaclass__ = PoolMeta


class ProductSupplier:
    __name__ = 'purchase.product_supplier'

    def get_rec_name(self, name):
        if self.code and self.name:
            return '[' + self.code + '] ' + self.name
        elif self.name:
            return self.name
        else:
            if self.product.code:
                return '[' + self.product.code + '] ' + self.product.name
            else:
                return self.product.name
