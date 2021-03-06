import pygame, sys
from pygame.locals import *

pygame.init()

# Frames Per Second
FPS = 30
clock = pygame.time.Clock()

size = (480, 320)
screen = pygame.display.set_mode(size)

# define color using Red, Green, Blue values
# 0 is blank
# 255 is maximum

RED = (255, 0, 0)  # all red. no other color
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# left edge of rectangle, top, width height
player_rect = pygame.Rect(160, 160, 64, 64)
player = pygame.image.load("girl.png")

up_rect = pygame.Rect(410, 100, 50, 50)
uparrow = pygame.image.load("50pxarrowup.png")
down_rect = pygame.Rect(410, 180, 50, 50)
dwnarrow = pygame.image.load("50pxarrowdwn.png")

direction = ""


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if up_rect.collidepoint(mouse_pos):
                direction = "up"
            if down_rect.collidepoint(mouse_pos):
                direction = "down"

    if direction == "down":
        player_rect.centery += 1
    elif direction == "up":
        player_rect.centery -= 1

    if player_rect.bottom > size[1]:
        direction = "up"
    if player_rect.top < 0:
        direction = "down"
        

    screen.fill(BLACK)
    # pygame.draw.rect(screen, RED, player_rect)
    screen.blit(player, player_rect)
    
    # pygame.draw.rect(screen, GREEN, up_rect)
    screen.blit(uparrow, up_rect)
    # pygame.draw.rect(screen, BLUE, down_rect)
    screen.blit(dwnarrow, down_rect)
    
    # slow the game down to 30 frames per second
    clock.tick(FPS)
    pygame.display.update()