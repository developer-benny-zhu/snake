class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x
        return self

    def set_y(self, y):
        self.y = y
        return self

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
