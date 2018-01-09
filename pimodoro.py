#!/usr/bin/env python

# Simply testing how to light pixels on button presses for now.

import signal
import buttonshim
import blinkt
import time

blinkt.set_brightness(0.1)

@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    blinkt.clear()
    blinkt.set_pixel(7, 255, 0, 0)
    blinkt.show()

@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    blinkt.clear()
    blinkt.set_pixel(6, 255, 127, 0)
    blinkt.show()

@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    blinkt.clear()
    blinkt.set_pixel(5, 255, 255, 0)
    blinkt.show()

@buttonshim.on_press(buttonshim.BUTTON_D)
def button_d(button, pressed):
    blinkt.clear()
    blinkt.set_pixel(4, 0, 255, 0)
    blinkt.show()

@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e(button, pressed):
    blinkt.clear()
    blinkt.set_pixel(3, 0, 0, 255)
    blinkt.show()

signal.pause()
