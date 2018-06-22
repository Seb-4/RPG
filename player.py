import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos, hp, pow):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.hp = hp
        self.pow = pow
        self.x = pos[0]
        self.y = pos[1]

    def move(self):
        pos = (self.x, self.y)
        self.rect.topleft = pos
