import py5

class Bird:
    def __init__(self, pos_x, pos_y, img):
        self.x = pos_x
        self.y = pos_y
        self.avatar = py5.load_image(img)

    def move(self, vel_x, vel_y):
        self.x = self.x + vel_x
        self.y = self.y + vel_y

    def display(self):
        py5.image(self.avatar, self.x, self.y, 50, 50)
