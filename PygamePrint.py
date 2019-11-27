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

import pygame

screen_x = 800
screen_y = 600
board_len = screen_y - 180
screen = pygame.display.set_mode((screen_x, screen_y))

board_s = pygame.image.load("images/board_s.png")
board_0 = pygame.image.load("images/board_0.png")
board_1 = pygame.image.load("images/board_1.png")
board_2 = pygame.image.load("images/board_2.png")
board_3 = pygame.image.load("images/board_3.png")
board_4 = pygame.image.load("images/board_4.png")
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

def blit_center(image, tuple):
    x, y = tuple
    xsize, ysize = image.get_rect().size
    screen.blit(image, (x-xsize/2, y-ysize/2))

def find_loc(x, y):
    if x == 0:
        return (board_len / 2, -board_len / 2 + board_len * y / 5)
    if x == 1:
        return (board_len / 2 - board_len * y / 5, board_len / 2)
    if x == 2:
        return (-board_len / 2, board_len / 2 - board_len * y / 5)
    if x == 3:
        return (-board_len / 2 + board_len * y / 5, -board_len / 2)
    if(x == 4):
        return (board_len / 2, -board_len / 2)
    if x == -1:
        return (board_len / 2 - board_len * y / 6, board_len / 2 - board_len * y / 6)
    if x == -2:
        return (-board_len / 2 + board_len * y / 6, board_len / 2 - board_len * y / 6)

def find_coord(tuple):
    x, y = tuple
    return (x + screen_x / 2, screen_y / 2 - y)

def print_board():
    for i in range(0, 4):
        for j in range(0, 5):
            image = board_s
            if j == 0:
                if i == 0:
                    image = board_2
                if i == 1:
                    image = board_1
                if i == 2:
                    image = board_0
                if i == 3:
                    image = board_4
            blit_center(image, find_coord(find_loc(i, j)))

    for i in range(-1, -3, -1):
        for j in range(1, 6):
            image = board_s
            if j == 3:
                image = board_3
            blit_center(image, find_coord(find_loc(i, j)))

"""
def turn(Player):
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
"""