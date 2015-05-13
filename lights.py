from serial import Serial


class StripLight():

    def __init__(self):

        self.payLoad = b''
        self.event = None

    def start(self, path=0):
        if not path:
            path = raw_input('Serial Port Path: ')
            serial = Serial(path, '9600')
            self.event = serial
        elif path:
            serial = Serial(path, '9600')
            self.event = serial

    def set(self, R, G, B):

        self.payLoad = b'{}, {}, {}, 0, 0\n'.format(R, G, B)

    def bang(self):
        self.event.write(self.payLoad)

    def clear(self):
        self.event.write(b'10, 10, 10, 0, 0\n')

    def echo(self):
        pass


class SingleLight:

    def __init__(self):

        self.payLoad = b''
        self.event = None
        self.pixel = 0

    def start(self, path=0):
        if not path:
            path = raw_input('Serial Port Path: ')
            serial = Serial(path, '9600')
            self.event = serial
        elif path:
            serial = Serial(path, '9600')
            self.event = serial

    def set(self, R, G, B, pixel):
        self.pixel = pixel
        self.payLoad = b'{}, {}, {}, 1, {}\n'.format(R, G, B, self.pixel)

    def bang(self):
        self.event.write(self.payLoad)

    def clear(self):
        self.event.write(b'0, 0, 0, 1, {}\n'.format(self.pixel))

    def echo(self):
        pass