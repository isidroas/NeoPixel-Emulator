from neopixel_emulator import NeoPixelEmulator


gui = NeoPixelEmulator(window_w=1920, window_h=1080, caption='hola que psa', resizable=True)
gui.draw_leds(51)
gui.render()
gui.draw_color(3, (255,0,0))
gui.draw_color(29, (0,255,0))
gui.render()
input()

