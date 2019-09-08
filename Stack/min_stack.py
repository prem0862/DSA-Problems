
# Problem: https://www.interviewbit.com/problems/min-stack/




class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)

    # @return nothing
    def pop(self):
        if self.stack:
            res = self.stack.pop()
            if res == self.min_stack[-1]:
                self.min_stack.pop()

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1
        
    # @return an integer
    def getMin(self):
        if self.stack:
            return self.min_stack[-1]
        else:
            return -1

