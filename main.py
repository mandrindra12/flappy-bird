import py5
from random import randint as rand
from bird import *
from pipe import *
vel_y = 7
pipe_vel = -7
bird = Bird(200, 300)
pipe = Pipe(py5.width)
pipe_reversed = Pipe(py5.width)


def setup():
    global bg
    global pipe_img
    global bird_img
    global game_over_bg
    global pipe_rev_img
    py5.size(720, 480)
    #py5.full_screen()
    bg = py5.load_image("./images/flappy_bg.png")
    pipe_img = py5.load_image("./images/pipe.png")
    bird_img = py5.load_image("./images/yellow_bird.png")
    game_over_bg = py5.load_image("./images/game_over.jpg")
    pipe_rev_img = py5.load_image("./images/pipe~2.png")

def draw():
    global vel_y
    global ostacle
    global bg
    global bird_img
    global pipe_img
    global game_over_bg
    h = rand(100, 300)
    pipe_height = py5.height - h
    if py5.is_key_pressed:
        if py5.key == ' ':
            vel_y = -vel_y

    py5.image(bg, 0, 0, py5.width, py5.height)
    py5.image(bird_img, bird.x, bird.y, 50, 50)
    py5.image(pipe_rev_img, pipe.x, 0, 100, 50)
    py5.image(pipe_img, pipe.x, py5.height-50, 100, 50)
    pipe.move(pipe_vel)
    bird.move(0, vel_y)
    vel_y = 7
    if pipe.x < 0:
        pipe.x = py5.width
    if bird.y+25 >= py5.height or bird.y-25 <= 0:
        py5.image(game_over_bg, 0, 0, py5.width, py5.height)
        py5.no_loop()



py5.run_sketch()
