"""
업기
잡기
4개
팀 2개
스페이스 ->
방향 선택

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

import PygamePrint
import PlayerClass
import pygame, sys, random
from pygame.locals import *
import os
def actplayer(Player):
    number = Player.onmapno
    x = ''
    print("움직이고 싶은 말의 번호를 움직여 주세요")
    input(x)
    while int(x) >= 4 or int(x) < 0:
        print("다시 입력해주세요")
        input(x)
    move = int(x)
    PlayerClass.player.move(Player.egglist[move], movecnt)






