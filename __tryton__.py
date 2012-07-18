#This file is part party_communication module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
{
    'name': 'Party Address Communnication',
    'name_ca_ES': 'Comunicació adresses de tercers',
    'name_es_ES': 'Comunicació dirección de terceros',
    'version': '2.4.0',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''Party Address Communnication (phones and email)''',
    'description_ca_ES': '''Comunicació adresses de tercers (telèfons i correu)''',
    'description_es_ES': '''Comunicación direcciones de terceros (teléfonos y correo)''',
    'depends': [
        'ir',
        'res',
        'party',
    ],
    'xml': [
        'address.xml',
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ]
}
