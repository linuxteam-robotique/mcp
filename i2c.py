# -*- coding: utf-8 -*-

from smbus import SMBus
from config import bus_id
from time import sleep

import logging

class I2CBus(object):
    """
    Singleton of SMBus

    @todo : Implémenter un Thread pour ecrire de façon non bloquante sur le bus
    de façon a ce que le programme puisse faire des écritures sans attendre la fin de l'envois des données. le read devra etre bloquant

    @idée : faire une queue du genre ({mode: read ou write, address: 0x21, registre: R_modes, valeur: M_avance_pas })
    """
    _bus = None
    def __new__(cls, *args, **kwargs):
        if not cls._bus:
            cls._bus = SMBus(bus_id)
        return cls._bus

class I2CDevice(object):
    """
    Generic class for each i²c devices
    """
    _bus = I2CBus()
    def __init__(self, address, name):
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.debug("address=%x, name=%s" % (address, name))
        self.address = address
        self.name = name

    """
    :register: Adresse du Registre
    :len: La longueure des données a lire en octets (default: 1)
    :return: La valeur du Registre
    """
    def read(self, register, len=1):
        try:
            result =  self._bus.read_i2c_block_data(self.address, register, len)
        except IOError, e:
            self.log.critical("I²C Read Error %s (device=%x, register=%x)", e, self.address, register)
            result = []
            for a in range(0,len):
                result.append(0)
        self.log.debug("read: address=%x, registre=%x, len=%i, result=%s" % (self.address, register, len, result))
        sleep(0.02)
        return result

    """
    On envois les données au pic par le registre 0x40
    :register: Adresse du Registre
    :value: Valeur à envoyer au registre
    """
    def write(self, register, value):
        self.log.debug("write: address=%x, registre=%x, value=%s" % (self.address, register, value))
        try:
            self._bus.write_i2c_block_data(self.address, register, value)
        except IOError, e:
            self.log.critical("I²C Write Error %s (device=%x, register=%s, value=%s)", e, self.address, register, type(value))
        sleep(0.05)

    def log_status(self):
        self.log.info("%s@0x%x" % (self.name, self.address))

if __name__ == "__main__":
    print "test du bus i2c"
    b = I2CBus()
    from datetime import datetime
    d = datetime.now()
    print b.read_i2c_block_data(0x21, 0x09, 1)
    print datetime.now() - d
    d = datetime.now()
    print b.read_i2c_block_data(0x22, 0x09, 1)
    print datetime.now() - d
    d = datetime.now()
    b.write_i2c_block_data(0x21, 0x40, [0x01, 0xff, 0x34])
    sleep(0.1)
    b.write_i2c_block_data(0x21, 0x40, [0x08, 0x03])
    sleep(0.1)
    b.write_i2c_block_data(0x22, 0x40, [0x08, 0x03])
    sleep(0.1)
    b.write_i2c_block_data(0x22, 0x40, [0x01, 0xff, 0x34])
    print datetime.now() - d

__all__ = ["I2CDevice"]
