#!/usr/bin/env python3

import time
import requests
import sys

import board
import busio
import digitalio

import adafruit_rfm9x

# Define radio parameters.
RADIO_FREQ_MHZ = 868.0  # Frequency of the radio in Mhz. Must match your
                        # module! Can be a value like 915.0, 433.0, etc.

CS = digitalio.DigitalInOut(board.CE1)
RESET = digitalio.DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

while True:
    msg = "Hi World!"
    msg_byles = bytes(msg, "utf-8")
    rfm9x.send(msg_byles)

    print("Sent:", msg_byles)
    time.sleep(5)
