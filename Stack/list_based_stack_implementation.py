"""
    Stacks, like the name suggests, follow the Last-in-First-Out (LIFO) principle. As if stacking 
    coins one on top of the other, the last coin we put on the top is the one that is the first 
    to be removed from the stack later.

    To implement a stack, therefore, we need two simple operations:
    1. push - add an element to the top of stack
    2, pop - remove the element at the top of stack

    Apart from that also implement some functions to find / check;
    3. length of the stack
    4. check if stack is empty or not?

"""



class Stack:
    # constructor to initialize a stack
    def __init__(self):
        self.items = []

    # add element at the top of stack
    def push(self, element):
        self.items.append(element)

    # remove element from the top of stack
    def pop(self):
        self.items.pop()

    # len of the stack
    def stack_len(self):
        return len(self.items)

    # check if stack is empty or not
    def is_stack_empty(self):
        if self.stack_len() == 0:
            return True
        return False



# create a stack
stack = Stack()
# add 5 to stack
stack.push(5)
stack.push(6)
print(stack.stack_len())
# remove topmost element from stack
stack.pop()
print(stack.stack_len())