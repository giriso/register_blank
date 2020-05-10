import pygame
import sys
import os

hero = (100, 100)
all_sprites = pygame.sprite.Group()
CHANGE = 10
SCREEN = (2720, 500)
count = 0

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.run1 = load_image('run1.png')
        self.run2 = load_image('run2.png')
        self.run3 = load_image('run3.png')
        self.run4 = load_image('run4.png')

        self.run1 = pygame.transform.scale(self.run1, (100, 100))
        self.run2 = pygame.transform.scale(self.run2, (100, 100))
        self.run3 = pygame.transform.scale(self.run3, (100, 100))
        self.run4 = pygame.transform.scale(self.run4, (100, 100))

        self.animations = [self.run1, self.run2, self.run3, self.run4]
        self.clock = pygame.time.Clock()

        self.count = 0

        pygame.time.set_timer(CHANGE, 10)

    def update(self):
        self.rect.x = 100
        self.rect.y = 100
        self.image = self.animations[self.count // len(self.animations)]


class Runner:
    def __init__(self):
        self.EVENT = 30
        self.screen = pygame.display.set_mode(SCREEN)
        self.camerax = 0
        self.gravity = 0
        self.playerx = 0
        self.playery = 100
        self.jump = 0
        self.fon = load_image('fon-cosmos.jpg')
        self.fon = pygame.transform.scale(self.fon, SCREEN)
        self.hero = load_image('run4.png').convert()
        self.hero = pygame.transform.scale(self.hero, (200, 100))
        self.hero.set_colorkey((0, 0, 0))
        self.road = load_image('road.png').convert()
        self.road = pygame.transform.scale(self.road, (SCREEN[0], 100))
        self.count = 0
        self.gravity = 0
        self.in_jump = False
        self.h_jump = 20

        self.run1 = load_image('run1.png')
        self.run2 = load_image('run2.png')
        self.run3 = load_image('run3.png')
        self.run4 = load_image('run4.png')

        self.run1 = pygame.transform.scale(self.run1, hero)
        self.run2 = pygame.transform.scale(self.run2, hero)
        self.run3 = pygame.transform.scale(self.run3, hero)
        self.run4 = pygame.transform.scale(self.run4, hero)

        self.animations = [self.run1, self.run2, self.run3, self.run4]
        self.clock = pygame.time.Clock()

        self.count = 0

        pygame.time.set_timer(self.EVENT, 100)

    def draw(self):
        self.screen.blit(self.fon, (0, 0))
        self.screen.blit(self.road, (0, 100))
        if self.in_jump:
            if self.playery == 100 + self.h_jump:
                self.in_jump = False
            else:
                self.playery += self.jump
        else:
            key = pygame.key.get_pressed()
            self.screen.blit(self.animations[self.count % len(self.animations)], (self.playerx, self.playery))

    def run(self):
        keys = pygame.key.get_pressed()
        while True:
            self.screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == self.EVENT:
                    self.count += 1
                    self.playerx += 10
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.in_jump = True
                        self.jump = 5
            self.draw()
            pygame.display.flip()
            print(self.jump)

Runner().run()
