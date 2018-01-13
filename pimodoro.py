#!/usr/bin/env python

import signal
import buttonshim
import blinkt
import time
import numpy as np

blinkt.clear()

# Set Pomodoro, short break and long break lengths in minutes below. Multiply by 60.

pomodoro = 25 * 60
short_break = 2 * 60
long_break = 7 * 60

# Stepdown times to fade the lights.
pom_step_down = (pomodoro / 8) / 20
sb_step_down = (short_break / 8 ) / 20
lb_step_down = (long_break / 8) / 20
test_step_down = 0.05

# Press button A to start a Pomodoro.
@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    blinkt.set_all(255, 12, 0, brightness=0.2)
    for x in range(7, -1, -1):
        for i in np.arange(0.2, 0, -0.01):
            blinkt.set_pixel(x, 255, 12, 0, brightness=i)
            blinkt.show()
            time.sleep(pom_step_down)

# Press button B to start a short break.
@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    blinkt.set_all(71, 255, 71, brightness=0.2)
    for x in range(7, -1, -1):
        for i in np.arange(0.2, 0, -0.01):
            blinkt.set_pixel(x, 71, 255, 71, brightness=i)
            blinkt.show()
            time.sleep(sb_step_down)

# Press button C to start a long break.
@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    blinkt.set_all(99, 71, 255, brightness=0.2)
    for x in range(7, -1, -1):
        for i in np.arange(0.2, 0, -0.01):
            blinkt.set_pixel(x, 99, 71, 255, brightness=i)
            blinkt.show()
            time.sleep(lb_step_down)

signal.pause()
