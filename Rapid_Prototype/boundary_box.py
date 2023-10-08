import board
import digitalio
import time
import audioio
import audiomp3
import adafruit_lis3dh
import random
import neopixel

# Set-up button
button = digitalio.DigitalInOut(board.A3)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP


# Set up speaker enable pin
enable = digitalio.DigitalInOut(board.D10)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True

speaker = audioio.AudioOut(board.A0)

sample = 'boundary.mp3'


# Setup Neopixel
NUM_PIXELS = 12  # NeoPixel ring length (in pixels)
BRIGHTNESS = 0.25 # Let's not blind everyone

# The power for the NeoPixels is not enabled by default (to save battery power)
# We need to turn on the power by setting pin D10 high
print("Enabling NeoPixel power!")
enable.direction = digitalio.Direction.OUTPUT
enable.value = True


pixel_pin = board.D5  # Change this to the pin you connected your Neopixel to
pixels = neopixel.NeoPixel(pixel_pin, NUM_PIXELS, brightness = BRIGHTNESS)

# Define colors
yellow = (255, 255, 0)
black = (0, 0, 0)  
red = (255, 0, 0) 
green = (0, 255, 0) 


# Define smiley face pattern
smiley_face = [ yellow, black, black, yellow, yellow, yellow, yellow, yellow, black, black, yellow, black]



color = green # start with green

# play audio fuunction
def play_audio():
    mp3stream = audiomp3.MP3Decoder(open(sample, "rb"))
    speaker.play(mp3stream)

while True:
    
    #choose color
    if random.randint(0, 1) == 0:
        color = green
    else:
        color = red

    pixels.fill(color)
    
    for i in range(70000):
        button_state = not button.value  # check button state (active LOW)
        if button_state:
            #play boundary song
            if color == red and (speaker.playing is False):
                #play audio
                play_audio()
                time.sleep(13)
                break
            # display smiley face
            elif color == green:
                # show smiley face when the color is green
                for i, color in enumerate(smiley_face):
                    pixels[i] = color
                time.sleep(6)
                break


