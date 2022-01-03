# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:52:18 2020

@author: micha
"""

"""
pandalab_base.py

@author: Paul cruickshank
"""

import serial
import time

print("Importing pandalab_base")


class ArduinoBase:
    """
    Bare-bones class to handle communication with an Arduino

    Example usage: arduino = ArduinoBase("COM4")
    """
    def __init__(self, serial_port_name="/dev/tty.usbmodem14201"):
        """
        Constructor
        """
        self.__port = serial.Serial(serial_port_name, baudrate=115200, timeout=2)
        time.sleep(2)
        self.port_name = serial_port_name
        self.info = self.identify()

    def __repr__(self):
        if self.__port.is_open:
            return "[ArduinoBase on port %s, %s]" % (self.port_name, self.info)
        else:
            return self.info

    def identify(self):
        """
        Query Arduino for pandalab software version
        """
        cmd = "i"
        self.send_command(cmd)

        self.info = self.read()
        return self.info

    def send_command(self, command):
        """
        Send command string to Arduino

        Automatically adds terminating new-line character
        Example usage: arduino.send_command("d03wh")
        """
        if self.__port.is_open:
            cmd = command + "\n"
            self.__port.write(cmd.encode("utf-8"))
        else:
            print("The connection to the Arduino is closed")

    def read(self):
        """
        Read string from Arduino
        Expects new-line termination
        Automatically removes terminating carriage-return and new-line
        """
        if self.__port.is_open:
            return self.__port.read_until().decode("utf-8")[:-2]
        else:
            print("The connection to the Arduino is closed")
            return None

    def close(self):
        """
        Close serial port connection to Arduino
        """
        if self.__port.is_open:
            self.__port.close()
            self.info = "ArduinoBase: no connection"
        else:
            print("The connection to the Arduino is closed")

    def __enter__(self):
        return self

    def __exit__(self, *arguments):
        self.close()

    def qopen(self):
        return self.__port.is_open
