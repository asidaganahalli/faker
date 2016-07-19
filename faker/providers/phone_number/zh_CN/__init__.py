# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '86'
    phonenumber_prefixes = [134, 135, 136, 137, 138, 139, 147, 150,
                            151, 152, 157, 158, 159, 182, 187, 188,
                            130, 131, 132, 145, 155, 156, 185, 186,
                            145, 133, 153, 180, 181, 189]
    formats = [str(i) + '########' for i in phonenumber_prefixes]


    @classmethod
    def phonenumber_prefix(cls):
        return cls.random_element(cls.phonenumber_prefixes)
