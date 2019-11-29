import PygamePrint as pp
import pygame
from pygame.locals import *
import random

LEFT = 1

def actuser(moving_egg, user1, user2, movecnt):

    run = False

    if movecnt == 4 or movecnt == 5:
        run = True

    moving_egg.move(movecnt)

    if moving_egg not in user1.onmap:
        user1.onmap.append(moving_egg)
        user1.onmapno += 1

    if moving_egg.x == 4 and moving_egg.y > 0:
        user1.onmap.remove(moving_egg)
        user1.finegg.append(moving_egg)
        for i in moving_egg.carrying_egg:
            user1.onmap.remove(i)
            user1.finegg.append(i)
        user1.onmapno -= moving_egg.carrying
        user1.fineggno += moving_egg.carrying

    chk = 0
    for i in user2.onmap:
        if i.x == moving_egg.x and i.y == moving_egg.y:
            i.catched()
            for j in i.carrying_egg:
                user2.onmap.remove(j)
                user2.onmapno -= 1
            user2.onmap.remove(i)
            user2.onmapno -= 1
            i.carrying_egg.clear()
            run = True
            pp.situation(user1, user2, 'catch')
            chk = 1

    ifcarry = 0
    for i in user1.onmap:
        for j in user1.onmap:
            if i.x == j.x and i.y == j.y and i is not j and i not in j.carrying_egg and j not in i.carrying_egg:
                user1.make_carry(i, j)
                ifcarry = 1
                chk = 1

    if ifcarry == 1:
        pp.situation(user1, user2, 'carry')

    if chk == 0:
        if movecnt == 4:
            chk = 1
            pp.situation(user1, user2, 'yut')
        elif movecnt == 5:
            chk = 1
            pp.situation(user1, user2, 'mo')

    if chk == 0:
        pp.print_all(user1, user2)
        pygame.time.delay(1000)

    if user1.fineggno == 4:
        run = False

    return run

def actcom(user1, user2):

    run = True

    while run:
        pp.print_all(user1, user2)
        pygame.time.delay(500)
        randomlist = []

        for i in range(4):
            if user1.egglist[i] in user1.onmap:
                randomlist.append(i)

        for i in range(4):
            if user1.egglist[i] not in user1.onmap and user1.egglist[i] not in user1.finegg:
                randomlist.append(i)
                break

        random.shuffle(randomlist)
        moving_egg = user1.egglist[randomlist[0]]

        movecnt = user1.wherego()
        run = actuser(moving_egg, user1, user2, movecnt)


def actplay(user1, user2):

    run = True

    while run:
        randomlist = []
        for i in range(4):
            if user1.egglist[i] not in user1.onmap and user1.egglist[i] not in user1.finegg:
                randomlist.append(user1.egglist[i])
                break
        random.shuffle(randomlist)

        pp.print_all(user1, user2)
        pygame.display.update()
        pygame.time.delay(500)
        choose = 0
        moving_egg = 0
        movecnt = user1.wherego()
        pygame.time.delay(500)
        pp.print_all(user1, user2)
        pp.print_mvcnt(movecnt)
        pp.blit_center(user1.imagedict['what'], pp.find_coord((0, 260)))
        choose_list = pp.eggarrow(user1)
        pygame.display.update()
        while not choose:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP and event.button == LEFT:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    mouse_x = mouse_x - pp.screen_x / 2
                    mouse_y = pp.screen_y / 2 - mouse_y
                    for eggnum in choose_list:
                        if eggnum == -1:
                                xsize, ysize = user1.imagedict['new'].get_rect().size
                                if (300 - xsize / 2 <= mouse_x <= 300 + xsize / 2) and (0 - ysize / 2 <= mouse_y <= 0 + ysize / 2):
                                    choose = 1
                                    moving_egg = randomlist[0]

                        else:
                            egg = user1.onmap[eggnum]
                            xsize, ysize = egg.image.get_rect().size
                            egg_x, egg_y = pp.find_loc(egg.x, egg.y)
                            if (egg_x - xsize / 2 <= mouse_x <= egg_x + xsize / 2) and (egg_y - ysize / 2 <= mouse_y <= egg_y + ysize / 2):
                                choose = 1
                                moving_egg = user1.onmap[eggnum]

        run = actuser(moving_egg, user1, user2, movecnt)

