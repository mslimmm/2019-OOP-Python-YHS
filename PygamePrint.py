import pygame
pygame.mixer.init()

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

yut = pygame.mixer.Sound("sounds/yut.wav")
catch = pygame.mixer.Sound("sounds/Scream10.ogg")
yay = pygame.mixer.Sound("sounds/yay.ogg")
los = pygame.mixer.Sound("sounds/los.ogg")
sel = pygame.mixer.Sound("sounds/sel.ogg")
car = pygame.mixer.Sound("sounds/car.ogg")

yut.set_volume(1.0)
catch.set_volume(1.0)
yay.set_volume(1.0)
los.set_volume(1.0)
sel.set_volume(1.0)
car.set_volume(1.0)

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
haitai_anykey_image = pygame.image.load("images/haitai_any_key.png")
haitai_what_image = pygame.image.load("images/haitai_what_image.png")
haitai_newegg_image = pygame.image.load("images/haitai_newegg.png")

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
dokabi_anykey_image = pygame.image.load("images/dokabi_any_key.png")
dokabi_what_image = pygame.image.load("images/dokabi_what_image.png")
dokabi_newegg_image = pygame.image.load("images/dokabi_newegg.png")

yut_0_image = pygame.image.load("images/yut_0.png")
yut_1_image = pygame.image.load("images/yut_1.png")
do_image = pygame.image.load("images/do.png")
gae_image = pygame.image.load("images/gae.png")
girl_image = pygame.image.load("images/girl.png")
yut_image = pygame.image.load("images/yut.png")
mo_image = pygame.image.load("images/mo.png")
back_image = pygame.image.load("images/back.png")

cvc_image = pygame.image.load("images/CVC.png")
pvc_image = pygame.image.load("images/PVC.png")
pvp_image = pygame.image.load("images/PVP.png")

arrow_r_image = pygame.image.load("images/arrow_r.png")
arrow_g_image = pygame.image.load("images/arrow_g.png")

s_0 = pygame.image.load("images/S_0.png")
s_1 = pygame.image.load("images/S_1.png")
s_2 = pygame.image.load("images/S_2.png")
s_3 = pygame.image.load("images/S_3.png")
s_4 = pygame.image.load("images/S_4.png")


yut_loc = [(-200, 0), (-100, 0), (100, 0), (200, 0)]

g_loc_dict = {'score': (330, 170), 'face': (330, 250)}
r_loc_dict = {'score': (-330, 170), 'face': (-330, 250)}

score_list = [s_0, s_1, s_2, s_3, s_4]

mvcnt_coord = (0, 130)

haitai_list = [0, haitai_1_image, haitai_2_image, haitai_3_image, haitai_4_image]
dokabi_list = [0, dokabi_1_image, dokabi_2_image, dokabi_3_image, dokabi_4_image]

haitai_dict = {'first': haitai_first_image, 'turn': haitai_turn_image, 'catch': haitai_catch_image,
               'win': haitai_win_image, 'yut': haitai_yut_again, 'mo': haitai_mo_again, 'carry': haitai_carry_image,
               'arrow': arrow_g_image, 'anykey': haitai_anykey_image, 'what': haitai_what_image,
               'new': haitai_newegg_image}
dokabi_dict = {'first': dokabi_first_image, 'turn': dokabi_turn_image, 'catch': dokabi_catch_image,
               'win': dokabi_win_image, 'yut': dokabi_yut_again, 'mo': dokabi_mo_again, 'carry': dokabi_carry_image,
               'arrow': arrow_r_image, 'anykey': dokabi_anykey_image, 'what': dokabi_what_image,
               'new': dokabi_newegg_image}

situ_dict = {'first': (0, 260), 'turn': (0, 0), 'catch': (0, 260), 'win': (0, 0), 'yut': (0, 260), 'mo': (0, 260),
             'carry': (0, 260)}

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

def print_score(user1, user2):
    blit_center(user1.image, find_coord(user1.locdict['face']))
    blit_center(user2.image, find_coord(user2.locdict['face']))
    blit_center(score_list[user1.fineggno], find_coord(user1.locdict['score']))
    blit_center(score_list[user2.fineggno], find_coord(user2.locdict['score']))

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
    print_score(user1, user2)
    pygame.display.update()


def eggarrow(user):
    choose_list = []
    for i in range(len(user.onmap)):
        egg = user.onmap[i]
        arrow_x, arrow_y = find_loc(egg.x, egg.y)
        choose_list.append(i)
        blit_center(user.imagedict['arrow'], find_coord((arrow_x, arrow_y + 30)))
    if 4 - user.onmapno - user.fineggno > 0:
        arrow_x = 336
        arrow_y = -150
        choose_list.append(-1)
        blit_center(user.imagedict['arrow'], find_coord((arrow_x, arrow_y - 20)))
        blit_center(user.imagedict['new'], find_coord((arrow_x, arrow_y)))
        blit_center(user.imagelist[4-user.onmapno-user.fineggno], find_coord((arrow_x, arrow_y - 80)))
    return choose_list

def print_mvcnt(mvcnt):
    if mvcnt == 1:
        blit_center(do_image, find_coord(mvcnt_coord))
        pygame.display.update()
    elif mvcnt == 2:
        blit_center(gae_image, find_coord(mvcnt_coord))
        pygame.display.update()
    elif mvcnt == 3:
        blit_center(girl_image, find_coord(mvcnt_coord))
        pygame.display.update()
    elif mvcnt == 4:
        blit_center(yut_image, find_coord(mvcnt_coord))
        pygame.display.update()
    else:
        blit_center(mo_image, find_coord(mvcnt_coord))
        pygame.display.update()
        mvcnt = 5

    return mvcnt

def situation(user1, user2, situ):
    if situ == 'catch' or situ == 'carry' or situ == 'yut' or situ == 'mo':
        print_all(user1, user2)
        pygame.display.update()
        if situ == 'carry':
            car.play()
        pygame.time.delay(500)
    blit_center(user1.imagedict[situ], find_coord(situ_dict[situ]))
    pygame.display.update()
    if situ == 'win':
        user1.winsound.play()
    pygame.time.delay(1000)
    print_all(user1, user2)
    pygame.display.update()