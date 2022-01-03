# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:51:11 2020

@author: micha
"""

import pandalab_base

class MyArduino(pandalab_base.ArduinoBase):
    def digital_pin_mode(self, pin, mode ="output"):
            if mode == "input":
                mode = "i"
            elif mode == "output":
                mode = "o"
            else:
                mode = "o"

            cmd = "m{:02d}".format(pin) + mode
            self.send_command(cmd)

    def query_pin_mode(self, pin):
            cmd = "q{:02d}".format(pin)
            self.send_command(cmd)
            return self.read()
