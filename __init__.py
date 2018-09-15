#This file is part party_communication module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.

from trytond.pool import Pool
from . import address
from . import contact_mechanism

def register():
    Pool.register(
        address.Address,
        contact_mechanism.ContactMechanism,
        module='party_communication', type_='model')
