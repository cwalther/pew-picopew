from micropython import const
import machine
import time


_FONT = (
    b'JJJJJJFFBJFJyhJJJJh5h5hJBtAreBynFLyJDy\xd6y\xd4JFBJJJJGHIHGJVjzjVJJlWlJJ'
    b'JFuFJJJJJJFLJJuJJJJJJJFJznFLIJgy}yTJFDFFFJQzWHuJdzVzdJFLiuzJuIezeJgIeydJ'
    b'unFLIJdyWydJdytzTJJFJFJJJFJFLJzFIFzJJuJuJJIFzFIJTzVJFJgxyHsJWhyqyJUyUyUJ'
    b'wHIHwJQiyiQJuIEIuJuIEIIJwHIxwJyyuyyJWFFFWJzzzydJymAmyJIIIIuJhqu}yJxmd|iJ'
    b'WhyhWJQyyQIJWhy|gzQyyQyJtIdzeJuFFFFJyyyxcJyyhSFJy}qulJylSlyJyhSFFJunFLuJ'
    b'EIIIEJILFnzJvzzzvJF}hJJJJJJJJuIBJJJJJwxysJIQiyQJJwHIsJzsxysJJgxAwJ~FdFFF'
    b'JsxsjTIQiyyJFNGFRJzZ~z{TIyAmyJGFFFnJJUuqyJJQiyyJJWxiWJJQiyQIJsxyszJ|AIIJ'
    b'JwLnUJFdFFnJJyyxgJJyhSFJJy}dlJJySSyJJyygjTJunLuJrFMFrJFFFFFFAF~FAJJ\xc78'
    b'JJJ\xd3,\xd3,\xd3,'
)
_SALT = const(181)


K_X = const(0x01)
K_DOWN = const(0x02)
K_LEFT = const(0x04)
K_RIGHT = const(0x08)
K_UP = const(0x10)
K_O = const(0x20)

_i2c = None
_buffer = None


def brightness(level):
    level &= 0xf
    _i2c.writeto_mem(80, 0xfe, b'\xc5')
    _i2c.writeto_mem(80, 0xfd, b'\x03')
    _i2c.writeto_mem(80, 0x01, b'\x01\x04\t\x10\x19$1@Qdy\x90\xa9\xc4\xe1\xff'[level:level+1])
    _i2c.writeto_mem(80, 0xfe, b'\xc5')
    _i2c.writeto_mem(80, 0xfd, b'\x01')


def palette(pal=False, offset=0):
    global _palette, _palettesize, _paletteoffset
    if pal is not False:
        if not pal:
            pal = bytearray(768)
            for i in range(256):
                if (i & 0xc0) == 0:
                    b = (255, 216, 180, 149, 121, 96, 75, 57, 42, 30, 20, 12, 7, 4, 2, 1)[(i >> 2) & 15]
                    pal[3*i] = (b*(0, 0, 255, 160)[i & 3] + 127)//255
                    pal[3*i+1] = b*(i & 1)
                elif (i & 0xc0) == 0x40:
                    b = (0, 15, 89, 255)[i & 3]
                    pal[3*i] =   (b*(0, 4, 16, 36, 64, 100, 143, 195, 255, 255, 255, 255, 255, 255, 255, 255)[(i >> 2) & 15] + 127)//255
                    pal[3*i+1] = (b*(255, 255, 255, 255, 255, 255, 255, 255, 255, 121, 42, 7, 0, 0, 0, 0)[(i >> 2) & 15] + 127)//255
                else:
                    pal[3*i] = (0, 1, 2, 4, 8, 15, 24, 35, 50, 68, 89, 114, 143, 176, 213, 255)[(i >> 3) & 15]
                    pal[3*i+1] = (0, 2, 10, 28, 60, 106, 171, 255)[i & 7]
        _palette = pal
    _palettesize = len(_palette)//3
    _paletteoffset = offset % _palettesize


def show(pix):
    global _buffer, _i2c

    buffer = pix.buffer
    width = pix.width
    index = 0
    for y in range(8):
        position = y*width
        for x in range(8):
            pixel = 3*((buffer[position] + _paletteoffset) % _palettesize)
            position += 1
            _buffer[index] = _palette[pixel + 1]
            index += 1
            _buffer[index] = _palette[pixel]
            index += 1
    _i2c.writeto_mem(80, 0x00, _buffer)


def _scankeys():
    k = 0
    for i in range(6):
        k |= ((_keypins[i].value() ^ 1) << i)
    return k


def keys():
    global _keys, _gameover
    nk = _scankeys()
    k = _keys | nk
    _keys = nk
    if k & 0b011110 == 0b011110 and not _gameover:
        _gameover = True
        raise GameOver()
    elif k == 0:
        _gameover = False
    return k


def tick(delay):
    global _tick
    delay = int(delay*1000)
    now = time.ticks_ms()
    _tick = time.ticks_add(_tick, delay)
    diff = time.ticks_diff(_tick, now)
    if diff < 0:
        _tick = now
        diff = 0
    time.sleep_ms(diff)


