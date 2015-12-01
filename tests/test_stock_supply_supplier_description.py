# This file is part of the stock_supply_supplier_description module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockSupplySupplierDescriptionTestCase(ModuleTestCase):
    'Test Stock Supply Supplier Description module'
    module = 'stock_supply_supplier_description'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockSupplySupplierDescriptionTestCase))
    return suite
