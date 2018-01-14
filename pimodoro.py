#!/usr/bin/env python

import buttonshim
import blinkt
import time
import numpy as np

blinkt.clear()

# Set Pomodoro, short break and long break lengths in minutes below. Multiply by 60.

pom_len = 25 * 60
sb_len = 2 * 60
lb_len = 7 * 60

# Stepdown times to fade the lights.
pom_fade = (pom_len / 8) / 20
sb_step_down = (sb_len / 8 ) / 20
lb_step_down = (lb_len / 8) / 20

# A test fade to demo the sequence.
test_fade = 0.05

# A Pomodoro sequence.
def pomodoro():
    blinkt.set_all(255, 12, 0, brightness=0.2)
    for x in range(7, -1, -1):
        for i in np.arange(0.2, 0, -0.01):
            blinkt.set_pixel(x, 255, 12, 0, brightness=i)
            blinkt.show()
            time.sleep(test_fade)

# A short break sequence.
def shortbreak():
    blinkt.set_all(71, 255, 71, brightness=0.2)
    for x in range(7, -1, -1):
        for i in np.arange(0.2, 0, -0.01):
            blinkt.set_pixel(x, 71, 255, 71, brightness=i)
            blinkt.show()
            time.sleep(test_fade)

# A long break sequence.
def longbreak():
    blinkt.set_all(99, 71, 255, brightness=0.2)
    for x in range(7, -1, -1):
        for i in np.arange(0.2, 0, -0.01):
            blinkt.set_pixel(x, 99, 71, 255, brightness=i)
            blinkt.show()
            time.sleep(test_fade)
