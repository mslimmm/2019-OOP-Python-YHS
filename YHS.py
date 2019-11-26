import pygame
import random
import PlayerClass

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
#

(2,4)   (-1,5)                 (-2,5)   (0,1)

(3,0)   (3,1)   (3,2)   (3,3)   (3,4)   (0,0) (4,0)
"""

def wherego():
    mvcnt = 0
    for i in range(4):
        x = random.randint(0,1)
        mvcnt += x

    if mvcnt == 1:
        print("도")
    elif mvcnt == 2:
        print("개")
    elif mvcnt == 3:
        print("걸")
    elif mvcnt == 4:
        print("윷")
    else:
        print("모")
        mvcnt = 5

    return mvcnt

def actcom(com, play):
    print("컴퓨터의 차례")

    run = True

    while run:
        run = False

        randomlist = []

        for i in range(4):
            if com.egglist[i] in com.onmap:

            randomlist.append(i)

        random.shuffle(randomlist)

        movecnt = wherego()

        if movecnt == 4 or movecnt == 5:
            run = True

        com.egglist[randomlist[0]].move(movecnt)

        if randomlist[0] == com.onmapno:
            com.onmap.append(com.egglist[randomlist[0]])
            com.onmapno += 1

        for i in play.onmap:
            if i.x == com.egglist[randomlist[0]].x and i.y == com.egglist[randomlist[0]].y:
                i.x = 0
                i.y = 0
                i.carrying = 1
                play.onmap.remove(i)    
                play.onmapno -= 1
                run = True
                print("컴퓨터가 당신의 말을 잡았습니다!")

        for i in range(com.onmapno):
            print("컴퓨터의", i + 1, "번째 알의 위치 : ", com.onmap[i].x, com.onmap[i].y)

        if run == True:
            print("컴퓨터가 한번 더 던집니다.")


Player = PlayerClass.player()
Computer = PlayerClass.player()

order = ['first','second']
random.shuffle(order)

if order[0] == 'second':
    print("컴퓨터가 선공입니다.")
    actcom(Computer, Player)

else:
    print("당신이 선공입니다.")

while True:
    print("플레이어")
    actcom(Player,Computer)


