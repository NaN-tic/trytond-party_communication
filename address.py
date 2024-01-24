# This file is part party_communication module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval


class Address(metaclass=PoolMeta):
    __name__ = 'party.address'
    phone = fields.Function(fields.Char('Phone'),
        'get_address_contact_mechanism', setter='set_address_contact_mechanism')
    mobile = fields.Function(fields.Char('Mobile'),
        'get_address_contact_mechanism', setter='set_address_contact_mechanism')
    fax = fields.Function(fields.Char('Fax'),
        'get_address_contact_mechanism', setter='set_address_contact_mechanism')
    email = fields.Function(fields.Char('E-Mail'),
        'get_address_contact_mechanism', setter='set_address_contact_mechanism')
    skype = fields.Function(fields.Char('Skype'),
        'get_address_contact_mechanism', setter='set_address_contact_mechanism')
    phones = fields.Function(fields.Char('Phones'),
        'get_address_contact_mechanisms')
    mobiles = fields.Function(fields.Char('Mobiles'),
        'get_address_contact_mechanisms')
    faxs = fields.Function(fields.Char('Faxs'),
        'get_address_contact_mechanisms')
    emails = fields.Function(fields.Char('E-Mails'),
        'get_address_contact_mechanisms')
    skypes = fields.Function(fields.Char('Skypes'),
        'get_address_contact_mechanisms')

    def get_address_contact_mechanism(self, name):
        contact_mechanism = self.contact_mechanism_get(name, usage='is_default')
        return contact_mechanism and contact_mechanism.value

    def get_address_contact_mechanisms(self, name):
        '''
        Get all contact mechanisms of type name (without last 's') separated
        by comma from the party address
        '''
        name = name[:-1]
        values = []
        for mechanism in self.contact_mechanisms:
            if mechanism.type == name and mechanism.value:
                values.append(mechanism.value)
        return ','.join(values)

    @classmethod
    def set_address_contact_mechanism(cls, addresses, name, value):
        ContactMechanism = Pool().get('party.contact_mechanism')

        for address in addresses:
            cm = ContactMechanism.search([
                    ('address', '=', address.id),
                    ('type', '=', name),
                    ], limit=1)
            if cm and value:
                ContactMechanism.write([cm[0]], {'value': value})
            elif cm and not value:
                ContactMechanism.delete([cm[0]])
            else:
                ContactMechanism.create([{
                            'address': address,
                            'type': name,
                            'value': value,
                            }])
