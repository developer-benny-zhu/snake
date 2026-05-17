import pygame

pygame.init()


class SnakeSegment:
    def __init__(self, position):
        self.position = position

    def draw(self, window):
        pygame.draw.rect(window, "green", (self.position.x, self.position.y, 80, 80))

    def get_x(self):
        return self.position.get_x()

    def get_y(self):
        return self.position.get_y()
