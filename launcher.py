#!/usr/bin/env python

import signal
import buttonshim
import pimodoro
import random
import time

from blinkt import set_clear_on_exit, set_pixel, show, clear

# Random lights will blink when first launched.
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

for x in range(16):
    pixels = random.sample(range(8), random.randint(1, 5))
    for i in range(8):
        if i in pixels:
            set_pixel(i, r, g, b)
        else:
            set_pixel(i, 0, 0, 0)
    show()
    time.sleep(0.05)

clear()
show()

# Press button A to start a pomodoro.
@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    pimodoro.pomodoro()

# Press button B to start a short break.
@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    pimodoro.shortbreak()

# Press button C to start a long break.
@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    pimodoro.longbreak()

signal.pause()
