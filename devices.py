# -*- coding: utf-8 -*-
from i2c import I2CDevice
from structure import *
from constants import C_commande

import logging

class ReadOnlyRegisterException(Exception):
    pass

"""
:parent: PICDevice
:address: PICDevice's address on the bus
"""
class Register(object):
    def __init__(self, parent, address, name=None, verbose=False, default=None):
        self.log = logging.getLogger(self.__class__.__name__)
        self.verbose = verbose
        self.parent = parent
        self.address = address
        if default is not None:
            self.write(default)
            self.value = default
        if name is None:
            self.name = self.__class__.__name__
        else:
            self.name = name

    def log_status(self):
        if self.verbose:
            self.log.info("%15s@0x%02x → 0x%04x" % (self.name, self.address, self.read()))

class ByteRegister(Register, Byte):
    def read(self):
        self.value =  self.parent.read(self.address, len=1)[0]
        return self.value

    def write(self, value):
        if isinstance(value, int):
            value = Byte(value)
        self.parent.write(C_commande , [ self.address ] + value.to_i2c)


class WordRegister(Register, Word):
    def read(self):
        array =  self.parent.read(self.address, len=2)
        self.array.first = array[0]
        self.array.second = array[1]
        return self.value
    def write(self, value):
        if isinstance(value, int):
            value = Word(value)
        self.parent.write(C_commande , [ self.address ] + value.to_i2c)


class PICDevice(I2CDevice):

    @property
    def registers(self):
        for attr in dir(self):
            if isinstance(getattr(self, attr), Register):
                yield getattr(self, attr)

    def log_status(self):
        super(PICDevice, self).log_status()
        for register in self.registers:
            register.log_status()


__all__ = [ "PICDevice", "WordRegister", "ByteRegister", "ReadOnlyRegisterException" ]
