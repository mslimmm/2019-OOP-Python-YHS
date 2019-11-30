import PygamePrint as pp
import yutdunzigi as yd
import action
import pygame
import random

class User:
    class egg:
        def __init__(self):
            self.x = 0
            self.y = 0
            self.carrying_egg = []
            self.carrying = 1

        def move(self, movecnt):

            if self.x == 1 and self.y == 0:
                self.x = -1
            elif self.x == 2 and self.y == 0:
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
            
            if self.x == -1 and self.y == 3:
                self.x = -2

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
        self.egglist = [self.egg(), self.egg(), self.egg(), self.egg()]
        self.onmap = []
        self.onmapno = 0
        self.finegg = []
        self.fineggno = 0
        if char == 0:
            self.imagelist = pp.haitai_list
            self.imagedict = pp.haitai_dict
            self.locdict = pp.g_loc_dict
            self.image = pp.haitai_1_image
        elif char == 1:
            self.imagelist = pp.dokabi_list
            self.imagedict = pp.dokabi_dict
            self.locdict = pp.r_loc_dict
            self.image = pp.dokabi_1_image



    def make_carry(self,egg1,egg2):
        egg1.carrying_egg.append(egg2)
        egg1.carrying += 1
        egg2.carrying_egg.append(egg1)
        egg2.carrying += 1

    def carry_image(self):
        for egg in self.egglist:
            egg.image = self.imagelist[egg.carrying]

class Player(User):
    def __init__(self, char):
        super().__init__(char)

    def wherego(self):
        return yd.playut(self)

    def act(self, user2):# 임시로 자동이동으로 함
        action.actplay(self, user2)

class Computer(User):
    def __init__(self, char):
        super().__init__(char)

    def wherego(self):
        return yd.comyut()

    def act(self, user2):
        action.actcom(self, user2)
