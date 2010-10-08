# -*- coding: utf-8 -*-

import threading
import logging
from robot import MakeRobot
from time import sleep
from datetime import datetime, timedelta
from config import *
from constants import *

class Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, target=self.run, args=()) 
        self.stop_asap = False
        self.pnr = False
        self.log = logging.getLogger(self.__class__.__name__)
        self.robot = MakeRobot()
        self.log.warning("init OK")

    def start(self):
        threading.Thread.start(self)

    def stop_thread(self):
        raise EndOfTimeException(self.stop_at)

    def avance(self, mouvement, distance=None, angle=None):
        self.robot.brake = BRAKE_OFF
        self.robot.mouvement = mouvement
        if distance is not None:
            self.robot.consigne_pas = int(distance*CM)
        elif angle is not None:
            self.robot.consigne_pas = int(angle*DEG)
        # self.robot.rampe = 0x50
        self.robot.mode = M_avance_pas

        sleep(1)

        self.robot.rampe = 10
        while self.en_mouvement():
            if self.stop_asap:
                self.stop_thread()
            sleep(0.1)

    def robot_adverse_here(self):
        return self.robot.md.etat.value & 4 or self.robot.mg.etat.value & 4

    def en_mouvement(self):
        return self.robot.md.etat.value & 2 or self.robot.mg.etat.value & 2

    def obstacle_detecte(self):
        return self.robot.md.vitesse_codeur.value == 0 or self.robot.md.vitesse_codeur.value == 0xffff or self.robot.mg.vitesse_codeur.value == 0 or self.robot.mg.vitesse_codeur.value == 0xffff

    def wait_telemetre_free(self):
        while self.robot_adverse_here():
            sleep(LAG_EVITEMENT)
            if self.stop_asap:
                self.stop_thread()
