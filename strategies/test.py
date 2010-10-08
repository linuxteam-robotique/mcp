# -*- coding: utf-8 -*-

from time import sleep

from utils import Thread
from robot import *
from config import *
from constants import *
import threading

class StrategieAvancePas(Thread):
    name = "AvancePas"

    def run(self):
        self.log.warning("DEBUT DE STRATEGIE %s" % self.name)
        self.robot.rampe_on = RAMPE_ON
        self.robot.rampe = 0x50

        self.robot.accessoires.balais.write(BALAI_AVALE)

        print "AVANCE "*80        
        self.robot.brake = BRAKE_OFF
        self.robot.vitesse = V_MAX

        self.avance(distance=70, mouvement=ROBOT_AVANCE)
        self.avance(angle=29, mouvement=ROTATION_GAUCHE)
        self.avance(distance=120, mouvement=ROBOT_AVANCE)
        self.avance(angle=50, mouvement=ROTATION_DROITE)
        self.avance(distance=140, mouvement=ROBOT_AVANCE)

        # print "DROITE "*80
        # self.avance(angle=80, mouvement=ROTATION_GAUCHE)
        # sleep(1)
        # self.robot.rampe = 10
        # while self.en_mouvement():
        #     if self.stop_asap:
        #         self.stop_thread()
        #     sleep(0.1)

        # print "AVANCE "*80
        # self.avance(distance=120, mouvement=ROBOT_AVANCE)
        # sleep(1)
        # self.robot.rampe = 10
        # while self.en_mouvement():
        #     if self.stop_asap:
        #         self.stop_thread()
        #     sleep(0.1)
        # print "AVANCE "*80
        # self.avance(distance=40, mouvement=ROBOT_AVANCE)
        # sleep(1)
        # self.robot.rampe = 10
        # while self.en_mouvement():
        #     if self.stop_asap:
        #         self.stop_thread()
        #     sleep(0.1)

        # print "DROITE "*80
        # self.avance(angle=45, mouvement=ROTATION_DROITE)
        # sleep(1)
        # self.robot.rampe = 10
        # while self.en_mouvement():
        #     if self.stop_asap:
        #         self.stop_thread()
        #     sleep(0.1)

        # print "AVANCE "*80
        # self.avance(distance=50, mouvement=ROBOT_AVANCE)
        # sleep(1)
        # self.robot.rampe = 10
        # while self.en_mouvement():
        #     if self.stop_asap:
        #         self.stop_thread()
        #     sleep(0.1)

        # print "DROITE "*80
        # self.avance(angle=45, mouvement=ROTATION_DROITE)
        # sleep(1)
        # self.robot.rampe = 10
        # while self.en_mouvement():
        #     if self.stop_asap:
        #         self.stop_thread()
        #     sleep(0.1)

        # self.robot.accessoires.balais.write(BALAI_EJECT)
        # self.robot.accessoires.pelle.write(PELLE_MONTE)

        self.log.warning("FIN DE STRATEGIE")

class StrategieBasic(Thread):
    name = "Basic"

    def run(self):
        self.log.warning("DEBUT DE STRATEGIE %s" % self.name)
        self.robot.rampe_on = RAMPE_OFF
        self.robot.rampe = V_RAMPE_MED
        self.robot.vitesse = V_MAX
        self.robot.accessoires.balais.write(BALAI_AVALE)

        # self.robot.brake = BRAKE_OFF
        # self.robot.mouvement = ROBOT_AVANCE
        # self.robot.mode = M_default
        self.avance(distance=0x25, mouvement=ROBOT_AVANCE)
        sleep(1)
        # while(not self.pnr):
        #     if self.stop_asap:
        #         self.stop_thread()
        #     if self.robot_adverse_here():
        #         if self.robot.md.etat.value & 4:
        #             m = self.robot.mg
        #         else:
        #             m = self.robot.md
        #         m.direction.write(MOTEUR_RECULE)
        #         self.wait_telemetre_free()
        #         m.direction.write(MOTEUR_AVANCE)
        #     if self.obstacle_detecte():
        #          self.robot.md.direction.write(MOTEUR_RECULE)
        #          self.robot.mg.direction.write(MOTEUR_RECULE)
        #          sleep(2)
        #          self.robot.md.direction.write(MOTEUR_AVANCE)
        #          self.robot.mg.direction.write(MOTEUR_AVANCE)
        #     sleep(0.1)
        # self.log.warning("POINT OF NO RETURN")
        # self.robot.mouvement = ROTATION_DROITE
        # sleep(2)
        # self.robot.vitesse = V_STOP
        # self.robot.accessoires.balais.write(BALAI_EJECT)
        while not self.stop_asap:
            sleep(0.1)

        self.log.warning("FIN DE STRATEGIE")

class StrategieTempo(Thread):
    name = "Tempo"

    def run(self):
        self.log.warning("DEBUT DE STRATEGIE %s" % self.name)
        self.robot.rampe_on = RAMPE_ON
        self.robot.rampe = V_RAMPE_MED
        self.robot.brake = BRAKE_OFF
        self.robot.vitesse = V_MAX
        self.robot.mouvement = ROBOT_AVANCE
        self.robot.accessoires.balais.write(BALAI_AVALE)
        self.robot.mode = M_default
        sleep(3)
        self.robot.mouvement = ROTATION_GAUCHE
        sleep(0.6)
        self.robot.mouvement = ROBOT_AVANCE
        sleep(5)
        self.robot.mouvement = ROTATION_DROITE
        sleep(0.5)
        self.robot.vitesse = V_STOP
        self.accessoires.balais.write(BALAI_EJECT)
        while not self.stop_asap:
            sleep(0.1)
        self.log.warning("FIN DE STRATEGIE")
