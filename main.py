from neopixel_emulator import NeoPixelEmulator


gui = NeoPixelEmulator(window_w=1765, window_h=400)
gui.draw_leds(30)
gui.render()
gui.draw_color(3, (255,0,0))
gui.draw_color(29, (0,255,0))
gui.render()
input()

