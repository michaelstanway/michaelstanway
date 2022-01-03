# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:01:21 2021

@author: micha
"""

import numpy as np

def maxheight(v_0, theta):
    a = 0.1
    g = 9.81
    t = np.log((v_0*a*np.sin(theta)+g)/g)/a
    y = -g*t/a-(v_0*np.sin(theta)+g/a)*np.exp(-a*t)/a + (v_0*np.sin(theta)+g/a)/a
    return y



