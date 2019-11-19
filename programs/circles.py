# a demo for alpha blending in the true-color part of the default palette

import pew
import random

pew.init()
pew.palette(None)

def main():
	screen = pew.Pix()
	r1 = -1
	r2 = -1
	stop = False
	stopped = 0
	blend = bytearray(16)
	t1r = t1g = t2r = t2g = 0
	while stopped != 3:
		stop = stop or pew.keys()
		if r1 < 10:
			if stop:
				stopped |= 1
				cx1 = 500
				r1 = 10
				dr1 = 20
			else:
				cx1 = random.getrandbits(7)
				cy1 = random.getrandbits(7)
				dx1 = random.getrandbits(4)-8
				dy1 = random.getrandbits(4)-11
				r1 = 10
				dr1 = random.getrandbits(4)+5
				t1r = random.getrandbits(8) % 23
				t1g = 7
				if t1r >= 16:
					t1g = 22 - t1r
					t1r = 15
				for a1 in range(4):
					for a2 in range(4):
						blend[(a1 << 2) | a2] = 0x80 | (((3*a1*t1r + (3-a1)*a2*t2r + 4)//9) << 3) | ((3*a1*t1g + (3-a1)*a2*t2g + 4)//9)
		if r2 < 10:
			if stop:
				stopped |= 2
				cx2 = 500
				r2 = 10
				dr2 = 20
			else:
				cx2 = random.getrandbits(7)
				cy2 = random.getrandbits(7)
				dx2 = random.getrandbits(4)-8
				dy2 = random.getrandbits(4)-11
				r2 = 10
				dr2 = random.getrandbits(4)+5
				t2r = random.getrandbits(8) % 23
				t2g = 7
				if t2r >= 16:
					t2g = 22 - t2r
					t2r = 15
				for a1 in range(4):
					for a2 in range(4):
						blend[(a1 << 2) | a2] = 0x80 | (((3*a1*t1r + (3-a1)*a2*t2r + 4)//9) << 3) | ((3*a1*t1g + (3-a1)*a2*t2g + 4)//9)
		r = r1 >> 1
		l1 = r-5
		l1 *= l1
		m1 = r*r
		u1 = r+5
		u1 *= u1
		r = r2 >> 1
		l2 = r-5
		l2 *= l2
		m2 = r*r
		u2 = r+5
		u2 *= u2
		for y in range(8):
			for x in range(8):
				rx = (x<<4)-cx1
				ry = (y<<4)-cy1
				rr1 = rx*rx + ry*ry
				rx = (x<<4)-cx2
				ry = (y<<4)-cy2
				rr2 = rx*rx + ry*ry
				screen.pixel(x, y, blend[((3 if rr1 < l1 else 2 if rr1 < m1  else 1 if rr1 < u1 else 0) << 2) | (3 if rr2 < l2 else 2 if rr2 < m2  else 1 if rr2 < u2 else 0)])
		r1 += dr1
		dr1 -= 1
		cx1 += dx1
		cy1 += dy1
		r2 += dr2
		dr2 -= 1
		cx2 += dx2
		cy2 += dy2
		pew.show(screen)
		pew.tick(0.05)

while pew.keys():
	pew.tick(0.1)
main()
