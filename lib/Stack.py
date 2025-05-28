class Stack:

    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.limit is not None and len(self.items) >= self.limit:
            return
        self.items.append(item)


    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        if self.limit is None:
            return False
        return len(self.items) >= self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items) - 1 - self.items.index(target)
        return -1
