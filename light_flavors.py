import lights


def odd(color):
    pixel = lights.SingleLight()
    pixel.start('/dev/ttyACM0')
    if color == 'clear':
        i = 0
        while i < 30:
            if i % 2:
                pixel.set(255, 255, 255, i)
                pixel.bang()
                i += 1
            else:
                i += 1
    else:
        i = 0
        while i < 30:
            if i % 2:
                pixel.set(color[0], color[1], color[2],  i)
                pixel.bang()
                i += 1
            else:
                i += 1













