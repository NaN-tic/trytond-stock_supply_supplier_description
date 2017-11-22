# This file is part of the stock_supply_supplier_description module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['CreatePurchase']


class CreatePurchase:
    __metaclass__ = PoolMeta
    __name__ = 'purchase.request.create_purchase'

    @classmethod
    def compute_purchase_line(cls, request, purchase):
        '''Create purchase line with supplier code and description'''
        ProductSupplier = Pool().get('purchase.product_supplier')

        line = super(CreatePurchase, cls).compute_purchase_line(request,
            purchase)

        description = request.product.rec_name
        for product_supplier in request.product.product_suppliers:
            supplier = product_supplier.party
            if supplier and (request.party == supplier):
                context = {}
                if supplier and supplier.lang:
                    context['language'] = supplier.lang.code

                with Transaction().set_context(context):
                    line.description = ProductSupplier(
                        product_supplier.id).supplier_name or description
                break
        return line
