"""Stack implementation using lists."""
class Stack:
    def __init__(self):
        """ Initialize the stack to be a an empty list."""
        self.stack = []

    def size(self):
        """Return the size of the stack."""
        return len(self.stack)

    def push(self, data):
        """Push data to the top of the stack.
            Runtime: O(1)
        """
        if data:
            self.stack.append(data)

    def pop(self):
        """Pop data from the top of the stack.
            Runtime: O(1)
        """
        if len(self.stack) > 0:
            return self.stack.pop()
