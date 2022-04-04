import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((300, 300))

degree = 0
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    surf = pygame.Surface((100, 100))
    surf.fill(WHITE)
    surf.set_colorkey((255, 0, 0))

    bigger = pygame.Rect(0, 0, 100, 100)

    pygame.draw.rect(surf, BLACK, bigger, 4)

    oldCenter = (150, 150)
    rotatedSurf = pygame.transform.rotate(surf, degree)
    rotRect = rotatedSurf.get_rect()
    rotRect.center = oldCenter
    screen.blit(rotatedSurf, rotRect)

    degree -= 5
    if degree < 0:
        degree = 360

    pygame.display.flip()

pygame.quit()