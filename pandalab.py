#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:21:02 2020

@author: paul
"""

import serial
import time

print("Importing pandalab")


class Arduino:
    """
    Tools for communicating with an Arduino programmed with 
    """
    
    def __init__(self, serial_port_name="/dev/tty.usbmodem301"):
        """
        Constructor

        Parameters
        ----------
        serial_port_name : string, optional
            DESCRIPTION. The name of the serial port your Arduino
            appears as, e.g., "COM4" or "/dev/tty.usbmodem301".

        Returns
        -------
        None.

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
        Query the Arduino for a string containing software version number

        Returns
        -------
        string
            String containing software version number.

        """
        
        cmd = "i"
        self.send_command(cmd)

        self.info = self.read()
        return self.info

    def send_command(self, command):
        """
        Send a command to the Arduino
        Automatically adds terminating new-line character
        Example usage: arduino.send_command("d03wh")

        Parameters
        ----------
        command : string
            The command you wish to send to the Arduino.

        Returns
        -------
        None.

        """
        
        if self.__port.is_open:
            cmd = command + "\n"
            self.__port.write(cmd.encode("utf-8"))
        else:
            print("The connection to the Arduino is closed")

    def read(self):
        """
        Read from the Arduino.
        Expects new-line termination
        Automatically removes terminating carriage-return and new-line

        Returns
        -------
        string 
            Response from the Arduino.

        """
        if self.__port.is_open:
            return self.__port.read_until().decode("utf-8")[:-2]
        else:
            print("The connection to the Arduino is closed")
            return None

    def close(self):
        """
        Close serial port connection to Arduino
        

        Returns
        -------
        None.

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

    def digital_pin_mode(self, pin, mode="output"):
        """
        Set the mode for an Arduino digital pin

        Parameters
        ----------
        pin : integer
            Valid pins for Arduino UNO are 2 to 13 (inclusive).
        mode : string, optional
            Valid modes are "input" and "output". The default is "output".

        Returns
        -------
        None.

        """
        if mode == "input":
            mode = "i"
        elif mode == "output":
            mode = "o"
        else:
            mode = "o"
        if pin in range(2, 14):
            cmd = "m{:02d}".format(pin) + mode
            self.send_command(cmd)
        else:
            print("digital_pin_mode: only valid for pins 2 to 13")

    def query_pin_mode(self, pin):
        """
        Query the mode for an Arduino digital pin
        
        Parameters
        ----------
        pin : integer
            Valid pins for are 2 to 13 (inclusive).

        Returns
        -------
        string
            For a valid pin: "input" or "output". Otherwise "query_pin_mode: invalid pin".

        """
        if pin in range(2, 14):
            cmd = "q{:02d}".format(pin)
            self.send_command(cmd)
            return self.read()
        else:
            return("query_pin_mode: invalid pin")

    def digital_write(self, pin, state):
        """
        Set the value of a digital pin high (5V) or low (0V)

        Parameters
        ----------
        pin : integer
            Valid pins for are 2 to 13 (inclusive).
        state : string
            Pin output state. Valid oopens are "high" (5V), "low" (0V).

        Returns
        -------
        None.

        """
        if pin in range(2, 14):
            if state == "high":
                state = "h"
            elif state == "low":
                state = "l"
            else:
                state = "l"

            cmd = "d{:02d}w".format(pin) + state + "\n"
            self.send_command(cmd)
        else:
            print("digital_write: only valid for pins 2 to 13")

    def digital_read(self, pin):
        """
        Read voltage on a digital pin

        Parameters
        ----------
        pin : integer
            Valid pins for are 2 to 13 (inclusive).

        Returns
        -------
        string
            Response from the Arduino.

        """
        if pin in range(2, 14):
            cmd = 'd{:02d}r'.format(pin) + '\n'
            self.send_command(cmd)
            time.sleep(0.01)
            return self.read()

        else:
            print("digital_read: only valid for pins 2 to 13")

    def analogue_read(self, pin):
        """
        

        Parameters
        ----------
        pin : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        if pin in (0, 1, 2, 3, 4, 5):
            cmd = 'a{:01d}'.format(pin)
            self.send_command(cmd)
            return int(self.read())
        else:
            print('analogue_read: pin {} does not support analogue measurement'.format(pin))

    def analogue_read_v(self, pin):
        """
        

        Parameters
        ----------
        pin : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        if pin in (0, 1, 2, 3, 4, 5):
            return (5/1023)*self.analogue_read(pin)

        else:
            print('analogue_read: pin {} does not support analogue measurement'.format(pin))

    def analogue_read_av_v(self, pin, n_av):
        """
        

        Parameters
        ----------
        pin : TYPE
            DESCRIPTION.
        n_av : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        if pin in (0, 1, 2, 3, 4, 5):
            cmd = 'v{:01d}{:03d}'.format(pin, n_av)
            self.send_command(cmd)
            response = self.read()

            return (5/(1023*n_av))*int(response)
        else:
            print('analogue_read: pin {} does not support analogue measurement'.format(pin))

    def analogue_ref_default(self):
        """
        

        Returns
        -------
        None.

        """
        cmd = 'rd'
        self.send_command(cmd)

    def analogue_ref_internal(self):
        """
        

        Returns
        -------
        None.

        """
        cmd = 'ri'
        self.send_command(cmd)

    def analogue_ref_external(self):
        """
        

        Returns
        -------
        None.

        """
        cmd = 're'
        self.send_command(cmd)

    def analogue_write(self, value):
        """
        

        Parameters
        ----------
        value : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if value < 0:
            value = 0
        if value > 4095:
            value = 4095
        cmd = "o{:04d}".format(value)
        self.send_command(cmd)

    def analogue_write_v(self, voltage):
        """
        

        Parameters
        ----------
        voltage : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if voltage < 0:
            voltage = 0
        if voltage > 5:
            voltage = 5
        value = int(voltage * 4095 / 5)
        cmd = "o{:04d}".format(value)
        self.send_command(cmd)

    def pwm_write(self, pin, value):
        """
        

        Parameters
        ----------
        pin : TYPE
            DESCRIPTION.
        value : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if pin in (3, 5, 6, 9, 10, 11):
            cmd = 'p{:02d}{:03d}'.format(pin, value)
            self.send_command(cmd)
        else:
            print('pwm_write: pin {} does not support pwm'.format(pin))

    def tone(self, freq):
        """
        

        Parameters
        ----------
        freq : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        cmd = 't{:04d}'.format(freq)
        self.send_command(cmd)
