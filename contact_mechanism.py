#This file is part party_communication module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval
from trytond.transaction import Transaction

__all__ = ['ContactMechanism']
__metaclass__ = PoolMeta

STATES = {
    'readonly': ~Eval('active'),
    }
DEPENDS = ['active']


class ContactMechanism:
    "Contact Mechanism"
    __name__ = 'party.contact_mechanism'
    address = fields.Many2One('party.address', 'Address', readonly=True,
        ondelete='CASCADE', states=STATES, select=True, depends=DEPENDS)
