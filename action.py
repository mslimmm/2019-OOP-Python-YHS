import PygamePrint as pp
import pygame
import random


def actcom(user1, user2):

    run = True

    while run:
        run = False
        pp.print_all(user1, user2)
        pygame.time.delay(500)
        randomlist = []

        for i in range(4):
            if user1.egglist[i] in user1.onmap:
                randomlist.append(i)

        for i in range(4):
            if user1.egglist[i] not in user1.onmap and user1.egglist[i] not in user1.finegg:
                randomlist.append(i)
                break

        random.shuffle(randomlist)

        movecnt = user1.wherego()

        if movecnt == 4 or movecnt == 5:
            run = True

        moving_egg = user1.egglist[randomlist[0]]
        moving_egg.move(movecnt)

        if moving_egg not in user1.onmap:
            user1.onmap.append(moving_egg)
            user1.onmapno += 1

        if moving_egg.x == 4 and moving_egg.y > 0:
            user1.onmap.remove(moving_egg)
            user1.finegg.append(moving_egg)
            for i in moving_egg.carrying_egg:
                user1.onmap.remove(i)
                user1.finegg.append(i)
            user1.onmapno -= moving_egg.carrying
            user1.fineggno += moving_egg.carrying

        chk = 0
        for i in user2.onmap:
            if i.x == moving_egg.x and i.y == moving_egg.y:
                i.catched()
                for j in i.carrying_egg:
                    user2.onmap.remove(j)
                    user2.onmapno -= 1
                user2.onmap.remove(i)
                user2.onmapno -= 1
                i.carrying_egg.clear()
                run = True
                pp.situation(user1, user2, 'catch')
                chk = 1

        if chk == 0:
            if movecnt == 4:
                chk = 1
                pp.situation(user1, user2, 'yut')
            elif movecnt == 5:
                chk = 1
                pp.situation(user1, user2, 'mo')

        for i in user1.onmap:
            for j in user1.onmap:
                if i.x == j.x and i.y == j.y and i is not j and i not in j.carrying_egg and j not in i.carrying_egg:
                    user1.make_carry(i,j)
                    pp.situation(user1, user2, 'carry')
                    chk = 1

        if chk == 0:
            pp.print_all(user1, user2)
            pygame.time.delay(1000)

        if user1.fineggno == 4:
            run = False