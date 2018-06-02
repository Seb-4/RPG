import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.hp = 100
        self.pow = 5