import pygame
from pygame.locals import *
import sys
from tile import *

pygame.init()

size = (width, height) = (40*32, 20*32)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
floor = pygame.sprite.Group()
i = 0
j = 0


def create_floor():
    global i
    global j
    map = []
    percent = int(.48 * (width // 32 * height // 32))
    while i < width // 32:
        map.append(["w"]*(height // 32))
        while j < height // 32:
            floor.add(Tile("images/Silmar/tiles/wall12.gif", (i*32, j*32)))
            j+=1
        i += 1


def main():
    create_floor()
    global screen
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    screen = pygame.display.set_mode(size, FULLSCREEN)
                elif event.key == K_ESCAPE:
                    screen = pygame.display.set_mode(size)
            screen.fill(color)
            floor.draw(screen)
            pygame.display.flip()


if __name__ == "__main__":
    main()
