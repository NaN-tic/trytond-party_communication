#This file is part of Tryton.  The COPYRIGHT file at the top level
#of this repository contains the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool

class Address(ModelSQL, ModelView):
    "Address"
    _name = 'party.address'
    _description = __doc__
    phone = fields.Char('Phone')
    mobile = fields.Char('Mobile')
    fax = fields.Char('Fax')
    email = fields.Char('E-Mail')
    skype = fields.Char('Skype')

Address()
