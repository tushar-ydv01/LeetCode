class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self, value):
        self.stack.append(value)
        if not self.minStack or value<= self.minStack[-1]:
            self.minStack.append(value)
        

    def pop(self):
        value = self.stack.pop()
        if value == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minStack[-1]