import pygame

import direction
import elapsed_timer
import message_bus
import position
import snake_segment

pygame.init()


class Snake:
    def __init__(self, head):
        self.snake_segments = [head]
        self.direction = direction.Direction(0, 0)
        self.elapsed_timer = elapsed_timer.ElapsedTimer()
        self.grow_requested = False
        message_bus.snake_grow_requested.connect(self.on_grow_requested)

    def draw(self, window):
        for segment in self.snake_segments:
            segment.draw(window)

    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and (
            len(self.snake_segments) == 1 or self.direction.get_x() != 1
        ):
            self.direction.set_x(-1).set_y(0)
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (
            len(self.snake_segments) == 1 or self.direction.get_x() != -1
        ):
            self.direction.set_x(1).set_y(0)
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and (
            len(self.snake_segments) == 1 or self.direction.get_y() != 1
        ):
            self.direction.set_x(0).set_y(-1)
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and (
            len(self.snake_segments) == 1 or self.direction.get_y() != -1
        ):
            self.direction.set_x(0).set_y(1)
        if self.direction.get_x() != 0 or self.direction.get_y() != 0:
            if self.elapsed_timer.elapsed(0.2):
                current_head = self.get_head()
                new_head_position = position.Position(
                    current_head.get_x() + (self.direction.get_x() * 80),
                    current_head.get_y() + (self.direction.get_y() * 80),
                )
                self.snake_segments.insert(
                    0, snake_segment.SnakeSegment(new_head_position)
                )
                if self.grow_requested:
                    self.grow_requested = False
                else:
                    self.snake_segments.pop(-1)
                head = self.get_head()
                for segment in self.snake_segments[1:]:
                    if (
                        head.get_x() == segment.get_x()
                        and head.get_y() == segment.get_y()
                    ):
                        message_bus.restart_requested.send(self)
                        return
        head = self.get_head()
        if head.get_x() >= 800 or head.get_x() < 0:
            message_bus.restart_requested.send(self)
        elif head.get_y() >= 800 or head.get_y() < 0:
            message_bus.restart_requested.send(self)

    def get_head(self):
        return self.snake_segments[0]

    def on_grow_requested(self, sender):
        self.grow_requested = True
