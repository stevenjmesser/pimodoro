#!/usr/bin/env python

import signal
import buttonshim
import pimodoro
import random
import time
import blinkt
from subprocess import call

buttonshim.set_pixel(0, 0, 0)

# Random lights will blink when first launched.
rand_r = random.randint(0, 255)
rand_g = random.randint(0, 255)
rand_b = random.randint(0, 255)

for x in range(16):
    pixels = random.sample(range(8), random.randint(1, 5))
    for i in range(8):
        if i in pixels:
            blinkt.set_pixel(i, rand_r, rand_g, rand_b)
        else:
            blinkt.set_pixel(i, 0, 0, 0)
    blinkt.show()
    time.sleep(0.05)

blinkt.clear()
blinkt.show()

# Press button A to start a pomodoro.
@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    pimodoro.lightsequence(255, 0, 0, 18.75)

# Press button B to start a short break.
@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    pimodoro.lightsequence(0, 255, 0, 1.5)

# Press button C to start a long break.
@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    pimodoro.lightsequence(0, 0, 255, 5.25)

# Press button E for to shut down.
@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e(button, pressed):
    blinkt.clear()
    blinkt.show()
    call("sudo shutdown now", shell=True)

signal.pause()
