# applications/leds.py: version: 2021-01-25 11:17
#
# To Do
# ~~~~~

import aiko.event
import aiko.oled

import machine
from machine import Pin

state = False

led0 = Pin(19, machine.Pin.OUT)
led1 = Pin(22, machine.Pin.OUT)

def blink():
    global state
    state = not state

    if state:
        led0.value(True)
        led1.value(False)
    else:
        led1.value(True)
        led0.value(False)

def initialise():
    aiko.event.add_timer_handler(blink, 250, immediate=True)
