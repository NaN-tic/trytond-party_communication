#This file is part party_communication module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval


class ContactMechanism(metaclass=PoolMeta):
    __name__ = 'party.contact_mechanism'

    @classmethod
    def create(cls, vlist):
        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if values.get('address'):
                address = Pool().get('party.address')(values.get('address'))
                values['party'] = address.party
        return super(ContactMechanism, cls).create(vlist)
