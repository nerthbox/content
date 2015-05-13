
import lights
import psutil

from time import sleep

_red = [255, 0, 0]
_green = [0, 255, 0]
_blue = [0, 0, 255]
_yellow = [255, 255, 0]
_purple = [255, 0, 255]
_white = [255, 255, 255]
_orange = [255, 51, 0]


strip = lights.StripLight()
strip.start('/dev/ttyACM0')
sleep(1)
strip.set(200, 200, 200)
strip.bang()

def red():
    strip.set(_red[0], _red[1], _red[2])
    strip.bang()


def green():
    strip.set(_green[0], _green[1], _green[2])
    strip.bang()


def blue():
    strip.set(_blue[0], _blue[1], _blue[2])
    strip.bang()


def yellow():
    strip.set(_yellow[0], _yellow[1], _yellow[2])
    strip.bang()


def purple():
    strip.set(_purple[0], _purple[1], _purple[2])
    strip.bang()


def white():
    strip.set(_white[0], _white[1], _white[2])
    strip.bang()


def orange():
    strip.set(_orange[0], _orange[1], _orange[2])
    strip.bang()


def off():
    strip.set(0, 0, 0)
    strip.bang()

while 1:
    usage = psutil.virtual_memory()
    print usage.percent
    sleep(.333)
    if usage.percent <= 8.5:
        green()
    elif usage.percent > 8.5 and usage.percent <= 8.6:
        purple()
    elif usage.percent == 8.7:
        blue()
    elif usage.percent == 8.8:
        yellow()
    elif usage.percent >= 8.9 and usage.percent <= 10:
        orange()
    elif usage.percent >= 10:
        red()
    else:
        white()








"""
while 1:
    check = raw_input('Color: ')
    if check == 'red':
        red()
    elif check == 'green':
        green()
    elif check == 'blue':
        blue()
    elif check == 'yellow':
        yellow()
    elif check == 'purple':
        purple()
    elif check == 'white':
        white()
    elif check == 'orange':
        orange()
    else:
        off()

"""


