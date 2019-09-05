
# Stack - LIFO data structure

""" 
    Implement methods:
    1. push - to push element on stack
    2. pop - to remove element from stack
    3. is_empty - check if stack is empty
    4. top_element - returns top element of stack

"""


# node 
class Node:
    def __init__(self, item):
        self.value = item
        self.next = None



class Stack:

    def __init__(self):
        self.head = None


    # push item on stack
    def push(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node

    
    # remove item from stack
    def pop(self):
        # check if stack is empty
        if self.head is None:
            print("Stack is empty, so any element can't be removed")
        else:
            popped = self.head.value
            self.head = self.head.next
            print("removed {}".format(popped))
            return popped

    
    # check stack is empty or not
    def is_empty(self):
        if self.head is None:
            return True
            print("Stack is empty")
        print("Stack is not empty")
        return False


    # return the top element
    def top_element(self):
        if self.head is None:
            print("Stack is empty")
        else:
            top_val = self.head.value
            return top_val


stack = Stack()
# push items on stack
stack.push("Prem")
stack.push("Rahul")
stack.push("Deepak")
stack.push("Anu")

# remove the topmost item
stack.pop
stack.pop

# check if empty 
stack.is_empty

# topmost element
stack.top_element