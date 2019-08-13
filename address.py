# This file is part party_communication module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval

__all__ = ['Address']

STATES = {
    'readonly': ~Eval('active'),
    }


class Address(metaclass=PoolMeta):
    __name__ = 'party.address'
    contact_mechanisms = fields.One2Many('party.contact_mechanism', 'address',
        'Contact Mechanisms', domain=[
            ('party', '=', Eval('party')),
            ], add_remove=[],
        states={
            'readonly': ~Eval('active'),
            }, depends=['active', 'party'])
    phone = fields.Function(fields.Char('Phone'),
        'get_address_contact_mechanism')
    mobile = fields.Function(fields.Char('Mobile'),
        'get_address_contact_mechanism')
    fax = fields.Function(fields.Char('Fax'),
        'get_address_contact_mechanism')
    email = fields.Function(fields.Char('E-Mail'),
        'get_address_contact_mechanism')
    skype = fields.Function(fields.Char('Skype'),
        'get_address_contact_mechanism')
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
        pool = Pool()
        ContactMechanism = pool.get('party.contact_mechanism')

        mechanisms = ContactMechanism.search([
            ('address', '=', self),
            ('type', '=', name),
            ], order=[('write_date', 'DESC')], limit=1)
        if mechanisms:
            return mechanisms[0].value
        return None

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
