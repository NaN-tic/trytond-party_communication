# This file is part of the party_communication module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool


class PartycommunicationTestCase(ModuleTestCase):
    'Test Party Communication module'
    module = 'party_communication'

    @with_transaction()
    def test_address(self):
        'Create address'
        pool = Pool()
        Party = pool.get('party.party')
        Address = pool.get('party.address')
        party1, = Party.create([{
                    'name': 'Party 1',
                    }])

        address, = Address.create([{
                    'party': party1.id,
                    'street': 'St sample, 15',
                    'city': 'City',
                    'email': 'demo@demo.com',
                    'phone': '+34935531803'
                    }])
        self.assertTrue(address.id)
        self.assertEqual(address.email, 'demo@demo.com')

        address.email = 'hello@demo.com'
        address.save()
        self.assertEqual(address.email, 'hello@demo.com')

        address.email = ''
        address.save()
        self.assertEqual(address.email, None)

def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartycommunicationTestCase))
    return suite
