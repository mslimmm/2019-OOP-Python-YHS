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
    return (x + screen_x / 2, y + screen_y / 2)

screen.fill((255, 255, 255))

for i in range(0, 4):
    for j in range(0, 5):
        image = sp_image
        if j == 0:
            image = bp_image
        blit_center(image, find_coord(find_loc(i, j)))

for i in range (-1, -3, -1):
    for j in range(1, 6):
        image = sp_image
        if j == 3:
            image = bp_image
        blit_center(image, find_coord(find_loc(i, j)))

while True:
    pygame.display.update()