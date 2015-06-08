# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['PurchaseLine']
__metaclass__ = PoolMeta


class PurchaseLine:
    __name__ = 'purchase.line'

    @fields.depends('_parent_product.product_suppliers',
        '_parent_purchase.party')
    def on_change_product(self):
        ProductSupplier = Pool().get('purchase.product_supplier')
        res = super(PurchaseLine, self).on_change_product()
        if not self.product:
            return res
        for product_supplier in self.product.product_suppliers:
            if product_supplier.party and product_supplier.name and (
                    self.purchase.party == product_supplier.party):
                supplier = product_supplier.party
                context = {}
                if supplier and supplier.lang:
                    context['language'] = supplier.lang.code

                with Transaction().set_context(context):
                    res['description'] = ProductSupplier(
                        product_supplier.id).rec_name
                break

        return res
