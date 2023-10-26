class Pipe:
    def __init__(self, x_pos):
        self.x = x_pos

    def move(self, vel_x):
        self.x = self.x + vel_x

