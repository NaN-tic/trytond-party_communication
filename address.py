# This file is part party_communication module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Address']
__metaclass__ = PoolMeta

STATES = {
    'readonly': ~Eval('active'),
    }


class Address:
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
        for mechanism in self.contact_mechanisms:
            if mechanism.type == name:
                return mechanism.value
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
