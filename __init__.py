# This file is part of the stock_supply_supplier_description module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import product
from . import purchase
from . import purchase_request


def register():
    Pool.register(
        purchase.PurchaseLine,
        product.ProductSupplier,
        module='stock_supply_supplier_description', type_='model')
    Pool.register(
        purchase_request.CreatePurchase,
        module='stock_supply_supplier_description', type_='wizard')
