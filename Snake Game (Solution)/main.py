import pygame
from pygame.locals import *
from random import randint
from Player import Player
from Food import Food
from Pill import Pill
from Scoreboard import Scoreboard

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('ICCS101 - SNAKE')
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.windowWidth = 800
        self.windowHeight = 600
        self.screen = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight), pygame.HWSURFACE)


        self.blockSize = 40
        self.gameSpeed = 6 # update player every 3 frames
        self.maxX = self.windowWidth / self.blockSize
        self.maxY = self.windowHeight / self.blockSize
        self.bgImage = pygame.image.load("assets/grass.jpg").convert()

        self.sfx = pygame.mixer.Sound('assets/beep.wav')
        self.reset()

    def reset(self):
        foodImage = pygame.image.load("assets/food.png").convert()
        self.player = Player(self.blockSize, pygame.Color('red'))
        self.food = Food(randint(0,self.maxX-1), randint(0,self.maxY-1), self.blockSize, foodImage)
        self.pill = Pill(randint(0,self.maxX-1), randint(0,self.maxY-1), self.blockSize)
        self.scoreboard = Scoreboard()

    def update(self):
        self.player.update()

        head_x, head_y = self.player.body[0]

        # does snake hit the wall?
        if (head_x < 0 or head_y < 0 or
            head_x >= self.maxX or head_y >= self.maxY):
            self.gameOver()

        # does snake eat food?
        if (head_x == self.food.x and head_y == self.food.y):
            self.player.eatFood()
            self.sfx.play()
            self.scoreboard.score += 10
            self.food.x = randint(0, self.maxX-1)
            self.food.y = randint(0, self.maxY-1)

        # does snake eat pill?
        if (head_x == self.pill.x and head_y == self.pill.y):
            self.player.eatPill()
            self.sfx.play()
            self.scoreboard.score -= 50
            self.pill.x = randint(0, self.maxX - 1)
            self.pill.y = randint(0, self.maxY - 1)

        # does snake crash into itself?
        if self.player.isSelfCollision():
            self.gameOver()

        # render stuff
        self.screen.blit(self.bgImage, (0, 0))
        self.food.draw(self.screen)
        self.pill.draw(self.screen)
        self.player.draw(self.screen)
        self.scoreboard.draw(self.screen)
        pygame.display.flip()


    def gameOver(self):
        print("Game over")
        self.reset()

    def cleanup(self):
        pygame.quit()

    def run(self):
        frame_count = 0
        while (True):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.player.moveLeft()

            if (keys[K_UP]):
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                break

            # update the game
            if frame_count > self.gameSpeed:
                self.update()
                frame_count = 0

            frame_count += 1

            # limit game speed
            self.clock.tick(self.FPS)

        self.cleanup()

if __name__ == "__main__":
    game = Game()
    # start the game loop and runs until ESC
    game.run()
