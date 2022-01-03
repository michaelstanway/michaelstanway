# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:49:07 2021

@author: micha
"""

import pandalab as pl
import numpy as np
import matplotlib . pyplot as plt

arduino = pl.Arduino("/dev/tty.usbmodem14301")

v_0 = []
v_1 = []

for i in range (101) :
    arduino.analogue_write_v(5*i/100)
    v_0.append(arduino.analogue_read_av_v(0, 100))
    v_1.append(arduino.analogue_read_av_v(1, 100))

arduino.analogue_write_v(0)
arduino.close()

v_0 = np.array(v_0)
v_1 = np.array(v_1)

fig, ax = plt.subplots()
ax.scatter(v_0, v_1)
plt.show()

filename = input("Enter a file name: ")

with open(filename, "w") as data_file:
    data_file.write("Vin (V), Vled (V)\n")
    for i in range(len(v_0)):
        data_file.write("{},{}\n".format(v_0[i], v_1[i]))