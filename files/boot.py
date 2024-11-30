import os
import sdcard
from machine import Pin, SPI

spi = SPI(2, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
sd = sdcard.SDCard(spi, Pin(15))
os.mount(sd, "/sd")

MAIN_PROGRAM = "/sd/main.py"
if os.path.exists(MAIN_PROGRAM):
    with open(MAIN_PROGRAM) as f:
        exec(f.read())
else:
    print("main.py not found on SD card.")
