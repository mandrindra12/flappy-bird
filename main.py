import py5
from random import randint as rand
from bird import *
from pipe import *
from game import *
vel_y = 5
pipe_vel = -5
bird = Bird(200, 200)
pipe = Pipe(700, 300, 100)
game = Game(bird, pipe)
gap = rand(80, 150)

def setup():
    global bg
    global pipe_img
    global bird_img
    global game_over_bg
    global pipe_rev_img
    global img
    py5.size(720, 480)
    #py5.full_screen()
    bg = py5.load_image("./images/flappy_bg.png")
    pipe_img = py5.load_image("./images/pipe_bottom.png")
    bird_img = py5.load_image("./images/yellow_bird.png")
    game_over_bg = py5.load_image("./images/game_over.jpg")
    pipe_rev_img = py5.load_image("./images/pipe_top.png")



def draw():
    global vel_y
    global bird
    global pipe
    global pipe_img
    global pipe_rev_img
    global bg
    global bird_img
    global pipe_vel
    global game
    global game_over_bg
    if py5.is_key_pressed and py5.key == ' ':
        vel_y = -vel_y
    pipe.lower_height = py5.height - pipe.y_lower
    game.run(bg, bird_img, pipe_img, pipe_rev_img, vel_y, pipe_vel)
    vel_y = 5
    if pipe.x < 0:
        pipe.x = py5.width
    if bird.y+35 >= py5.height or bird.y+35 <= 0 or (bird.x+35>=pipe.x and bird.x<=pipe.x+100) and (bird.y+35>=pipe.y_lower or bird.y < pipe.upper_height):
        bird = Bird(200, 200)
        py5.image(game_over_bg, 0, 0, py5.width, py5.height)
        pipe = Pipe(700, rand(100, 400), rand(70, 90))
        game = Game(bird, pipe)
        py5.no_loop()
        """game.over(game_over_bg)"""
    if pipe.x > py5.width:
        pipe.x = 0


def key_pressed():
    global pipe_vel
    if py5.key == '\n':
        py5.loop()
    if py5.key == py5.CODED:
        if py5.key_code == py5.CONTROL:
            pipe_vel = 5
        if py5.key_code == py5.SHIFT:
            pipe_vel = -5


py5.run_sketch()
