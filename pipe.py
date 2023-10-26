class Pipe:
    def __init__(self, x_pos, h):
        self.x = x_pos
        self.h = h

    def move(self, vel_x):
        self.x = self.x + vel_x

