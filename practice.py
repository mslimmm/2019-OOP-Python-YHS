import pygame

pygame.init()
screen_x = 800
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("메인")


class SimpleSprite(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.user_src_image = pygame.image.load(image)
        self.user_position = position
        self.user_rotation = 30

    def update(self):
        self.image = pygame.transform.rotate(self.user_src_image, self.user_rotation)  # 이미지를 회전 각도 만큼 회전시킨다
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position


simple1 = SimpleSprite("images/gaeyo.png", (300, 300))
simple2 = SimpleSprite("images/gaeyo.png", (100, 100))
simple_group = pygame.sprite.Group(simple1, simple2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    simple_group.update()
    screen.fill((255, 255, 255))
    simple_group.draw(screen)


