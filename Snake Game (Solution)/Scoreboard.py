import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("Lucida Grande", 36)

    def draw(self, surface):
        text = self.font.render('Score: {}'.format(self.score), True, (0, 128, 0))
        surface.blit(text, (0,0))