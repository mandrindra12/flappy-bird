
class Bird:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

    def move(self, vel_x, vel_y):
        self.x = self.x + vel_x
        self.y = self.y + vel_y

