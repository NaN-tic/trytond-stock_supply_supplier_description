# This file is part of the stock_supply_supplier_description module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .product import *
from .purchase import *
from .purchase_request import *


def register():
    Pool.register(
        PurchaseLine,
        ProductSupplier,
        module='stock_supply_supplier_description', type_='model')
    Pool.register(
        CreatePurchase,
        module='stock_supply_supplier_description', type_='wizard')
