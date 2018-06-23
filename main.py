from pygame.locals import *
import sys
from tile import *
from player import *
from dead import *
import random

pygame.init()

size = (width, height) = (40*32, 20*32)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
alive = True
pygame.font.sysFont('oldenglishtext', 32)
floor = pygame.sprite.Group()
wall = pygame.sprite.Group()
players = pygame.sprite.Group()
ends = pygame.sprite.Group()
keys = pygame.sprite.Group()
enemies = pygame.sprite.Group()


def create_floor():
    global mage
    global key
    global end
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
        dir = random.randint(0, 3)
        if dir == 0 and y > 1:
            y -= 1
        if dir == 1 and x < 38:
            x += 1
        if dir == 2 and y < 18:
            y += 1
        if dir == 3 and x > 1:
            x -= 1
        if level[x][y] == "w":
            level[x][y] = "f"
            f += 1

    # Make the Exit
    global endx
    global endy
    endx = random.randint(0, 39)
    endy = random.randint(0, 19)
    while level[endx][endy] != "f":
        endx = random.randint(0, 39)
        endy = random.randint(0, 19)
    level[endx][endy] = "e"

    # Make the Key
    keyx = random.randint(0, 39)
    keyy = random.randint(0, 19)
    while level[keyx][keyy] != "f":
        keyx = random.randint(0, 39)
        keyy = random.randint(0, 19)
    level[keyx][keyy] = "k"

    # Draw the level
    for i in range(width // 32):
        for j in range(height // 32):
            if level[i][j] == "w":
                wall.add(Tile("wall12.gif", (i * 32, j * 32)))
            if level[i][j] == "f" or level[i][j] == "k":
                floor.add(Tile("floor13.gif", (i * 32, j * 32)))
            if level[i][j] == "e":
                end = Tile("door12.gif", (i * 32, j * 32))
                ends.add(end)
            if level[i][j] == "k":
                key = Tile("key.png", (i * 32, j * 32))
                keys.add(key)

    # Create Player
    x = 0
    y = 0
    while level[x][y] != "f":
        x = random.randint(0, 39)
        y = random.randint(0, 19)
    mage = Player("battlemage.gif", (x * 32, y * 32), 100, 5)
    players.add(mage)

    # Create Enemies
    for i in range(10):
        x = 0
        y = 0
        while level[x][y] != "f":
            x = random.randint(0, 39)
            y = random.randint(0, 19)
        bad = Player("yellow_snake.png", (x * 32, y * 32), 15, 1)
        enemies.add(bad)


def main():
    global screen
    global level
    global alive
    haveKey = False
    stage = 1
    count = 0
    create_floor()
    while True:
        clock.tick(60)

        # Events
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    screen = pygame.display.set_mode(size, FULLSCREEN)
                elif event.key == K_ESCAPE:
                    screen = pygame.display.set_mode(size)
                elif event.key == K_r:
                    alive = True
                    stage = 1
                    haveKey = False
                    ends.remove(ends, 0)
                    keys.remove(keys, 0)
                    players.remove(players, 0)
                    enemies.remove(enemies, 0)
                    for i in range(len(wall)):
                        wall.remove(wall, i)
                    for i in range(len(floor)):
                        floor.remove(floor, i)
                    create_floor()
                elif event.key == K_UP:
                    if level[mage.x//32][(mage.y-32)//32] != "w":
                        if level[mage.x//32][(mage.y-32)//32] != "e" or haveKey:
                            mage.y -= 32
                elif event.key == K_DOWN:
                    if level[mage.x // 32][(mage.y + 32) // 32] != "w":
                        if level[mage.x // 32][(mage.y + 32) // 32] != "e" or haveKey:
                            mage.y += 32
                elif event.key == K_RIGHT:
                    if level[(mage.x + 32) // 32][mage.y // 32] != "w":
                        if level[(mage.x + 32) // 32][mage.y // 32] != "e" or haveKey:
                            mage.x += 32
                elif event.key == K_LEFT:
                    if level[(mage.x - 32) // 32][mage.y // 32] != "w":
                        if level[(mage.x - 32) // 32][mage.y // 32] != "e" or haveKey:
                            mage.x -= 32
        # Enemy Movement
        if count % 30 == 0:
            en = enemies.sprites()
            for i in range(len(enemies)):
                j = en[i]
                mt = random.randint(0, 3)
                if mt == 0 and level[(j.x - 32) // 32][j.y // 32] != "w":
                        if level[(j.x - 32) // 32][j.y // 32] != "e":
                            j.x -= 32
                if mt == 1 and level[j.x//32][(j.y-32)//32] != "w":
                        if level[j.x//32][(j.y-32)//32] != "e":
                            j.y -= 32
                if mt == 2 and level[(j.x + 32) // 32][j.y // 32] != "w":
                        if level[(j.x + 32) // 32][j.y // 32] != "e":
                            j.x += 32
                if mt == 3 and level[j.x // 32][(j.y + 32) // 32] != "w":
                        if level[j.x // 32][(j.y + 32) // 32] != "e":
                            j.y += 32

        # Key Checking
        if mage.x == key.x and mage.y == key.y:
            haveKey = True
            ends.remove(ends, 0)
            ends.add(Tile("openDoor12.gif", (end.x, end.y)))

        # Death Checking
        if alive:
            en = enemies.sprites()
            for i in range(len(en)):
                j = en[i]
                if mage.x == j.x and mage.y == j.y:
                    players.remove(players, 0)
                    players.add(Dead("grave.gif", (mage.x, mage.y)))
                    alive = False

        # Ending the Stage
        if mage.x == end.x and mage.y == end.y and haveKey:
            stage += 1
            haveKey = False
            ends.remove(ends, 0)
            keys.remove(keys, 0)
            players.remove(players, 0)
            enemies.remove(enemies, 0)
            for i in range(len(wall)):
                wall.remove(wall, i)
            for i in range(len(floor)):
                floor.remove(floor, i)
            create_floor()

        # Updating the Stage
        mage.move()
        en = enemies.sprites()
        for i in range(len(en)):
            en[i].move()
        screen.fill(color)
        floor.draw(screen)
        wall.draw(screen)
        players.draw(screen)
        ends.draw(screen)
        enemies.draw(screen)
        if not haveKey:
            keys.draw(screen)
        text = font.render("Stage: {}".format(stage), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.bottomright= (width, height)
        screen.blit(text, text_rect)
        pygame.display.flip()
        count += 1


if __name__ == "__main__":
    main()
