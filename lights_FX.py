import lights
from time import sleep


class BlinkStripLight(lights.StripLight):
    def __init__(self):
        lights.StripLight.__init__(self)
        self.color = [255, 0, 255]
        self.color2 = [104, 104, 255]
        self.delay = 1.0
        self.iter = 1

    def blinkColor(self):
        self.set(self.color[0], self.color[1], self.color[2])
        i = 0.0
        while i < self.iter:
            self.bang()
            sleep(self.delay/2.0)
            self.clear()
            sleep(self.delay/2.0)
            i += 1
        self.clear()

    def swapColor(self):
        i = 0.0
        while i < self.iter:
            self.set(self.color[0], self.color[1], self.color[2])
            self.bang()
            sleep(self.delay/2.0)
            self.set(self.color2[0], self.color2[1], self.color2[2])
            self.bang()
            sleep(self.delay/2.0)
            i += 1
