from collections import deque

class Queue:

    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft();

    def size(self):
        return self.items.__len__()

    def peek(self):
        return self.items[0]

    def __str__(self) -> str:
        return str(self.items)