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

    order = ['first','second']
    random.shuffle(order)

    if order[0] == 'second':
        print(com1.name + "가 선공입니다.")
        com1.act(com1, play)
    else:
        print(play.name + "가 선공입니다.")

    while True:

        if com1.fineggno == 4:
            print(com1.name + "가 이겼습니다!")
            break

        play.act(play, com1)

        if play.fineggno == 4:
            print(play.name + "가 이겼습니다!")
            break
        com1.act(com1, play)

        if com1.fineggno == 4:
            print(com1.name + "가 이겼습니다!")
            break


