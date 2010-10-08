#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from i2c import *
from motor import Motor
from accessoires import Telemetre, Accessoires
from config import motors, telemetres, pic_accessoires
from constants import *

class WriteOnlyRegisterException(Exception):
    pass

class ReadOnlyRegisterException(Exception):
    pass

class MakeRobot(object):
    """
    THE ROBOT FACTORY (inc.)

    This robot is unique
    """
    _robot = None

    def __new__(cls):
        if not cls._robot:
            cls._robot = Robot()
        return cls._robot
    

class Robot(object):
    def __init__(self):
        for attr, motor in motors.iteritems():
            setattr(self, attr, Motor(**motor))

        for attr, telemetre in telemetres.iteritems():
            setattr(self, attr, Telemetre(**telemetre))

        self.accessoires = Accessoires(address=pic_accessoires['address'], name="Accessoires")

        self.log = logging.getLogger(self.__class__.__name__)
        self.log.info("READY !")
        self.log_status()

    """
    On Lève une exception pour les registres en lecture seule
    """
    def _read_only(self, x):
        raise ReadOnlyRegisterException()

    """
    On Lève une exception pour les registres en lecture seule
    """
    def _write_only(self):
        pass
    #raise WriteOnlyRegisterException()

    """
    Défini le mouvement à effectuer
    :m: ROBOT_AVANCE, ROBOT_RECULE, ROTATION_DROITE, ROTATION_GAUCHE
    """
    def _set_mouvement(self, m):
        self.log.debug("set_mouvement(%s)" % (m))
        for k,v in m.iteritems():
            if k == motors['md']['address']:
                self.md.direction.write(v)
            elif k == motors['mg']['address']:
                self.mg.direction.write(v)

    """
    Recupère le movement défini dans le pic
    :retourne: { adresse: direction }
    ex : {0x22: MOTEUR_AVANCE, 0x21: MOTEUR_RECULE} == ROTATION_DROITE
    """
    def _get_mouvement(self):
        self.log.debug("get_mouvement")
        return { self.md.address:self.md.direction, self.mg.address: self.mg.direction}

    mouvement = property(_write_only, _set_mouvement)


    """
    Défini la vitesse dans le PIC
    :v: La vitesse sur 16 bits
    """
    def _set_vitesse(self, v):
        self.log.debug("set_vitesse(%s)" % (v))
        self.md.vitesse.write(v)
        self.mg.vitesse.write(v)

    """
    Retourne la vitesse réglée dans le PIC
    example : {0x21: 0xFFFF, 0x22: 0xFFFF}
    """
    def _get_vitesse(self):
        self.log.debug("get_vitesse")
        return { self.md.address:self.md.vitesse, self.mg.address: self.mg.vitesse}


    vitesse = property(_write_only, _set_vitesse)

    """
    Défini la vitesse de la rampe
    :v: 1/v seconde sur 8 bit dans le PIC
    """
    def _set_rampe(self, v):
        self.log.debug("set_rampe(%s)" % (v))
        self.md.rampe.write(v)
        self.mg.rampe.write(v)

    """
    Retourne la vitesse de la rampe dans le PIC
    """
    def _get_rampe(self):
        self.log.debug("get_rampe")
        return { self.md.address:self.md.rampe, self.mg.address: self.mg.rampe}

    rampe = property(_write_only, _set_rampe)

    """
    Défini la distance a parcourir par le moteur
    Fonctionne uniquement dans le mode avance_pas et avance_pas_asservie
    :d: en pas sur 16 bits
    """
    def _set_consigne_pas(self, d):
        self.log.debug("set_consigne_pas(%s)" % (d))
        self.md.consigne_pas.write(d)
        self.mg.consigne_pas.write(d)


    """
    Retourne la distance restant a parcourir
    lire le registre de set_consigne_pas ?
    """
    def _get_consigne_pas(self):
        self.log.debug("get_consigne_pas")
        return { self.md.address:self.md.consigne_pas, self.mg.address: self.mg.consigne_pas}

    consigne_pas = property(_write_only, _set_consigne_pas)

    """
    Règle le mode de moteur
    """
    def _set_mode(self, m):
        self.log.debug("set_mode(%s)" % (m))
        self.md.mode.write(m)
        self.mg.mode.write(m)

    """
    Récupère le mode du moteur
    """
    def _get_mode(self):
        self.log.debug("get_mode")
        return { self.md.address:self.md.mode, self.mg.address: self.mg.mode}

    mode = property(_write_only, _set_mode)

    """
    Défini le Brake
    en i2c : 0 = pas de frein, 1 = Frein
    """
    def _set_brake(self, b):
        self.log.debug("set_brake(%s)" % (b))
        self.md.brake.write(b)
        self.mg.brake.write(b)

    """
    Récupère le Brake
    """
    # def _get_brake(self):
    #     self.log.debug("get_brake")
    #     return { self.md.address:self.md.brake, self.mg.address: self.mg.brake}

    brake = property(_write_only, _set_brake)

    """
    Active/Désactive la Rampe
    """
    def _set_rampe_on(self, b):
        self.log.debug("set_rampe_on(%s)" % (b))
        self.md.rampe_on.write(b)
        self.mg.rampe_on.write(b)

    """
    Etat de la Rampe
    en i2c : 0 = Rampe, 1 = Pas de Rampe
    """
    def _get_rampe_on(self):
        self.log.debug("get_rampe_on")
        return { self.md.address:self.md.rampe_on, self.mg.address: self.mg.rampe_on}

    rampe_on = property(_write_only, _set_rampe_on)

    """
    Récupère la valeur des codeur (16bits)
    """
    def _get_codeur(self):
        return { self.md.address:self.md.codeur, self.mg.address: self.mg.codeur}

    codeurs = property(_write_only, _read_only)

    """
    Retourne la vitesse instantanée mesurée par le PIC
    """
    def _vitesse_codeur(self):
        return { self.md.address:self.md.vitesse_codeur, self.mg.address: self.mg.vitesse_codeur}

    vitesse_codeur = property(_write_only, _read_only)

    @property
    def devices(self):
        for attr in dir(self):
            if isinstance(getattr(self, attr), I2CDevice):
                yield getattr(self, attr)

    """
    :return: True si la tirette est dans le robot, False si-non
    """
    def tirette(self):
        if self.md.etat.read() & 1:
            return False
        else:
            return True

    def log_status(self):
        self.log.info("Workshop #3")
        for device in self.devices:
            device.log_status()
        self.log.info("EndLog")

__all__ = ["MakeRobot", "Robot"]
