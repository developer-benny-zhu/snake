import pygame

from position import Position

pygame.init()


class Apple:
    def __init__(self, position):
        self.position = position

    def draw(self, window):
        pygame.draw.rect(
            window, "red", (self.position.get_x(), self.position.get_y(), 80, 80)
        )

    def update(self):
        pass

    def get_x(self):
        return self.position.get_x()

    def get_y(self):
        return self.position.get_y()
