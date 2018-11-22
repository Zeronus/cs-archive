class Food:
    def __init__(self, x, y, blockSize, image):
        self.x = x
        self.y = y
        self.blockSize = blockSize
        self.image = image

    def draw(self, surface):
        surface.blit(self.image, (self.x * self.blockSize,
                                  self.y * self.blockSize))
