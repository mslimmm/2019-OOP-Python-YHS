import pygame
import random
import PlayerClass
import PygamePrint
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
            com.onmapno -= 1
            com.finegg.append(moving_egg)
            com.fineggno += 1

        for i in play.onmap:
            if i.x == moving_egg.x and i.y == moving_egg.y:
                i.x = 0
                i.y = 0
                i.carrying = 1
                play.onmap.remove(i)
                play.onmapno -= 1
                run = True
                print("컴퓨터가 당신의 말을 잡았습니다!")

        for i in range(4):
            if com.egglist[i] in com.onmap:
                print("컴퓨터의", i + 1, "번째 알의 위치 : ", com.egglist[i].x, com.egglist[i].y)

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
    actcom(Computer,Player)
    if Computer.fineggno == 4:
        print("컴퓨터가 이겼습니다!")
        break