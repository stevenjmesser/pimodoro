#!/usr/bin/env python

import signal
import buttonshim
import pimodoro

@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    pimodoro.pomodoro()

@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    pimodoro.shortbreak()

@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    pimodoro.longbreak()

signal.pause()
