# This file is part of the stock_supply_supplier_description module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['PurchaseLine']


class PurchaseLine(metaclass=PoolMeta):
    __name__ = 'purchase.line'

    @fields.depends('_parent_product.product_suppliers',
        '_parent_purchase.party')
    def on_change_product(self):
        ProductSupplier = Pool().get('purchase.product_supplier')

        super(PurchaseLine, self).on_change_product()
        if not self.product or not self.purchase:
            return

        description = self.product.rec_name
        for product_supplier in self.product.template.product_suppliers:
            supplier = product_supplier.party
            if supplier and (self.purchase.party == supplier):
                context = {}
                if supplier and supplier.lang:
                    context['language'] = supplier.lang.code

                with Transaction().set_context(context):
                    self.description = ProductSupplier(
                        product_supplier.id).supplier_name or description
                break
