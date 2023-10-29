class Pipe:
    def __init__(self, x_pos, y_pos, g):
        self.x = x_pos
        self.y_upper = 0
        self.gap = g
        self.y_lower = y_pos
        self.lower_height = 0
        self.upper_height = y_pos-g

    def move(self, vel_x):
        self.x = self.x + vel_x

