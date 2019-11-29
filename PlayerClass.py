import PygamePrint as pp

class player:
    class egg:
        def __init__(self, char):
            self.x = 0
            self.y = 0
            self.carrying_egg = []
            self.carrying = 1
            if char == 'haitai':
                self.imagelist = pp.haitai_list
                self.image = pp.haitai_list[1]
            elif char == 'dokabi':
                self.imagelist = pp.dokabi_list
                self.image = pp.dokabi_list[1]


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


    def __init__(self, char):
        self.egglist = [self.egg(char), self.egg(char), self.egg(char), self.egg(char)]
        self.onmap = []
        self.onmapno = 0
        self.finegg = []
        self.fineggno = 0
        if char == 'haitai':
            self.name = "해태"
        elif char == 'dokabi':
            self.name = '도깨비'

    def make_carry(self,egg1,egg2):
        egg1.carrying_egg.append(egg2)
        egg1.carrying += 1
        egg2.carrying_egg.append(egg1)
        egg2.carrying += 1

    def carry_image(self):
        for egg in self.egglist:
            egg.image = egg.imagelist[egg.carrying]


'''
유저 클래스로 개편
'''




'''
    class User:
        class egg:
            def __init__(self, char):
                self.x = 0
                self.y = 0
                self.carrying_egg = []
                self.carrying = 1
                if char == 'haitai':
                    self.imagelist = pp.haitai_list
                    self.image = pp.haitai_list[1]
                elif char == 'dokabi':
                    self.imagelist = pp.dokabi_list
                    self.image = pp.dokabi_list[1]

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

        def __init__(self, char):
            self.egglist = [self.egg(char), self.egg(char), self.egg(char), self.egg(char)]
            self.onmap = []
            self.onmapno = 0
            self.finegg = []
            self.fineggno = 0
            if char == 'haitai':
                self.name = "해태"
            elif char == 'dokabi':
                self.name = '도깨비'

        def make_carry(self, egg1, egg2):
            egg1.carrying_egg.append(egg2)
            egg1.carrying += 1
            egg2.carrying_egg.append(egg1)
            egg2.carrying += 1

        def carry_image(self):
            for egg in self.egglist:
                egg.image = egg.imagelist[egg.carrying]

    class Player(User):
        def playertogo(self):
            pass

    class Com(User):
        def wherego(self):
'''