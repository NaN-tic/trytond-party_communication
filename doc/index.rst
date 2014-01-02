Contact Mechanisms in Parties and Addresses
###########################################

This module adds a relationship between the contact media (phone, mobile, email,
...) and the address of a party. Thus it may be known that a contact media
belongs to a specific address.

The address of a contact media is not a required field. Therefore, if a contact
media does not have an address, it means it is a general contact media of the
party (for example a corporate phone or a web site).

At the technical level, certain functional fields are available to get contact
media from an address:

 * address.phone
 * address.mobile
 * address.fax
 * address.email
 * address.skype
