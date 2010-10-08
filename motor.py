# -*- coding: utf-8 -*-

from devices import *
from constants import *

class Motor(PICDevice):
    def __init__(self, address, name=None):
        super(Motor, self).__init__(address, name)
        self.vitesse = WordRegister(self, address=R_vitesse, name="Vitesse", default=V_STOP)
        self.rampe = ByteRegister(self,  address=R_rampe, name="Vitesse Rampe", default=V_RAMPE_MED)
        self.brake = ByteRegister(self,  address=R_brake, name="Brake on/off", default=BRAKE_ON)
        self.rampe_on = ByteRegister(self,  address=R_rampe_on, name="Rampe on/off", default=RAMPE_ON)
        self.direction = ByteRegister(self, address=R_direction, name="Direction", default=MOTEUR_AVANCE)
        self.codeur = WordRegister(self, address=R_codeur, name="Codeur")
        self.consigne_pas = WordRegister(self, address=R_consigne_pas, name="Consigne Pas")
        self.mode = ByteRegister(self, address=R_modes, name="Mode", default=M_arret)
        self.etat = ByteRegister(self, address=R_etats, name="Etats", verbose=True)
        self.vitesse_codeur = WordRegister(self, address=R_vitesse_codeur, name="Vitesse codeur", verbose=True)
        self.Kp = ByteRegister(self, address=R_Kp, name="Kp", default=0x10)
        self.Ki = ByteRegister(self, address=R_Ki, name="Kp", default=0x10)
        self.Kd = ByteRegister(self, address=R_Kd, name="Kd", default=0x10)
        self.last_error = ByteRegister(self, address=R_lastError, name="Last Error")

__all__ = [ "Motor" ]
