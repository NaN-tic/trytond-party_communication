# This file is part of the party_communication module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class PartycommunicationTestCase(ModuleTestCase):
    'Test Party Communication module'
    module = 'party_communication'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartycommunicationTestCase))
    return suite
