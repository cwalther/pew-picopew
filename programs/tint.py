import pew

pew.init()
choice = {64: 1, 80: 2, 96: 3, 112: 4}.get(pew._paletteoffset, 0)
pew.palette(None)
screen = pew.Pix()

keyhistory = 0
def keyevents():
	global keyhistory
	keys = pew.keys()
	events = keys & (~keyhistory | (keyhistory & (keyhistory >> 8) & (keyhistory >> 16) & (keyhistory >> 24)))
	keyhistory = ((keyhistory & 0x3FFFFF) << 8) | keys
	return events

def paint():
	if choice == 0:
		for i in range(3):
			screen.box(i+1, 2*i+1, 1, 2, 2)
	else:
		for i in range(3):
			screen.box(32+i+1, 2*i+1, 1, 2, 1)
	for c in range(1, 5):
		if choice == c:
			for i in range(3):
				screen.box(48+c*16+i+1, 2*i+1, 1+c, 2, 2)
		else:
			screen.box(48+c*16+1, 1, 1 + c + (0 if choice > c else 1), 6, 1)
	pew.show(screen)

paint()
while pew.keys():
	pew.tick(0.1)
while True:
	k = keyevents()
	if k & pew.K_UP:
		choice = (choice - 1) % 5
	if k & pew.K_DOWN:
		choice = (choice + 1) % 5
	if k & pew.K_O:
		pew.palette(offset = (0, 64, 80, 96, 112)[choice])
		break
	paint()
	pew.tick(0.06)
