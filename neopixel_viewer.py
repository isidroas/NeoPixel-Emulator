from emulator_backend import Adafruit_NeoPixel
from neopixel_effects import NeoPixel_Effects

def run():
    pixels = Adafruit_NeoPixel(51,6,"NEO_GRB + NEO_KHZ800")
    effects = NeoPixel_Effects(pixels)
    pixels.begin()
    pixels.setBrightness(100)
    pixels.setPixelColor(2,pixels.Color(255,0,0))
    pixels.show()
    input()
    pixels.clear()
    pixels.show()
    input()
    #pixels.show()

run()
