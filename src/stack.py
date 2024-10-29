class Stack():
    def __init__(self, items: list = None):
        if items is None:
            items = []
        self.items = items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        if self.items is None:
            return True
        return len(self.items) < 1
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
