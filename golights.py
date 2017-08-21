from gpiozero import LED
from time import sleep
import sys

redLightPin = 14
yellowLightPin = 15
greenLightPin = 18

redLED = LED(redLightPin)
yellowLED = LED(yellowLightPin)
greenLED = LED(greenLightPin)

greenLED.on()
sleep(1)
greenLED.off()
yellowLED.on()
sleep(1)
yellowLED.off()
redLED.on()
sleep(1)
redLED.off()


#a mistake
