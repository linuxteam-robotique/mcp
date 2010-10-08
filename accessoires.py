# -*- coding: utf-8 -*-

from devices import *
from constants import *

class Telemetre(PICDevice):
    def __init__(self, address, name=None):
        super(Telemetre, self).__init__(address, name)
        self.ana0 = ByteRegister(self, address=R_ANA0, name="Ana0")
        self.comparateur = ByteRegister(self, address=R_COMPARATEUR, name="Comparateur", default=V_COMPARATEUR)

class Accessoires(PICDevice):
    def __init__(self, address, name=None):
        super(Accessoires, self).__init__(address, name)
        self.balais = ByteRegister(self, address=R_BALAI, name="Balai", default=BALAI_OFF)
        self.pelle = ByteRegister(self, address=R_PELLE, name="Pelle", default=PELLE_OFF)

__all__ =  ["Telemetre"]
