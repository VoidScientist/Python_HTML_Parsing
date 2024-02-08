class Stack():
    def __init__(self):
        self.content = []
        
    def stack(self, value):
        self.content.append(value)
        
    def is_empty(self):
        return len(self.content) == 0
    
    def peek(self):
        if not self.is_empty():
            return stack[-1]
        raise Exception("Stack is empty")
        
    def unstack(self):
        del self.content