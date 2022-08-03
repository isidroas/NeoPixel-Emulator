import pyglet
import math
import os
from pathlib import Path

CHIP_IMAGE = Path(__file__).parent / "ws2812b.png"
CIRCLE_IMAGE = Path(__file__).parent / "circle.png"

class NeoPixelEmulator(pyglet.window.Window):
    def __init__(self, resizable=True, caption='neopixel-emulator'):
        super().__init__(resizable=resizable, caption=caption)
        self.batch = pyglet.graphics.Batch()
        self.sprites = []
        self.color_sprites = []
        self.led_group = pyglet.graphics.OrderedGroup(0)
        self.color_group = pyglet.graphics.OrderedGroup(1)
        self.alive = 1

    def draw_leds(self, led_number):
        led_width = int(self.width / led_number)

        for pos in range(led_number):
            img = pyglet.image.load(CHIP_IMAGE)
            sprite_chip = pyglet.sprite.Sprite(
                    img=img,
                    batch=self.batch,
                    x=pos * led_width,
                    y=int(self.height/2),
                    group=self.led_group,
                )
            sprite_chip.scale = led_width/ sprite_chip.width
            self.sprites.append(
                sprite_chip
            )

            img=pyglet.image.load(CIRCLE_IMAGE)
            sprite_circle= pyglet.sprite.Sprite(
                    img=img,
                    batch=self.batch,
                    x=pos * led_width,
                    y=int(self.height/2),
                    group=self.color_group,
                )
            sprite_circle.color = (0, 0, 0)
            sprite_circle.opacity = 200
            sprite_circle.scale = led_width/ sprite_circle.width
            self.color_sprites.append(sprite_circle)


    def map(self, input_val, in_min, in_max, out_min, out_max):
        output = (input_val - in_min) / (in_max - in_min) * (
            out_max - out_min
        ) + out_min
        return output

    def draw_color(self, led_position, color):
        self.color_sprites[led_position].color = color

    def on_draw(self):
        self.render()

    def render(self):
        self.clear()
        self.batch.draw()
        event = self.dispatch_events()
        self.flip()
