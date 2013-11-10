#This file is part party_communication module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Address']
__metaclass__ = PoolMeta


class Address:
    "Address"
    __name__ = 'party.address'
    contact_mechanism = fields.One2Many('party.contact_mechanism', 'address',
        'Contact Mechanism', readonly=True)
    address_phone = fields.Function(fields.Char('Phone'),
        'get_address_contact_mechanism')
    address_mobile = fields.Function(fields.Char('Mobile'),
        'get_address_contact_mechanism')
    address_fax = fields.Function(fields.Char('Fax'),
        'get_address_contact_mechanism')
    address_email = fields.Function(fields.Char('E-Mail'),
        'get_address_contact_mechanism')
    address_skype = fields.Function(fields.Char('Skype'),
        'get_address_contact_mechanism')

    def get_address_contact_mechanism(self, name):
        for mechanism in self.contact_mechanism:
            if mechanism.type == name:
                return mechanism.value
        return ''
