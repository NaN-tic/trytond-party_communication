#This file is part party_communication module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.pool import Pool
from .address import *
from .contact_mechanism import *

def register():
    Pool.register(
        Address,
        ContactMechanism,
        module='party_communication', type_='model')
