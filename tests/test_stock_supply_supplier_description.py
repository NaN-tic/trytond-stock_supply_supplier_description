#!/usr/bin/env python
# This file is part of the stock_supply_supplier_description module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.tests.test_tryton import test_depends
import os
import sys
import trytond.tests.test_tryton
import unittest


class StockSupplySupplierDescriptionTestCase(unittest.TestCase):
    'Test Stock Supply Supplier Description module'

    def setUp(self):
        trytond.tests.test_tryton.install_module(
            'stock_supply_supplier_description')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockSupplySupplierDescriptionTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
