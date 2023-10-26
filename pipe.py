import py5

class Pipe:
    def __init__(self, x_pos, img, h):
        self.x = x_pos
        self.icon = py5.load_image(img)
        self.h = h

    def move(self, vel_x):
        self.x = self.x + vel_x

    def display(self):
        py5.image(self.icon, self.x, py5.height-self.h, 100, self.h)
