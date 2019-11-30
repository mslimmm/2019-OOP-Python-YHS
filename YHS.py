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

def play(mode):
    if mode == 0:
        user1 = UserClass.Computer(0)
        user2 = UserClass.Computer(1)
    if mode == 1:
        user1 = UserClass.Player(0)
        user2 = UserClass.Computer(1)
    if mode == 2:
        user1 = UserClass.Player(0)
        user2 = UserClass.Player(1)

    pp.print_all(user2, user1)
    pygame.display.update()

    order = ['first','second']
    random.shuffle(order)

    if order[0] == 'second':
        pp.situation(user1, user2, 'first')
        pp.situation(user1, user2, 'turn')
        user1.act(user2)

    else:
        pp.situation(user2, user1, 'first')

    while True:

        if user1.fineggno == 4:
            pp.situation(user1, user2, 'win')
            break

        pp.situation(user2, user1, 'turn')
        user2.act(user1)

        if user2.fineggno == 4:
            pp.situation(user2, user1, 'win')
            break

        pp.situation(user1, user2, 'turn')
        user1.act(user2)

        if user1.fineggno == 4:
            pp.situation(user1, user2, 'win')
            break


