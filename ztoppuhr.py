#!/usr/bin/env python3

"""
Async Stopwatch using ZeroSeg
"""
__author__ = 'Richard Hull <rm_hull@yahoo.co.uk>'
__date__ = '07 November 2016'
__version_info__ = (0, 1, 0)
__version__ = '%s.%s.%s' % __version_info__
__license__ = 'MIT'

import asyncio
import functools
import os
import signal

import max7219.led as led
import RPi.GPIO as GPIO

import const as button

# GPIO buttons
button.a = 17
button.b = 26


class Stopwatch:

    def __init__(self, device, delta, loop):
        self.device = device
        self.delta = delta
        self.loop = loop
        self.reset(None)
        loop.call_soon(self.__ticker)

    def __ticker(self):
        if self.running is True:
            self.device.write_number(0, self.counter, decimalPlaces=3)
            self.counter = self.counter + self.delta
        self.loop.call_later(self.delta, self.__ticker)

    def reset(self, channel):
        self.counter = 0
        self.running = False
        self.device.write_number(0, self.counter, decimalPlaces=3)

    def pause(self, channel):
        self.running = not self.running


def init_gpio(stopwatch):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button.a, GPIO.IN)
    GPIO.setup(button.b, GPIO.IN)
    GPIO.add_event_detect(button.a, GPIO.FALLING, callback=functools.partial(stopwatch.pause), bouncetime=200)
    GPIO.add_event_detect(button.b, GPIO.RISING, callback=functools.partial(stopwatch.reset), bouncetime=200)


def ask_exit(signame, device):
    print("got signal %s: exit" % signame)
    device.clear()
    loop.stop()


device = led.sevensegment()
loop = asyncio.get_event_loop()
stopwatch = Stopwatch(device, 0.043, loop)
init_gpio(stopwatch)

for signame in ('SIGINT', 'SIGTERM'):
    loop.add_signal_handler(getattr(signal, signame),
                            functools.partial(ask_exit, signame, device))

print("Event loop running forever, press Ctrl+C to interrupt.")
print("pid %s: send SIGINT or SIGTERM to exit." % os.getpid())


try:
    loop.run_forever()
finally:
    loop.close()
