# -*- coding: utf-8 -*-

import logging
from time import sleep

from robot import MakeRobot
from config import *
from constants import *
from strategies import unit, test, coupe2010
from utils import Thread
import threading

class EndOfTimeException(Exception):
    pass


class McpThreads(object):
    _threads = None

    def __new__(cls):
        if not cls._threads:
            cls._threads = []
        return cls._threads

class Logguer(Thread):
    name = "Logguer"

    def run(self):
        self.log.warning("DEBUT DE LOGGUER")
        while not self.stop_asap:
            self.robot.log_status()
            sleep(0.1)
        self.log.warning("FIN DE LOGGUER")


class Match(object):

    """
    :TODO: Prendre en paramettre la statégie/scénario a charger
    """
    def __init__(self):
        self.log = log = logging.getLogger(self.__class__.__name__)

    """
    = Déroulement =

    * Attente de Tirette Sortie
    * lance Log
    * lance Startégie
    * sleep 90
    * Quitte Strategie
    * Arret Moteurs et accessoires
    * Quitte Log
    * Attente remise en place de la tirette
    """
    def deroulement_match(self):
        match_timer = threading.Timer(DUREE_MATCH, self.end_of_match)
        backhome_timer = threading.Timer(PNR, self.back_home)
        robot = MakeRobot()
        #strategie = test.StrategieBasic()
        strategie = test.StrategieAvancePas()
        #strategie = unit.AvaleRecrache()
        
        #strategie = coupe2010.Homologation()
        #strategie = coupe2010.Match()
        logguer = Logguer()
        
        self.threads = McpThreads()
        self.threads.append(strategie)
        self.threads.append(logguer)

        # robot.accessoires.balais.write(BALAI_EJECT)
        robot.accessoires.pelle.write(PELLE_MONTE)

        self.log.warning("ROBOT OK METTRE LA TIRETTE")
        while(not robot.tirette()):
            sleep(0.01)

        robot.accessoires.pelle.write(PELLE_DESCENDS)
        sleep(0.75)
        robot.accessoires.pelle.write(PELLE_OFF)
        
        self.log.warning("ATTENTE SORTIE DE TIRETTE")
        while(robot.tirette()):
            sleep(0.01)

        self.log.warning("DEBUT DE MATCH")
        match_timer.start()
        backhome_timer.start()
        strategie.start()
        logguer.start()
        strategie.join(timeout=DUREE_MATCH)

        robot.brake = BRAKE_ON
        robot.vitesse = V_STOP
        robot.accessoires.balais.write(BALAI_OFF)
        self.log.warning("FIN DE MATCH strategie.isAlive() = %s" % strategie.isAlive() )
        #robot.log_status()

    def back_home(self):
        print "BACK TO HOME"
        for thread in self.threads:
            self.log.warning("Thread %s Point of No Return" % (thread.name))
            thread.pnr = True

    def end_of_match(self):
        print "END OF MATCH"
        for thread in self.threads:
            self.log.warning("STOP Thread %s" % (thread.name))
            thread.stop_asap = True

__all__ = ["Match"]
