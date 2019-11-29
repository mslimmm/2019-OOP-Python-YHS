import pygame
import PygamePrint as pp
import random

def playut(user):
    sum = 0
    mvcnt = 0
    running = True
    pp.blit_center(user.imagedict['anykey'], pp.find_coord((0, 260)))
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
                pp.yut.play()
                sum += 1

            if sum == 4:
                pygame.time.delay(500)
                mvcnt = pp.print_mvcnt(mvcnt)

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
        pp.yut.play()
        pygame.time.delay(300)
        mvcnt += x

    pygame.time.delay(300)
    mvcnt = pp.print_mvcnt(mvcnt)

    pygame.time.delay(700)
    return mvcnt
