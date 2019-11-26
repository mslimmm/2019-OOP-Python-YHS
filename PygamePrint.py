"""
(2,0)   (1,4)   (1,3)   (1,2)   (1,1)   (1,0)


(2,1)   (-2,1)                 (-1,1)   (0,4)


(2,2)       (-2,2)         (-1,2)       (0,3)
                   (-1,3)
                   (-2,3)
(2,3)       (-1,4)         (-2,4)       (0,2)


(2,4)   (-1,5)                 (-2,5)   (0,1)

(3,0)   (3,1)   (3,2)   (3,3)   (3,4)   (0,0) (4,0)
"""
import pygame, sys, random
from pygame.locals import *
import PlayerClass
import os

os.environ['SDL_VIDEO_CENTERED'] = '0'

pygame.init()
pygame.display.set_caption("YUT")
screen_x = 800
screen_y = 600
board_len = screen_y - 180
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()

sp_image = pygame.image.load("images/small_point.png")
bp_image = pygame.image.load("images/big_point.png")
egg_1_image = pygame.image.load("images/egg_1.png")
yut_0_image = pygame.image.load("images/yut_0.png")
yut_1_image = pygame.image.load("images/yut_1.png")
do_image = pygame.image.load("images/do.png")
gae_image = pygame.image.load("images/gae.png")
girl_image = pygame.image.load("images/girl.png")
yut_image = pygame.image.load("images/yut.png")
mo_image = pygame.image.load("images/mo.png")
wood_image = pygame.image.load("images/wood.png")

yut_loc = [(-200, 0), (-100, 0), (100, 0), (200, 0)]

def wherego():
    mvcnt = 0
    for i in range(4):
        x = random.randint(0,1)
        image = yut_0_image
        if(x == 1):
            image = yut_1_image
        blit_center(image, find_coord(yut_loc[i]))
        pygame.display.update()
        pygame.time.delay(300)
        mvcnt += x

    pygame.time.delay(500)
    if mvcnt == 1:
        blit_center(do_image, find_coord((0, 0)))
        pygame.display.update()
    elif mvcnt == 2:
        blit_center(gae_image, find_coord((0, 0)))
        pygame.display.update()
    elif mvcnt == 3:
        blit_center(girl_image, find_coord((0, 0)))
        pygame.display.update()
    elif mvcnt == 4:
        blit_center(yut_image, find_coord((0, 0)))
        pygame.display.update()
    else:
        blit_center(mo_image, find_coord((0, 0)))
        pygame.display.update()
        mvcnt = 5

    pygame.time.delay(300)
    return mvcnt

def find_loc(x, y):
    if x == 0:
        return (board_len / 2, -board_len / 2 + board_len * y / 5)
    if x == 1:
        return (board_len / 2 - board_len * y / 5, board_len / 2)
    if x == 2:
        return (-board_len / 2, board_len / 2 - board_len * y / 5)
    if x == 3:
        return (-board_len / 2 + board_len * y / 5, -board_len / 2)
    if x == -1:
        return (board_len / 2 - board_len * y / 6, board_len / 2 - board_len * y / 6)
    if x == -2:
        return (-board_len / 2 + board_len * y / 6, board_len / 2 - board_len * y / 6)

def blit_center(image, tuple):
    x, y = tuple
    xsize, ysize = image.get_rect().size
    screen.blit(image, (x-xsize/2, y-ysize/2))

def find_coord(tuple):
    x, y = tuple
    return (x + screen_x / 2, screen_y / 2 - y)

def print_board():
    for i in range(0, 4):
        for j in range(0, 5):
            image = sp_image
            if j == 0:
                image = bp_image
            blit_center(image, find_coord(find_loc(i, j)))

    for i in range(-1, -3, -1):
        for j in range(1, 6):
            image = sp_image
            if j == 3:
                image = bp_image
            blit_center(image, find_coord(find_loc(i, j)))

Player = PlayerClass.player()

while True:
    blit_center(wood_image, find_coord((0, 0)))
    print_board()
    blit_center(egg_1_image, find_coord(find_loc(Player.egglist[0].x, Player.egglist[0].y)))
    pygame.display.update()
    pygame.time.delay(500)
    mvcnt = wherego()
    pygame.time.delay(500)
    blit_center(wood_image, find_coord((0, 0)))
    print_board()
    blit_center(egg_1_image, find_coord(find_loc(Player.egglist[0].x, Player.egglist[0].y)))
    pygame.display.update()
    pygame.time.delay(500)
    Player.egglist[0].move(mvcnt)
    blit_center(egg_1_image, find_coord(find_loc(Player.egglist[0].x, Player.egglist[0].y)))
    pygame.display.update()
