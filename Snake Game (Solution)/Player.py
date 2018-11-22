import pygame

UP = 2
DOWN = 3
LEFT = 1
RIGHT = 0

class Player:
    def __init__(self, blockSize, color):
        self.body = [(3,3),(2,3),(1,3)]
        self.length = len(self.body)
        self.direction = RIGHT
        self.blockSize = blockSize
        self.color = color


    def update(self):
        head_x, head_y = self.body[0]
        if self.direction == RIGHT:
            self.body.insert(0,(head_x + 1,head_y))
        if self.direction == LEFT:
            self.body.insert(0, (head_x - 1, head_y))
        if self.direction == UP:
            self.body.insert(0, (head_x, head_y - 1))
        if self.direction == DOWN:
            self.body.insert(0, (head_x, head_y + 1))
        # shorten the snake if needed
        if len(self.body) > self.length:
            self.body = self.body[:self.length]

    def moveRight(self):
        if self.direction in [UP,DOWN]:
            self.direction = RIGHT

    def moveLeft(self):
        if self.direction in [UP,DOWN]:
            self.direction = LEFT

    def moveUp(self):
        if self.direction in [LEFT,RIGHT]:
            self.direction = UP

    def moveDown(self):
        if self.direction in [LEFT,RIGHT]:
            self.direction = DOWN

    def eatFood(self):
        self.length += 1

    def eatPill(self):
        if self.length > 2:
            self.length -= 1

    def changeColor(self, color):
        self.color = color

    def isSelfCollision(self):
        head_x, head_y = self.body[0]
        for x,y in self.body[1:]:
            if head_x == x and head_y == y:
                return True
        return False

    def draw(self, surface):
        for x,y in self.body:
            surface.fill(self.color, pygame.Rect(
                x*self.blockSize, y*self.blockSize, self.blockSize, self.blockSize))
