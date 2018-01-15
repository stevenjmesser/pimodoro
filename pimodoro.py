#!/usr/bin/env python

from blinkt import set_all, set_pixel, show, clear
import time
import numpy as np

# A light sequence.
def lightsequence(r, g, b, fade_time):
    set_all(r, g, b, brightness=0.2)
    for x in range(7, -1, -1):
        for i in np.arange(0.2, 0, -0.01):
            set_pixel(x, r, g, b, brightness=i)
            show()
            time.sleep(fade_time)
