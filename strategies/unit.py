# -*- coding: utf-8 -*-

from time import sleep

from utils import Thread
from robot import *
from config import *
from constants import *
import threading

class StrategieTest(Thread):
    name = "Test"

    def run(self):
        self.log.warning("DEBUT DE STRATEGIE %s" % self.name)
        for i in range(1,15):
            self.log.error(i)
            sleep(1)
            if self.stop_asap:
                self.stop_thread()
        self.log.warning("FIN DE STRATEGIE")


class StrategieRobotAdverse(Thread):
    name = "RobotAdverse"

    def run(self):
        self.log.warning("DEBUT DE STRATEGIE %s" % self.name)
        self.robot.rampe_on = RAMPE_ON
        self.robot.rampe = V_RAMPE_MED
        self.robot.brake = BRAKE_OFF
        self.robot.vitesse = V_MED
        self.robot.mouvement = ROBOT_AVANCE
        self.robot.mode = M_default
        cont = True
        while(cont):
            if self.stop_asap:
                self.stop_thread()
            if self.robot.md.etat.value & 4 or self.robot.mg.etat.value & 4:
                #self.robot.vitesse.write(V_STOP)
                self.robot.brake = BRAKE_ON
                cont = False
            sleep(0.1)

        self.log.warning("FIN DE STRATEGIE")


class AvaleRecrache(Thread):
    name = "AvaleRecrache"

    def run(self):
        self.log.warning("DEBUT DE STRATEGIE %s" % self.name)
        self.robot.accessoires.balais.write(BALAI_AVALE)

        while(not self.pnr):
            sleep(0.1)

        self.robot.accessoires.balais.write(BALAI_EJECT)
        self.robot.accessoires.pelle.write(PELLE_MONTE)
        sleep(1.5)
        self.robot.accessoires.pelle.write(PELLE_OFF)
        if self.stop_asap:
            self.stop_thread()

        self.robot.accessoires.pelle.write(PELLE_DESCENDS)
        sleep(0.75)
        self.robot.accessoires.pelle.write(PELLE_OFF)

        self.log.warning("FIN DE STRATEGIE")