class GameOver(Exception):
    __slots__ = ()


class Pix:
    __slots__ = ('buffer', 'width', 'height')

    def __init__(self, width=8, height=8, buffer=None):
        if buffer is None:
            buffer = bytearray(width * height)
        self.buffer = buffer
        self.width = width
        self.height = height

    @classmethod
    def from_text(cls, string, color=None, bgcolor=0, colors=None):
        pix = cls(4 * len(string), 6)
        font = memoryview(_FONT)
        if colors is None:
            if color is None:
                colors = [3, 2, 1, 0]
                if _paletteoffset == 0:
                    colors = [c + 80 for c in colors]
                if bgcolor != 0:
                    colors[2] = colors[3] = bgcolor
            else:
                colors = (color, color, bgcolor, bgcolor)
        x = 0
        for c in string:
            index = ord(c) - 0x20
            if not 0 <= index <= 95:
                continue
            row = 0
            for byte in font[index * 6:index * 6 + 6]:
                unsalted = byte ^ _SALT
                for col in range(4):
                    pix.pixel(x + col, row, colors[unsalted & 0x03])
                    unsalted >>= 2
                row += 1
            x += 4
        return pix

    @classmethod
    def from_iter(cls, lines):
        pix = cls(len(lines[0]), len(lines))
        y = 0
        for line in lines:
            x = 0
            for pixel in line:
                pix.pixel(x, y, pixel)
                x += 1
            y += 1
        return pix

    def pixel(self, x, y, color=None):
        if not 0 <= x < self.width or not 0 <= y < self.height:
            return 0
        if color is None:
            return self.buffer[x + y * self.width]
        self.buffer[x + y * self.width] = color

    def box(self, color, x=0, y=0, width=None, height=None):
        x = min(max(x, 0), self.width - 1)
        y = min(max(y, 0), self.height - 1)
        width = max(0, min(width or self.width, self.width - x))
        height = max(0, min(height or self.height, self.height - y))
        for y in range(y, y + height):
            xx = y * self.width + x
            for i in range(width):
                self.buffer[xx] = color
                xx += 1

    def blit(self, source, dx=0, dy=0, x=0, y=0,
             width=None, height=None, key=None):
        if dx < 0:
            x -= dx
            dx = 0
        if x < 0:
            dx -= x
            x = 0
        if dy < 0:
            y -= dy
            dy = 0
        if y < 0:
            dy -= y
            y = 0
        width = min(min(width or source.width, source.width - x),
                    self.width - dx)
        height = min(min(height or source.height, source.height - y),
                     self.height - dy)
        source_buffer = memoryview(source.buffer)
        self_buffer = self.buffer
        if key is None:
            for row in range(height):
                xx = y * source.width + x
                dxx = dy * self.width + dx
                self_buffer[dxx:dxx + width] = source_buffer[xx:xx + width]
                y += 1
                dy += 1
        else:
            for row in range(height):
                xx = y * source.width + x
                dxx = dy * self.width + dx
                for col in range(width):
                    color = source_buffer[xx]
                    if color != key:
                        self_buffer[dxx] = color
                    dxx += 1
                    xx += 1
                y += 1
                dy += 1

    def __str__(self):
        return "\n".join(
            "".join(
                ('.', '+', '*', '@')[self.pixel(x, y)]
                for x in range(self.width)
            )
            for y in range(self.height)
        )


def init():
    global _i2c, _buffer, _keys, _tick, _keypins

    # turn off dotstar to save power
    machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_HOLD)
    machine.Pin(12, machine.Pin.IN)
    machine.Pin(2, machine.Pin.IN)

    _tick = time.ticks_ms()
    _buffer = bytearray(128)

    if _i2c is not None:
        return

    _i2c = machine.I2C(0, sda=machine.Pin(21), scl=machine.Pin(22))

    _keypins = (
        machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP), # X
        machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP), # down
        machine.Pin(23, machine.Pin.IN, machine.Pin.PULL_UP), # left
        machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP), # right
        machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP), # up
        machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP) # O
    )
    _keys = 0
    def handler(p):
        global _keys
        _keys |= _scankeys()
    for p in _keypins:
        p.irq(handler=handler, trigger=machine.Pin.IRQ_FALLING)

    try:
        _i2c.readfrom_mem(80, 0x11, 1) # reset
    except OSError:
        raise RuntimeError("PewPew board not found")
    _i2c.writeto_mem(80, 0xfe, b'\xc5') # unlock pages
    _i2c.writeto_mem(80, 0xfd, b'\x03') # go to function page
    _i2c.writeto_mem(80, 0x00, b'\x01') # power on
    _i2c.writeto_mem(80, 0xfe, b'\xc5') # unlock pages
    _i2c.writeto_mem(80, 0xfd, b'\x00') # go to LED control page
    _i2c.writeto_mem(80, 0x00, b'\xff'*16) # all 128 LEDs on

    palette(None)
    brightness(7)
