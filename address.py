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
    phone = fields.Char('Phone')
    mobile = fields.Char('Mobile')
    fax = fields.Char('Fax')
    email = fields.Char('E-Mail')
    skype = fields.Char('Skype')

