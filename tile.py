import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.x = pos[0]
        self.y = pos[1]
