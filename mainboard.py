import pygame
import PygamePrint as pp
from pygame.locals import *
import os
import sys

os.environ['SDL_VIDEO_CENTERED'] = '0'

pygame.init()
pygame.display.set_caption("main")
screen_x = 800
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))

game_start = pygame.image.load("images/game_start.png")
game_intro = pygame.image.load("images/game_introduction.png")
zapgi_upgi = pygame.image.load("images/zapgi_upgi.png")
gaeyo = pygame.image.load("images/gaeyo.png")
malpan = pygame.image.load("images/malpan.png")
sem = pygame.image.load("images/sem.png")
gaeyo_board = pygame.image.load("images/gaeyo_board.png")
malpan_board = pygame.image.load("images/malpan_board.png")
sem_board = pygame.image.load("images/sem_board.png")
zapgi_upgi_board = pygame.image.load("images/gaeyo_board.png")
name = pygame.image.load("images/name.png")
backspace = pygame.image.load("images/backspace.png")

'''
screen.fill((255, 255, 255))
pp.blit_center(game_start, pp.find_coord((0, 150)))
pp.blit_center(game_intro, pp.find_coord((0, 0)))
pp.blit_center(gaeyo, pp.find_coord((0, 150)))
pp.blit_center(zapgi_upgi, pp.find_coord((0, 0)))
pp.blit_center(malpan, pp.find_coord((0, -150)))

pygame.display.update()
pygame.time.delay(1000)

'''

spot_gs = pp.find_coord((0, -100))
spot_gi = pp.find_coord((0, -200))
spot_gaeyo = pp.find_coord((0, 150))
spot_sem = pp.find_coord((0, 50))
spot_malpan = pp.find_coord((0, -50))
spot_zapgi_upgi = pp.find_coord((0, -150))
spot_backspace = pp.find_coord((350, 275))

def IsReal(pos, spot_coord, garo, sero):
    return -garo/2 < pos[0] - spot_coord[0] < garo/2 and -sero/2 < pos[1] - spot_coord[1] < sero/2
LEFT = 1
RIGHT = 3
cnt = 0
running = True
MainMenu = True
Intro = False
Intro1 = False
Intro2 = False
Intro3 = False

GamePlay = True

while running:

    if MainMenu:
        screen.fill((255, 204, 102))
        pp.blit_center(name, pp.find_coord((0, 50)))
        pp.blit_center(game_start, pp.find_coord((0, -100)))
        pp.blit_center(game_intro, pp.find_coord((0, -200)))
        pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                print(mouse_x, mouse_y)
                print(spot_gi[0], spot_gi[1])

                '''screen.fill((255, 255, 255))
                pp.blit_center(gaeyo, pp.find_coord((0, 150)))
                pp.blit_center(zapgi_upgi, pp.find_coord((0, 0)))
                pp.blit_center(malpan, pp.find_coord((0, -150)))
                pygame.display.update()
                pygame.time.delay(10000)'''
                if IsReal(pos, spot_gi, 300, 50):
                    #-150 < mouse_x - spot_gi[0] < 150 and -25 < mouse_y - spot_gi[1] < 25
                    print(1)
                    MainMenu = False
                    Intro = True
    if Intro:
        screen.fill((255, 204, 102))
        pp.blit_center(backspace, pp.find_coord((350, 275)))
        pp.blit_center(gaeyo, pp.find_coord((0, 150)))
        pp.blit_center(sem, pp.find_coord((0, 50)))
        pp.blit_center(malpan, pp.find_coord((0, -50)))
        pp.blit_center(zapgi_upgi, pp.find_coord((0, -150)))
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                print(mouse_x, mouse_y)
                if IsReal(pos, spot_gaeyo, 300, 50):
                    #-150 < mouse_x - spot_gi[0] < 150 and -25 < mouse_y - spot_gi[1] < 25
                    print(1)
                    Intro = False
                    Intro1 = True
                elif IsReal(pos, spot_sem, 300, 50):
                    print(1)
                    Intro = False
                    Intro2 = True
                elif IsReal(pos, spot_malpan, 300, 50):
                    print(1)
                    Intro = False
                    Intro3 = True
                elif IsReal(pos, spot_zapgi_upgi, 300, 50):
                    print(1)
                    Intro = False
                    Intro4 = True
                if IsReal(pos, spot_backspace, 100, 50):
                    Intro = False
                    MainMenu = True

    if Intro1:
        screen.fill((255, 204, 102))
        pp.blit_center(backspace, pp.find_coord((350, 275)))
        pp.blit_center(gaeyo_board, pp.find_coord((0, 0)))
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if IsReal(pos, spot_backspace, 100, 50):
                Intro1 = False
                Intro = True
    '''if Intro2:
        screen.fill((255, 204, 102))
        pp.blit_center(backspace, pp.find_coord((350, 275)))
        pp.blit_center(sem_board, pp.find_coord((0, 0)))
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if IsReal(pos, spot_backspace, 100, 50):
                Intro1 = False
                Intro = True
    if Intro3:
        screen.fill((255, 204, 102))
        pp.blit_center(backspace, pp.find_coord((350, 275)))
        pp.blit_center(gaeyo_board, pp.find_coord((0, 0)))
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if IsReal(pos, spot_backspace, 100, 50):
                Intro1 = False
                Intro = True
    if Intro4:
        screen.fill((255, 204, 102))
        pp.blit_center(backspace, pp.find_coord((350, 275)))
        pp.blit_center(gaeyo_board, pp.find_coord((0, 0)))
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if IsReal(pos, spot_backspace, 100, 50):
                Intro1 = False
                Intro = True'''


