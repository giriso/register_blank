import pygame
import os

width, height = 800, 500
screen = pygame.display.set_mode((width, height))
running = True
screen.fill((0, 0, 0))
pygame.mouse.set_visible(False)
all_sprites = pygame.sprite.Group()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


cursor_image = load_image('arrow.png').pygame.transform.scale(10, 10)
cursor = pygame.sprite.Sprite(all_sprites)
cursor.image = cursor_image
cursor.rect = cursor.image.get_rect()
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    cursor.rect.x = pygame.mouse.get_pos()[0]
    print(pygame.mouse.get_pos()[0])
    print(pygame.mouse.get_pos()[1])
    cursor.rect.y = pygame.mouse.get_pos()[1]
    if pygame.mouse.get_focused():
        all_sprites.draw(screen)
        all_sprites.update()
    pygame.display.flip()