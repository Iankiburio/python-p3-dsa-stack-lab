class Stack:
    def __init__(self, stack=[], limit=None):
       self.stack = stack
       self.limit = limit

    def push(self, value):
        if self.limit is None or len(self.stack) < self.limit:  # check how the limit is assigned
            self.stack.append(value)
        else:
            raise Exception('Stack is full')

    
    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            return None
    
    def peek(self):
        if not self.empty():
            return self.stack[-1]
        else:
            return None
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        return len(self.stack) == 0
    
    def full(self):
        return self.limit is not None and len(self.stack) == self.limit
    
    def search(self, value):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == value:
                return len(self.stack) - i
        return -1
