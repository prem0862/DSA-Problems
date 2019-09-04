"""
    Implement singly linked list

    A linked list is a linear data structure where each element is a separate object.
    Linked list elements are not stored at contiguous location; the elements are linked 
    using pointers.

    Each node of a list is made up of two items - the data and a reference to the next node. 
    The last node has a reference to null. The entry point into a linked list is called the 
    head of the list. It should be noted that head is not a separate node, but the reference
    to the first node. If the list is empty then the head is a null reference.

"""



# Node class
class Node:
    # function to initialize node object
    def __init__(self, data):
        self.value = data # assign value
        self.reference = None # initialize next node adderess as Null




# Linkedlist class
class Linkedlist:
    # function to initialize linkedlist
    def __init__(self):
        self.head = None


    # traverse through linked list
    def traverse_linked_list(self):
        if self.head == None:
            print("Linked list is empty")
            return self.head
        else:
            current_ref = self.head
            while current_ref != None:
                print("Current element is {}".format(current_ref.value))
                current_ref = current_ref.reference
            

    # add element at the end of linked list
    def add_element_end(self, item):
        if self.head == None:
            new_node = Node(item)
            new_node.reference = self.head
            self.head = new_node
        else:
            current_ref = self.head
            while current_ref != None:
                current_ref = current_ref.reference
            new_node = Node(item)
            current_ref = new_node
            

    # add element at the start of linked list
    def add_element_start(self, item):
        new_node = Node(item)
        new_node.reference = self.head
        self.head = new_node


    # size of linked list
    def linked_list_size(self):
        count = 0
        current_ref = self.head
        while current_ref != None:
            count += 1
            current_ref = current_ref.reference
        return count


    # insert item after another element
    def insert_after_item(self, element, item):
        current_ref = self.head
        while current_ref != None:
            if current_ref.value == element:
                break
            current_ref = current_ref.reference
        if current_ref is None:
            print("{} is not present in the linked list".format(element))
        else:
            new_node = Node(item)
            new_node.reference = current_ref
            current_ref = new_node


    # insert item before another item
    def insert_before_item(self, element, item):
        # check if list is emply
        if self.head is None:
            print("Linked list is empty")
            return

        # check if element is located at first node
        if self.head.value == element:
            new_node = Node(item)
            new_node.reference = self.head
            self.head = new_node

        # for other location in linklist
        current_ref = self.head
        while current_ref is not None:
            if current_ref.value == element:
                break
            current_ref = current_ref.reference
        if current_ref is None:
            print("{} is not present is the linked list".format(element))
        else:
            new_node = Node(item)
            new_node.reference = current_ref
            current_ref = new_node




linked_list = Linkedlist()
linked_list.add_element_start("Prem")
linked_list.add_element_end("Prakash")
linked_list.add_element_end("Singh")