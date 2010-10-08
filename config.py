# -*- coding: utf-8 -*-

DUREE_MATCH = 20
PNR = 20
LAG = 0.1
LAG_EVITEMENT = 0.5

bus_id = 0 # identifiant du bus i2c

motors = { # Les moteurs du robot
    'md': {'address': 0x22, 'name': "Moteur Droit" },
    'mg': {'address': 0x21, 'name': "Moteur Gauche" }
    }

telemetres = {
    'tg': {'address': 0x21, 'name': "Télémetre Gauche"},
    'td': {'address': 0x22, 'name': "Télémetre Droite"}
}

pic_accessoires = { 'address': 0x23, 'name': "Accessoires" }
