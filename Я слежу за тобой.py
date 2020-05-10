import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
run = True
count = 0


while run:
    font = pygame.font.Font(None, 30)
    text_lost = font.render(str(count), 1, (255, 255, 255))
    screen.blit(text_lost, (250, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.WINDOWEVENT_CLOSE:
            print(event)
            count += 1

pygame.quit()