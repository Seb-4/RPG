import pygame
from pygame.locals import *
import sys
from tile import *
from player import *
import random

pygame.init()

size = (width, height) = (40*32, 20*32)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
floor = pygame.sprite.Group()
wall = pygame.sprite.Group()
players = pygame.sprite.Group()


def create_floor():
    # Set Up the level
    global level
    level = []
    f = 0
    x = random.randint(0, 39)
    y = random.randint(0, 19)
    for i in range(width // 32):
        level.append(["w"]*(height // 32))

    # Create the level
    percent = 400
    while f < percent:
        print(x, y)
        dir = random.randint(0, 3)
        if dir == 0 and y > 0:
            y -= 1
        if dir == 1 and x < 39:
            x += 1
        if dir == 2 and y < 19:
            y += 1
        if dir == 3 and x > 0:
            x -= 1
        if level[x][y] == "w":
            level[x][y] = "f"
            f += 1
            print(f)
    for row in level:
        print(row)

    # Draw the level
    for i in range(width // 32):
        for j in range(height // 32):
            if level[i][j] == "w":
                wall.add(Tile("Silmar/tiles/wall12.gif", (i * 32, j * 32)))
            if level[i][j] == "f":
                floor.add(Tile("Silmar/tiles/floor13.gif", (i * 32, j * 32)))
    x = 0
    y = 0
    while level[x][y] != "f":
        x = random.randint(0, 39)
        y = random.randint(0, 19)
    players.add(Player("Silmar/player/battlemage.gif", (x, y)))


def main():
    global screen
    create_floor()
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
        wall.draw(screen)
        players.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
