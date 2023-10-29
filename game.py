from bird import *
from pipe import *
from random import randint as rand
import py5

class Game:
    def __init__(self, bird, pipe):
        self.bird = bird
        self.pipe = pipe
    def run(self, bg, bird_img, pipe_img, pipe_rev_img, vel_y,pipe_vel):
        py5.image(bg, 0, 0, py5.width, py5.height)
        py5.image(bird_img, self.bird.x, self.bird.y, 40, 40)
        py5.image(pipe_rev_img, self.pipe.x, 0, 100, self.pipe.upper_height)
        py5.image(pipe_img, self.pipe.x, self.pipe.y_lower, 100, self.pipe.lower_height)
        self.pipe.move(pipe_vel)
        self.bird.move(0, vel_y)

