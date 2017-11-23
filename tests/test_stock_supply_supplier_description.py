# This file is part of the stock_supply_supplier_description module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import doctest_setup, doctest_teardown


class StockSupplySupplierDescriptionTestCase(ModuleTestCase):
    'Test Stock Supply Supplier Description module'
    module = 'stock_supply_supplier_description'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockSupplySupplierDescriptionTestCase))
    from trytond.modules.company.tests import test_company
    for test in test_company.suite():
        if test not in suite and not isinstance(test, doctest.DocTestCase):
            suite.addTest(test)
    suite.addTests(doctest.DocFileSuite(
            'scenario_stock_supplier_description.rst',
            setUp=doctest_setup, tearDown=doctest_teardown, encoding='UTF-8',
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    return suite
