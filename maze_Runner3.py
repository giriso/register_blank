import pygame
import sys
import os
import random
from pygame.locals import *


hero = (10, 10)
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
CHANGE = 30
W, H = 800, 440
SCREEN = (W, H)
count = 0
screen = pygame.display.set_mode(SCREEN)
clock = pygame.time.Clock()
pygame.time.set_timer(CHANGE, 10)
NEW_PLATFORM = 16
v = 25
jump_v = 0
g = 20
playerx = 10
playery = 100


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


bg = load_image('bg.png').convert()
x = 0
speed = 100
run = True

pygame.time.set_timer(NEW_PLATFORM, 100)


class Hero(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.run1 = load_image('run111.png')
        self.run2 = load_image('run222.png')
        self.run3 = load_image('run333.png')
        self.run4 = load_image('run444.png')

        self.animations = [self.run1, self.run2, self.run3, self.run4]

        pygame.time.set_timer(CHANGE, 10)

        self.image = self.animations[0]
        self.rect = self.image.get_rect()
        self.rect.x = playerx
        self.rect.y = playery

        pygame.time.set_timer(CHANGE, 100)

    def update(self):
        self.image = self.animations[count % len(self.animations)]
        self.rect.x = playerx
        self.rect.y = playery


class Platform(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        heights = [100, 200, 300, 400]
        self.image = load_image('road.png')
        self.image = pygame.transform.scale(self.image, (random.randint(100, 300), 10))
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = random.choice(heights)

        pygame.time.set_timer(NEW_PLATFORM, 10000)


Hero(all_sprites)
Platform(platforms)
while True:
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == CHANGE:
            if jump_v:
                playery -= jump_v
                jump_v -= g
                if jump_v <= 0:
                    jump_v = 0
            else:
                for i in all_sprites:
                    if not pygame.sprite.spritecollideany(i, platforms):
                        playery += g
            count += 1
            for i in platforms:
                i.rect.x -= v
        if event.type == NEW_PLATFORM:
            Platform(platforms)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump_v = 60

    bgx = x % bg.get_rect().width
    screen.blit(bg, (bgx - bg.get_rect().width, 0))
    if bgx < W:
        screen.blit(bg, (bgx, 0))
    x -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    all_sprites.draw(screen)
    all_sprites.update()
    platforms.draw(screen)
    platforms.update()
    pygame.display.update()
    clock.tick(speed)