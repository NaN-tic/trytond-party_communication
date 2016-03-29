#This file is part party_communication module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval

__all__ = ['ContactMechanism']

STATES = {
    'readonly': ~Eval('active'),
    }


class ContactMechanism:
    __metaclass__ = PoolMeta
    __name__ = 'party.contact_mechanism'
    address = fields.Many2One('party.address', 'Address',
        domain=[('party', '=', Eval('party'))],
        ondelete='CASCADE', states=STATES, select=True,
        depends=['active', 'party'])

    @classmethod
    def create(cls, vlist):
        for values in vlist:
            if values.get('address'):
                address = Pool().get('party.address')(values.get('address'))
                values['party'] = address.party
        return super(ContactMechanism, cls).create(vlist)
