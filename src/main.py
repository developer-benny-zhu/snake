import random

import pygame

import apple
import message_bus
import position
import snake
import snake_segment
from check_collision_between_snake_and_apple_system import (
    CheckCollisionBetweenSnakeAndAppleSystem,
)

pygame.init()


class Application:
    def on_restart_requested(self, sender):
        self.restart()

    def restart(self):
        self.window = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.running = True

                message_bus.restart_requested.connect(self.on_restart_requested)
        message_bus.spawn_new_apple_requested.connect(self.on_spawn_new_apple_requested)

        self.snake_group = [
            snake.Snake(snake_segment.SnakeSegment(position.Position(0, 0)))
        ]
        self.apple_group = []
        self.check_collision_between_snake_and_apple_system = (
            CheckCollisionBetweenSnakeAndAppleSystem(self.snake_group, self.apple_group)
        )

        message_bus.spawn_new_apple_requested.send(self)

    def __init__(self):
        self.restart()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.update()
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        self.window.fill("black")
        for snake in self.snake_group:
            snake.draw(self.window)
        for apple in self.apple_group:
            apple.draw(self.window)

    def update(self):
        for snake in self.snake_group:
            snake.update()
        for apple in self.apple_group:
            apple.update()
        self.check_collision_between_snake_and_apple_system.update()
        self.clock.tick(60)

    def on_spawn_new_apple_requested(self, sender):
        valid_position = False
        while not valid_position:
            x = random.randrange(0, 800, 80)
            y = random.randrange(0, 800, 80)

            valid_position = True
            for snake in self.snake_group:
                if snake.get_head().get_x() == x and snake.get_head().get_y() == y:
                    valid_position = False

        self.apple_group.append(apple.Apple(position.Position(x, y)))


if __name__ == "__main__":
    application = Application()
    application.run()
