import message_bus


class CheckCollisionBetweenSnakeAndAppleSystem:
    def __init__(self, snake_group, apple_group):
        self.snake_group = snake_group
        self.apple_group = apple_group

    def update(self):
        for snake in self.snake_group:
            for apple in self.apple_group:
                if (
                    snake.get_head().get_x() == apple.get_x()
                    and snake.get_head().get_y() == apple.get_y()
                ):
                    message_bus.snake_grow_requested.send(self)
                    message_bus.spawn_new_apple_requested.send(self)
                    self.apple_group.remove(apple)
