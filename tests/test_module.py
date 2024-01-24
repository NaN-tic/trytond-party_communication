
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool


class PartyCommunicationTestCase(ModuleTestCase):
    'Test PartyCommunication module'
    module = 'party_communication'

    @with_transaction()
    def test_address(self):
        'Create address'
        pool = Pool()
        Party = pool.get('party.party')
        Address = pool.get('party.address')
        ContactMechanism = pool.get('party.contact_mechanism')

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
        self.assertEqual(len(address.contact_mechanisms), 2)
        self.assertEqual(address.email, 'demo@demo.com')
        self.assertEqual(address.phone, '+34935531803')

        c1, _ = address.contact_mechanisms
        self.assertEqual(c1.address, address)

        address.email = 'hello@demo.com'
        address.save()
        self.assertEqual(address.email, 'hello@demo.com')

        c3 = ContactMechanism()
        c3.address = address
        c3.type = 'email'
        c3.value = 'suport@demo.com'
        c3.is_default = True
        c3.save()

        self.assertEqual(len(address.contact_mechanisms), 3)
        self.assertEqual(address.party, party1)
        self.assertEqual(address.email, 'suport@demo.com')

        address.email = ''
        address.save()
        self.assertEqual(len(address.contact_mechanisms), 2)

del ModuleTestCase
