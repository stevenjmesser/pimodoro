#!/usr/bin/env python

import buttonshim
import blinkt
import time
import numpy as np

blinkt.clear()

# A light sequence.
def lightsequence(r, g, b, fade_time):
    blinkt.set_all(r, g, b, brightness=0.1)
    for x in range(7, -1, -1):
        for i in np.arange(0.1, 0, -0.01):
            blinkt.set_pixel(x, r, g, b, brightness=i)
            blinkt.show()
            time.sleep(fade_time)
