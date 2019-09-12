
# implement a doubly linked list

"""
    In single linked list each node of the list has two components, the actual value of the 
    node and the reference to the next node in the linked list. In the doubly linked list, 
    each node has three components: the value of the node, the reference to the previous node, 
    and the reference to the next node. For the start node of the doubly linked list, the 
    reference to the previous node is null. Similarly, for the last node in the doubly linked 
    list, the reference to next node is null.

    - Pros and Cons of a Doubly Linked List

    Pros
    1. Unlike a single linked list, the doubly linked list can be traversed and searched in both 
       directions. The reference to the next node helps in traversing the node in the forward 
       direction while the references to the previous nodes allow traversal in the backward direction.

    2. Basic operations such as insertion and deletion are easier to implement in the doubly linked 
       lists since, unlike single linked lists, we do not need to traverse to the predecessor node and 
       store its reference. Rather, in a doubly linked list the reference of the predecessor node can 
       be retrieved from the node that we want to delete.

    Cons
    1. One of the major drawbacks of the doubly linked list is that you need more memory space to 
       store one extra reference for each node.

    2. A few additional steps are required to be performed in order to perform insertion and deletion 
       operations.

"""


class Node:
    def __init__(self, item):
        self.val = item
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # traverse linked list
    def traverse(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            while self.head:
                print(self.head.val)
                self.head = self.head.next

    # insert item in empty list
    def insert_empty_list(self, item):
        if self.head is None:
            new_node = Node(item)
            self.head = new_node
        else:
            print("list is not empty")

    # insert item at start
    def insert_at_head(self, item):
        if self.head is None:
            new_node = Node(item)
            self.head = new_node
            return
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # insert item at the end
    def inset_at_end(self, item):
        if self.head is None:
            new_node = Node(item)
            self.start = new_node
            return
        else:
            current = self.head
            while current:
                current = current.next
            new_node = Node(item)
            new_node.prev = current
            current = new_node

    # insert after another item
    def insert_after_item(self, item):
        pass


