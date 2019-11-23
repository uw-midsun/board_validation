import glob
import logging

import serial
from serial import EIGHTBITS, PARITY_NONE


class UartDriver(object):
    """
        configurations:
            115200
            8
            N1
    """
    def __init__(self):
        self.serial = None

    def select_device(self):
        dev = glob.glob("/dev/*usbmodem*")
        if not dev:
            return glob.glob("/dev/*CMSIS*")[0]
        return dev[0]

    def connect(self):
        device = self.select_device()
        log.info("connecting to device at: %s" % device)
        self.serial = serial.Serial(device,
                                    baudrate=115200,
                                    bytesize=EIGHTBITS,
                                    parity=PARITY_NONE)
        return self

    def read(self):
        return self.serial.readline()

    def close(self):
        self.serial.close()
        self.serial = None


log = logging.getLogger("{}.{}".format(UartDriver.__module__, UartDriver.__name__))
