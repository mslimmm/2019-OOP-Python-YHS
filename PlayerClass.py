import PygamePrint as pp
class player: #컴퓨터와 플레이어
    class egg: #가지고 있는 알의 특성
        def __init__(self):
            self.x = 0
            self.y = 0
            self.carrying_egg = []
            self.carrying = 1
            self.image = pp.haitai_1_image


        def move(self, movecnt):

            if self.x == 1 and self.y == 0:
                self.x = -1
            elif self.x == 2 and self.y == 0:
                self.x = -2
            elif self.x == -1 and self.y == 3:
                self.x = -2

            for i in range(movecnt):
                self.y += 1
                if 0 <= self.x <= 3 and self.y == 5:
                    self.y = 0
                    self.x += 1
                elif self.x == -1 and self.y == 6:
                    self.y = 0
                    self.x = 3
                elif self.x == -2 and self.y == 6:
                    self.y = 0
                    self.x = 4

                if self.x == 4 and self.y > 0:
                    break

            for i in self.carrying_egg:
                i.x = self.x
                i.y = self.y

        def catched(self):

            self.x = 0
            self.y = 0
            self.carrying = 1

            for i in self.carrying_egg:
                i.x = 0
                i.y = 0
                i.carrying = 1
                i.carrying_egg.clear()

            self.carrying_egg.clear()

    def __init__(self):
        self.egglist = [self.egg(), self.egg(), self.egg(), self.egg()]
        self.onmap = []
        self.onmapno = 0
        self.finegg = []
        self.fineggno = 0

    def make_carry(self,egg1,egg2):
        egg1.carrying_egg.append(egg2)
        egg1.carrying += 1
        egg2.carrying_egg.append(egg1)
        egg2.carrying += 1
        if egg1.carrying == 1:
            egg1.image = pp.haitai_1_image
            egg2.image = pp.haitai_1_image
        if egg1.carrying == 2:
            egg1.image = pp.haitai_2_image
            egg2.image = pp.haitai_2_image
        if egg1.carrying == 3:
            egg1.image = pp.haitai_3_image
            egg2.image = pp.haitai_3_image
        if egg1.carrying == 4:
            egg1.image = pp.haitai_4_image
            egg2.image = pp.haitai_4_image