import pygame

class Pill:
    def __init__(self, x, y, blockSize):
        self.x = x
        self.y = y
        self.blockSize = blockSize
        self.color = (255,255,0)
        self.updateCount = 0

    def draw(self, surface):
        r = self.blockSize // 2
        pygame.draw.circle(surface, self.color, (self.x*self.blockSize+r, self.y*self.blockSize+r), r)
