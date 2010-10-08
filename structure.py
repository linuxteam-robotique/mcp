# -*- coding: utf-8 -*-

from ctypes import *
import logging

class Byte(c_ubyte):
    @property
    def to_i2c(self):
        return [ self.value ]

class ByteArray(Structure):
    _fields_ = [("first", c_ubyte), ("second", c_ubyte)]

    @property
    def to_i2c(self):
        return [ self.first, self.second ]

class Word(Union):
    _fields_ = [("value", c_ushort), ("array", ByteArray)]

    @property
    def to_i2c(self):
        return self.array.to_i2c

__all__ = ["Word", "Byte", "sizeof"]
