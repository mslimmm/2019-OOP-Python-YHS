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

haitai_1_image = pygame.image.load("images/haitai_1.png")
haitai_2_image = pygame.image.load("images/haitai_2.png")
haitai_3_image = pygame.image.load("images/haitai_3.png")
haitai_4_image = pygame.image.load("images/haitai_4.png")
haitai_first_image = pygame.image.load("images/haitai_first_image.png")
haitai_turn_image = pygame.image.load("images/haitai_turn_image.png")
haitai_yut_again = pygame.image.load("images/haitai_yut_again.png")
haitai_mo_again = pygame.image.load("images/haitai_mo_again.png")
haitai_catch_image = pygame.image.load("images/haitai_catch_image.png")
haitai_carry_image = pygame.image.load("images/haitai_carry_image.png")
haitai_win_image = pygame.image.load("images/haitai_win_image.png")

dokabi_1_image = pygame.image.load("images/dokabi_1.png")
dokabi_2_image = pygame.image.load("images/dokabi_2.png")
dokabi_3_image = pygame.image.load("images/dokabi_3.png")
dokabi_4_image = pygame.image.load("images/dokabi_4.png")
dokabi_first_image = pygame.image.load("images/dokabi_first_image.png")
dokabi_turn_image = pygame.image.load("images/dokabi_turn_image.png")
dokabi_yut_again = pygame.image.load("images/dokabi_yut_again.png")
dokabi_mo_again = pygame.image.load("images/dokabi_mo_again.png")
dokabi_catch_image = pygame.image.load("images/dokabi_catch_image.png")
dokabi_carry_image = pygame.image.load("images/dokabi_carry_image.png")
dokabi_win_image = pygame.image.load("images/dokabi_win_image.png")

yut_0_image = pygame.image.load("images/yut_0.png")
yut_1_image = pygame.image.load("images/yut_1.png")
do_image = pygame.image.load("images/do.png")
gae_image = pygame.image.load("images/gae.png")
girl_image = pygame.image.load("images/girl.png")
yut_image = pygame.image.load("images/yut.png")
mo_image = pygame.image.load("images/mo.png")
back_image = pygame.image.load("images/back.png")

anykey_image = pygame.image.load("images/any_key.png")

yut_loc = [(-200, 0), (-100, 0), (100, 0), (200, 0)]
haitai_list = [0, haitai_1_image, haitai_2_image, haitai_3_image, haitai_4_image]
dokabi_list = [0, dokabi_1_image, dokabi_2_image, dokabi_3_image, dokabi_4_image]
haitai_dict = {'first': haitai_first_image, 'turn': haitai_turn_image, 'catch': haitai_catch_image, 'win': haitai_win_image, 'yut': haitai_yut_again, 'mo': haitai_mo_again, 'carry': haitai_carry_image}
dokabi_dict = {'first': dokabi_first_image, 'turn': dokabi_turn_image, 'catch': dokabi_catch_image, 'win': dokabi_win_image, 'yut': dokabi_yut_again, 'mo': dokabi_mo_again, 'carry': dokabi_carry_image}

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

def print_all(user1, user2):
    user1.carry_image()
    user2.carry_image()
    blit_center(back_image, find_coord((0, 0)))
    print_board()
    for i in range(4):
        if user1.egglist[i] in user1.onmap:
            blit_center(user1.egglist[i].image, find_coord(find_loc(user1.egglist[i].x, user1.egglist[i].y)))
        if user2.egglist[i] in user2.onmap:
            blit_center(user2.egglist[i].image, find_coord(find_loc(user2.egglist[i].x, user2.egglist[i].y)))
    pygame.display.update()