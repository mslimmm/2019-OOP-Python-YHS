import pygame
import PygamePrint as pp
import random

mvcnt_coord = (0, 130)

def playut():
    sum = 0
    mvcnt = 0
    running = True
    pp.blit_center(pp.anykey_image, pp.find_coord((0, 260)))
    pygame.display.update()
    pygame.event.clear()
    while running:
        check = 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("누름")
                x = random.randint(0, 1)
                image = pp.yut_0_image
                if (x == 1):
                    image = pp.yut_1_image
                    mvcnt += 1
                pp.blit_center(image, pp.find_coord(pp.yut_loc[sum]))
                pygame.display.update()
                sum += 1

            if sum == 4:
                pygame.time.delay(500)
                if mvcnt == 1:
                    pp.blit_center(pp.do_image, pp.find_coord(mvcnt_coord))
                    pygame.display.update()
                elif mvcnt == 2:
                    pp.blit_center(pp.gae_image, pp.find_coord(mvcnt_coord))
                    pygame.display.update()
                elif mvcnt == 3:
                    pp.blit_center(pp.girl_image, pp.find_coord(mvcnt_coord))
                    pygame.display.update()
                elif mvcnt == 4:
                    pp.blit_center(pp.yut_image, pp.find_coord(mvcnt_coord))
                    pygame.display.update()
                else:
                    pp.blit_center(pp.mo_image, pp.find_coord(mvcnt_coord))
                    pygame.display.update()
                    mvcnt = 5

                check += 1
                break
        if check == 1:
            running = False
            pygame.time.delay(700)

    return mvcnt


def comyut():
    mvcnt = 0
    for i in range(4):
        x = random.randint(0,1)
        image = pp.yut_0_image
        if(x == 1):
            image = pp.yut_1_image
        pp.blit_center(image, pp.find_coord(pp.yut_loc[i]))
        pygame.display.update()
        pygame.time.delay(300)
        mvcnt += x

    pygame.time.delay(500)
    if mvcnt == 1:
        pp.blit_center(pp.do_image, pp.find_coord(mvcnt_coord))
        pygame.display.update()
    elif mvcnt == 2:
        pp.blit_center(pp.gae_image, pp.find_coord(mvcnt_coord))
        pygame.display.update()
    elif mvcnt == 3:
        pp.blit_center(pp.girl_image, pp.find_coord(mvcnt_coord))
        pygame.display.update()
    elif mvcnt == 4:
        pp.blit_center(pp.yut_image, pp.find_coord(mvcnt_coord))
        pygame.display.update()
    else:
        pp.blit_center(pp.mo_image, pp.find_coord(mvcnt_coord))
        pygame.display.update()
        mvcnt = 5

    pygame.time.delay(700)
    return mvcnt
playut()