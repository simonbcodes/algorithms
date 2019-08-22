"""Queue data structure implementation."""


class Queue:
    def __init__(self):
        """Initialize queue with an empty list."""
        self.queue = []

    def __repr__(self):
        """Print list representing queue when called."""
        print(self.queue)

    def get_size(self):
        return len(self.queue)

    def enqueue(self, data):
        """Enqueue data to the beginning of the queue.
            Runtime: O(1)
        """
        if data:
            self.queue.append(data)

    def dequeue(self):
        """Dequeue data from the end of the queue.
            Runtime: O(1)
        """
        if len(self.queue) > 0:
            return self.queue.pop(0)
