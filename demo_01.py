import pygame
from pygame.locals import Rect

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([740, 580])
pygame.display.set_caption("pygame demo - Modified Version")

running = True
x1, y1 = 0, 2
a, b = 180, 180
# infinite loop top ----
while running:
    # press ctrl-c to stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100, 0, 0))  # back ground color

    pygame.draw.circle(screen, (176, 176, 222), (520, 300), a)
    pygame.draw.circle(screen, (222, 176, 222), (120, 300), b)
    pygame.draw.rect(screen, (b, a, b), Rect(140, 140, 300, 220))
    pygame.draw.polygon(screen, (255, 255, 255), [(320, 480), (160, 320),(458, 320)], 0)

    a += 3
    b += -3
    color_on = (240, 0, 120)
    color_off = (120, 220, 120)
    for x0 in range(5):
        for y0 in range(7):
            # pygame.draw.circle(screen, color_off, (24 + x0 * 16, 24 + y0 * 16), 8)
            pygame.draw.rect(screen, color_off, Rect(24 + x0 * 16, 24 + y0 * 16, 12, 12))

    # pygame.draw.circle(screen, color_on, (24 + x1 * 16, 24 + y1 * 16), 8)
    pygame.draw.rect(screen, color_on, Rect(24 + x1 * 16, 24 + y1 * 16, 12, 12))
    x1 += 1
    if x1 > 4:
        x1 = 0

    pygame.display.flip()  # update
    clock.tick(5)  # FPS, Frame Per Second
# infinite loop bottom ----

pygame.quit()
