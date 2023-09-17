# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.3

while True:
    led[0] = (0, 0, 102) #Blue = solitude/loneliness
    time.sleep(3)

    led[0] = (255, 255, 0) #Yellow = hope in meeting someone new
    time.sleep(1)

    #Loop to emphasize the crush that has developed
    for x in range(1, 3):
        led[0] = (0, 0, 102) #Blue = solitude/loneliness
        time.sleep(2)

        led[0] = (255, 255, 0) #Yellow = hopefullness
        time.sleep(1)

        led[0] = (255, 80, 80) # Light Pink = crush
        time.sleep(2)

    led[0] = (0, 0, 102) #Blue = solitude/loneliness
    time.sleep(1)

    led[0] = (255, 255, 0) #Yellow = hopefullness
    time.sleep(1)

    brightPink_time = 5
    red_time = 1

    #Loop as the relationship becomes unhealthy
    #Bright Pink becomes shorter and Red becomes longer
    for i in range (0, 3):
        led[0] = (255, 0, 102) #Pink = Full relationship
        time.sleep(brightPink_time - (2*i))
        led[0] = (139, 0, 0) # Red = Abusive elements
        time.sleep(red_time + (2*i))

    led[0] = (255, 255, 255)  #Clean break = white
    time.sleep(3)

