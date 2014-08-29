============================================
Medios de contacto en empresas y direcciones
============================================

Añade una relación entre los medios de contacto (teléfono, móvil, email, ...) y
las direcciones de tercero. De este modo puede saberse que medios de contactos
pertenecen a una dirección concreta.

La dirección en un medio de contacto no es un campo requerido. Por tanto, si un
medio de contacto no dispone de dirección se entiende que es un medio de
contacto general del tercero (por ejemplo un teléfono corporativo o una web).

A nivel técnico se dispone de campos funcionales para obtener el primer medio de
contacto de una dirección de un cierto tipo:

 * address.phone
 * address.mobile
 * address.fax
 * address.email
 * address.skype

Y para obtener todos los medio de contacto de una dirección de un cierto tipo
separados por coma:

 * address.phones
 * address.mobiles
 * address.faxs
 * address.emails
 * address.skypes
