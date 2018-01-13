#!/usr/bin/env python

# Press button A, lights turn on and gradually dim.

import signal
import buttonshim
import blinkt
import time
import numpy as np

blinkt.clear()

step_down = 187.5 / 20
test_step_down = 0.05

# Press button A to start a Pomodoro.
@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    blinkt.set_all(255, 0, 0, brightness=0.2)
    for x in range(7, -1, -1):
        for i in np.arange(0.2, 0, -0.01):
            blinkt.set_pixel(x, 255, 0, 0, brightness=i)
            blinkt.show()
            time.sleep(test_step_down)

signal.pause()
