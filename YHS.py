import pygame
import random
import PlayerClass
import PygamePrint as pp
import os
"""
업기
스페이스
도 1
개 2
걸 3
윷 4
모 5
(2,0)   (1,4)   (1,3)   (1,2)   (1,1)   (1,0)

(2,1)   (-2,1)                 (-1,1)   (0,4)

(2,2)       (-2,2)         (-1,2)       (0,3)

                   (-1,3)
                   (-2,3)
                   
(2,3)       (-1,4)         (-2,4)       (0,2)

(2,4)   (-1,5)                 (-2,5)   (0,1)

(3,0)   (3,1)   (3,2)   (3,3)   (3,4)   (0,0) (4,0)
"""
pygame.init()
sound = pygame.mixer.Sound("sounds/Scream10.ogg")
sound.set_volume(0.5)
os.environ['SDL_VIDEO_CENTERED'] = '0'

pygame.display.set_caption("YUT")

def print_all(com, play):
    com.carry_image()
    play.carry_image()
    pp.blit_center(pp.back_image, pp.find_coord((0, 0)))
    pp.print_board()
    for i in range(4):
        if com.egglist[i] in com.onmap:
            pp.blit_center(com.egglist[i].image, pp.find_coord(pp.find_loc(com.egglist[i].x, com.egglist[i].y)))
        if play.egglist[i] in play.onmap:
            pp.blit_center(play.egglist[i].image, pp.find_coord(pp.find_loc(play.egglist[i].x, play.egglist[i].y)))
    pygame.display.update()

def wherego():
    mvcnt = 0
    for i in range(4):
        x = random.randint(0,1)
        image = pp.yut_0_image
        if(x == 1):
            image = pp.yut_1_image
        pp.blit_center(image, pp.find_coord(pp.yut_loc[i]))
        pygame.display.update()
        sound.play()
        pygame.time.delay(300)
        mvcnt += x

    pygame.time.delay(500)
    if mvcnt == 1:
        pp.blit_center(pp.do_image, pp.find_coord((0, 0)))
        pygame.display.update()
    elif mvcnt == 2:
        pp.blit_center(pp.gae_image, pp.find_coord((0, 0)))
        pygame.display.update()
    elif mvcnt == 3:
        pp.blit_center(pp.girl_image, pp.find_coord((0, 0)))
        pygame.display.update()
    elif mvcnt == 4:
        pp.blit_center(pp.yut_image, pp.find_coord((0, 0)))
        pygame.display.update()
    else:
        pp.blit_center(pp.mo_image, pp.find_coord((0, 0)))
        pygame.display.update()
        mvcnt = 5

    pygame.time.delay(700)
    return mvcnt

def actcom(com, play):

    run = True

    while run:
        run = False
        print_all(com, play)
        pygame.time.delay(500)
        randomlist = []

        for i in range(4):
            if com.egglist[i] in com.onmap:
                randomlist.append(i)

        for i in range(4):
            if com.egglist[i] not in com.onmap and com.egglist[i] not in com.finegg:
                randomlist.append(i)
                break

        random.shuffle(randomlist)
        movecnt = wherego()

        if movecnt == 4 or movecnt == 5:
            run = True

        moving_egg = com.egglist[randomlist[0]]
        moving_egg.move(movecnt)

        if moving_egg not in com.onmap:
            com.onmap.append(moving_egg)
            com.onmapno += 1

        if moving_egg.x == 4 and moving_egg.y > 0:
            com.onmap.remove(moving_egg)
            com.finegg.append(moving_egg)
            for i in moving_egg.carrying_egg:
                com.onmap.remove(i)
                com.finegg.append(i)
            com.onmapno -= moving_egg.carrying
            com.fineggno += moving_egg.carrying

        for i in play.onmap:
            if i.x == moving_egg.x and i.y == moving_egg.y:
                i.catched()
                for j in i.carrying_egg:
                    play.onmap.remove(j)
                    play.onmapno -= 1
                play.onmap.remove(i)
                play.onmapno -= 1
                i.carrying_egg.clear()
                run = True
                print(com.name + "가 말을 잡았습니다!")

        for i in com.onmap:
            for j in com.onmap:
                if i.x == j.x and i.y == j.y and i is not j and i not in j.carrying_egg and j not in i.carrying_egg:
                    com.make_carry(i,j)
                    print(com.name + "가 말을 업었습니다.")


        print_all(com, play)
        pygame.time.delay(500)

        if com.fineggno == 4:
            run = False

        if run == True:
            print(com.name + "가 한번 더 던집니다.")

def play():
    Player = PlayerClass.player('haitai')
    Computer = PlayerClass.player('dokabi')

    order = ['first','second']
    random.shuffle(order)

    if order[0] == 'second':
        print(Computer.name + "가 선공입니다.")
        actcom(Computer, Player)
    else:
        print(Player.name + "가 선공입니다.")

    pp.blit_center(pp.back_image, pp.find_coord((0, 0)))
    pp.print_board()
    pygame.display.update()
    pygame.time.delay(500)

    while True:

        if Computer.fineggno == 4:
            print(Computer.name + "가 이겼습니다!")
            break

        actcom(Player, Computer)

        if Player.fineggno == 4:
            print(Player.name + "가 이겼습니다!")
            break
        actcom(Computer, Player)

        if Computer.fineggno == 4:
            print(Computer.name + "가 이겼습니다!")
            break


