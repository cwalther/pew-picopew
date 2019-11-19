# a demo for palette-based animation

import pew
import math

pew.init()
pew.palette((
	0, 0, 0,  0, 1, 0,  0, 7, 0,  0, 20, 0,  0, 42, 0,  0, 75, 0,  0, 121, 0,  0, 180, 0,
	0, 255, 0,  1, 255, 0,  4, 255, 0,  11, 255, 0,  24, 255, 0,  42, 255, 0,  68, 255, 0,  101, 255, 0,
	143, 255, 0,  143, 180, 0,  143, 121, 0,  143, 75, 0,  143, 42, 0,  143, 20, 0,  143, 7, 0,  143, 1, 0,
	143, 0, 0,  101, 0, 0,  68, 0, 0,  42, 0, 0,  24, 0, 0,  11, 0, 0,  4, 0, 0,  1, 0, 0
))

screen = pew.Pix()
for y in range(8):
	for x in range(8):
		rx = 2*x - 7
		ry = 2*y - 7
		if rx*rx + ry*ry > 49:
			screen.pixel(x, y, int(math.floor(math.sin(-math.atan2(x-3.5, y-3.5)/2)*32)) % 32)
		else:
			screen.pixel(x, y, int(math.floor(-math.atan2(y-3.5, x-3.5)/math.pi*32)) % 32)

while pew.keys():
	pew.tick(0.1)
while pew.keys() == 0:
	for i in range(32):
		pew.palette(offset = i)
		pew.show(screen)
		pew.tick(0.03)

pew.palette(None)
