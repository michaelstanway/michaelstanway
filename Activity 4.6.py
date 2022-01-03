
"""
pandalab_led

LED measurement for PH2012 electronics lab
Paul A. S. Cruickshank
2021
"""

import pandalab as pl
import numpy as np
import matplotlib.pyplot as plt

arduino = pl.Arduino("COM3")

v_0 = []
v_1 = []

for i in range(301):
    arduino.analogue_write_v(5)
    v_0.append(arduino.analogue_read_av_v(0,100))
    v_1.append(arduino.analogue_read_av_v(1,100))

arduino.analogue_write_v(0)
arduino.close()

v_0 = np.array(v_0)
v_1 = np.array(v_1)

fig, ax = plt.subplots()
ax.scatter(v_0,v_1)
ax.set_title("Vout against Vin")
ax.set_xlabel("Pin 3 (V)")
ax.set_ylabel("Pin 2 (V)")
plt.show()

filename = input("Enter a file name:  ")

with open(filename, "w") as data_file:
    data_file.write("Pin 3 (V), Pin 2 (V)\n")
    for i in range(len(v_0)):
        data_file.write("{},{}\n".format(v_0[i], v_1[i]))

