import lights
import psutil
from light_flavors import odd
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

print 'Reading CPU[0] Usage\n\n'
while 1:
    check = psutil.cpu_percent(interval=.333)
    print 'CPU[0]: {}%...'.format(check)
    if check < 5:
        green()
    elif check >=5 and check < 10:
        blue()
    elif check >= 10 and check < 17:
        purple()
    elif check >= 17 and check < 22:
        yellow()
    elif check >= 22 and check < 25:
        orange()
    else: 
        red()





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


