import time


class ElapsedTimer:
    def __init__(self):
        self.initial_time = time.time()

    def elapsed(self, duration):
        final_time = time.time()
        elapsed_time = final_time - self.initial_time
        if elapsed_time >= duration:
            self.initial_time = final_time
            return True
        return False

    def reset(self):
        self.initial_time = time.time()
