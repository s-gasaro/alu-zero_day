class Stack:
    def __init__(self):
        # Initialize an empty list to hold the stack items
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item from the stack
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        # Return the top item from the stack without removing it
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def is_empty(self):
        # Return True if the stack is empty, False otherwise
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the stack
        return len(self.items)
