from time import time

class TimeChecker:
    def __init__(self):
        self.start_time = None

    def start(self):
        """Start the timer."""
        self.start_time = time()

    def elapsed(self):
        """Return the elapsed time since start was called."""
        if self.start_time is None:
            raise ValueError("Timer has not been started. Call start() before elapsed().")
        return time() - self.start_time

    def reset(self):
        """Reset the timer."""
        self.start_time = None