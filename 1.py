import pygame

pygame.init()

win = pygame.display.set_mode([640, 480])
size = [640, 480]
pygame.display.set_caption("YHS")

win.fill((255, 255, 255))


def coord(loc):
    return [size[0]/2+loc[0], size[1]/2-loc[1]]


class Node:
    def __init__(self, loc):
        self.next = []
        self.x, self.y = coord(loc)

    def draw(self):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 10, 1)
        pygame.display.flip()


start = Node([300, -300])
done = False

while not done:
    pygame.time.delay(1000)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True
    start.draw()

pygame.quit()

"""
(2,0)   (1,4)   (1,3)   (1,2)   (1,1)   (1,0)


(2,1)   (-2,1)                 (-1,1)   (0,4)


(2,2)       (-2,2)         (-1,2)       (0,3)
                   (-1,3)
                   (-2,3)
(2,3)       (-1,4)         (-2,4)       (0,2)


(2,4)   (-1,5)                 (-2,5)   (0,1)

(3,0)   (3,1)   (3,2)   (3,3)   (3,4)   (0,0) (4,0)
"""