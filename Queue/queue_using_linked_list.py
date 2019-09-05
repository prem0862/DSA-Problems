
# implement queue using linked list

""""
    Implement methods:
    1. enque - to push element on stack
    2. deque - to remove element from stack
    3. is_empty - check if stack is empty
    4. top_element - returns top element of stack
"""


# create node
class Node:
    def __init__(self, item):
        self.value = item
        self.next = None


# create queue
class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    
    # add element in queue
    def enqueue(self, item):                # O(1)
        new_node = Node(item)
        if self.head is None:
            self.head = self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = self.last.next


    # remove element from queue
    def dequeue(self):                    # O(1)
        # remove from head side
        if self.head is None:
            print("Queue is empty already")
            return
        else:
            popped_item = self.head.value
            self.head = self.head.next
            return popped_item
        

    # check queue is empty is or not
    def is_empty(self):
        if self.head:
            print("queue is empty")
        else:
            print("queue is empty")


    # top_element
    def top_element(self):
        top_ele = self.last.value
        return top_ele




queue = Queue()
# append element to quesue
queue.enqueue("Prem")
queue.enqueue("Prakash")
queue.enqueue("Singh")

# remove element from queue
print(queue.dequeue())
print(queue.dequeue())


# topmost element
print(queue.top_element())