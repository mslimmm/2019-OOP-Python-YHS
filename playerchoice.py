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

누르는 칸 : 20px짜리 정사각형, 말 기준으로 위로 30, 오른쪽으로 30px에 중심이 오게 찍는다.
"""

import PygamePrint as pp
from PlayerClass import *
import pygame, random
from pygame.locals import *
from YHS import *
import yutdunzigi
LEFT = 1
RIGHT = 3

def find_coord(egg):
    return pp.find_coord(pp.find_loc(egg.x, egg.y))

#pp.find_coord(pp.find_loc(com.egglist[i].x, com.egglist[i].y))

def actplayer(Player, Computer):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
    for i in Player.egglist:
        if i not in Player.finegg and -10 < find_coord(i)[0] + 30 - mouse_x < 10 and -10 < find_coord(i)[1] + 30 - mouse_y < 10:
            x = yutdunzigi.playertogo() # 윷던지기.py에서 playertogo를 wheretogo랑 비슷하게 만들 것임

            act(Player, Computer) #act는 가제로, YHS에서 구동하는 함수 이름임.









