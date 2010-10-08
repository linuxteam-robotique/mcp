# -*- coding: utf-8 -*-

R_vitesse       = 0x01 # vitesse des moteurs
R_rampe         = 0x02 # vitesse de la rampe (en seconde): sur 8 bits
R_direction     = 0x03
R_brake         = 0x04 # Brake on/off: etat
R_rampe_on      = 0x05 # Rampe on/off: etat
R_codeur        = 0x06 # Nombres de pas compter sur le codeur
R_consigne_pas  = 0x07 # valeur de consigne -> avance de X pas
R_modes         = 0x08 # modes de fonctionnements
R_etats          = 0x09

C_commande       = 0x40 # l'alix nous envoie une commande pour le main + une valeur sur 8 ou 16 bits
C_eeprom         = 0x41 # change adresse sur le bus i2c du pic

M_default        = 0x00 # fonctionement libre
M_arret          = 0x01 # moteur a l'arret
M_avance_pas     = 0x03
M_avance_pas_asservie = 0x04
M_avance_vitesse_asservie = 0x05

MOTEUR_AVANCE = 0x00
MOTEUR_RECULE = 0x01
ROBOT_AVANCE = { 0x21: MOTEUR_AVANCE, 0x22: MOTEUR_AVANCE }
ROBOT_RECULE = { 0x21: MOTEUR_RECULE, 0x22: MOTEUR_RECULE }
ROTATION_DROITE = { 0x21: MOTEUR_AVANCE, 0x22: MOTEUR_RECULE }
ROTATION_GAUCHE = { 0x21: MOTEUR_RECULE, 0x22: MOTEUR_AVANCE }

V_MAXMAX = 0xFFFF # Vitesse Max
V_MAX = 0xFE00    # Vitesse 80% de V_Max à utiliser pour laisser un marge aux PIC
V_MED = 0x6666    # Vitesse Milieu
V_MIN = 0x3750    # Vitesse Min
V_STOP = 0x0000   # Arret

V_RAMPE_MAX = 0xff
V_RAMPE_MED = 0x80
V_RAMPE_MIN = 0x00

# Asservissement

R_Kp=0x10
R_Ki=0x11
R_Kd=0x12
R_lastError=0x13
R_vitesse_codeur=0x14

# Télémètres :
R_ANA0 = 0x0A
R_ANA1 = 0x0B
R_ANA2 = 0x0C
R_COMPARATEUR =	0x0F
V_COMPARATEUR = 0x30

# Carte Accessoires (0x23)

R_BALAI = 0x01
R_PELLE = 0x02

BALAI_AVALE = 0x01
BALAI_EJECT = 0x02
BALAI_OFF = 0x00

PELLE_OFF = 0x00
PELLE_MONTE = 0x01
PELLE_DESCENDS = 0x02

BRAKE_ON = 0x01
BRAKE_OFF = 0x00

RAMPE_ON = 0x01
RAMPE_OFF = 0x00

CM = 2.37244897
DEG = 0.43

COTE_BLEU=-1
COTE_JAUNE=1
