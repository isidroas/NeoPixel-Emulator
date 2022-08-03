from neopixel_emulator import NeoPixelEmulator


gui = NeoPixelEmulator()
gui.draw_leds(50)
gui.render()
gui.draw_color(0, (0,0,255))
gui.draw_color(3, (255,0,0))
gui.draw_color(29, (0,255,0))
gui.draw_color(49, (0,255,0))
gui.render()
input()

