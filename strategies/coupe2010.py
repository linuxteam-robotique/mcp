# -*- coding: utf-8 -*-

from time import sleep

from utils import Thread
from robot import *
from config import *
from constants import *
import threading

class Homologation(Thread):
    name = "Homologation"

    def run(self):
        self.log.warning("DEBUT DE STRATEGIE %s" % self.name)
        self.robot.rampe_on = RAMPE_ON
        self.robot.rampe = 10

        self.robot.accessoires.balais.write(BALAI_AVALE)

        print "AVANCE "*80        
        self.robot.brake = BRAKE_OFF
        self.robot.vitesse = V_MED

        self.avance(distance=150, mouvement=ROBOT_AVANCE)
        sleep(1)
        while self.en_mouvement():
            if self.stop_asap:
                self.stop_thread()
            sleep(0.1)

        print "DROITE "*80
        self.avance(angle=90, mouvement=ROTATION_GAUCHE)
        sleep(1)
        while self.en_mouvement():
            if self.stop_asap:
                self.stop_thread()
            sleep(0.1)

        print "AVANCE "*80
        self.avance(distance=120, mouvement=ROBOT_AVANCE)
        sleep(1)
        while self.en_mouvement():
            if self.stop_asap:
                self.stop_thread()
            sleep(0.1)
        print "AVANCE "*80
        self.avance(distance=125, mouvement=ROBOT_AVANCE)
        sleep(1)
        while self.en_mouvement():
            if self.stop_asap:
                self.stop_thread()
            sleep(0.1)

        print "DROITE "*80
        self.avance(angle=90, mouvement=ROTATION_DROITE)
        sleep(1)
        while self.en_mouvement():
            if self.stop_asap:
                self.stop_thread()
            sleep(0.1)

        print "AVANCE "*80
        self.avance(distance=120, mouvement=ROBOT_AVANCE)
        sleep(1)
        while self.en_mouvement():
            if self.stop_asap:
                self.stop_thread()
            sleep(0.1)
        self.robot.accessoires.balais.write(BALAI_EJECT)
        self.robot.accessoires.pelle.write(PELLE_MONTE)

        self.log.warning("FIN DE STRATEGIE")

class Match(Thread):
    name = "StrategieMatch"

    def run(self):
        self.log.warning("DEBUT DE STRATEGIE %s" % self.name)
        self.log.warning("FIN DE STRATEGIE")
