import py5
from random import randint as rand
from bird import *
from obstacle import *

pipes = []
vel_y = 10
pipe_vel = -10
def setup():
    global bg
    global bird
    global obs
    py5.size(720, 480)
    #py5.full_screen()
    bg = py5.load_image("flappy_bg.png")
    bird = Bird(200, 300, "yellow_bird.png")
def show(pipes, pipe_vel):
    for i in pipes:
        i.display()
        i.move(pipe_vel)

def draw():
    global vel_y
    global ostacle
    global bg
    global bird
    if py5.is_key_pressed:
        if py5.key == ' ':
            vel_y = -vel_y

    #loading background
    py5.image(bg, 0, 0, py5.width, py5.height)
    h=rand(100, 400)
    bird.display()
    bird.move(0, vel_y)
    pipe = Pipe(py5.width, "pipe.png", h)
    pipes.append(pipe)
    vel_y = 10
    if pipe.x < 0:
        pipe.x = py5.width
    if bird.y+25 >= py5.height or bird.y-25 <= 0:
        py5.background(255, 0, 0)

py5.run_sketch()
