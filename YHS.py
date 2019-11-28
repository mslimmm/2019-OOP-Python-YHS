import pygame
import random
import PlayerClass
import PygamePrint as pp
import UserClass
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
os.environ['SDL_VIDEO_CENTERED'] = '0'

pygame.display.set_caption("YUT")

def play():
    com1 = UserClass.Computer('컴퓨터')
    play = UserClass.Player('플레이어')

    pp.print_all(com1, play)
    pygame.display.update()

    order = ['first','second']
    random.shuffle(order)

    if order[0] == 'second':
        pp.blit_center(com1.imagedict['first'], pp.find_coord((0, 260)))
        pygame.display.update()
        pygame.time.delay(1000)
        pp.print_all(com1, play)
        pygame.display.update()

        pp.blit_center(com1.imagedict['turn'], pp.find_coord((0, 0)))
        pygame.display.update()
        pygame.time.delay(1000)
        pp.print_all(com1, play)
        pygame.display.update()
        com1.act(com1, play)

    else:
        pp.blit_center(play.imagedict['first'], pp.find_coord((0, 260)))
        pygame.display.update()
        pygame.time.delay(1000)
        pp.print_all(com1, play)
        pygame.display.update()

    while True:

        if com1.fineggno == 4:
            pp.blit_center(com1.imagedict['win'], pp.find_coord((0, 0)))
            pygame.display.update()
            pygame.time.delay(1000)
            break

        pp.blit_center(play.imagedict['turn'], pp.find_coord((0, 0)))
        pygame.display.update()
        pygame.time.delay(1000)
        pp.print_all(play, com1)
        pygame.display.update()
        play.act(play, com1)

        if play.fineggno == 4:
            pp.blit_center(play.imagedict['win'], pp.find_coord((0, 0)))
            pygame.display.update()
            pygame.time.delay(1000)
            break

        pp.blit_center(com1.imagedict['turn'], pp.find_coord((0, 0)))
        pygame.display.update()
        pygame.time.delay(1000)
        pp.print_all(com1, play)
        pygame.display.update()
        com1.act(com1, play)

        if com1.fineggno == 4:
            pp.blit_center(com1.imagedict['win'], pp.find_coord((0, 0)))
            pygame.display.update()
            pygame.time.delay(1000)
            break


