
# Problem: https://www.interviewbit.com/problems/reverse-linked-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        head = A
        previous = None
        current = head
        # head -> A -> B -> C -> D -> NULL
        # NULL <- A <- B <- C <- D <- head
        while current is not None:
            next_pointer = current.next
            current.next = previous
            previous = current
            current = next_pointer
        
        # set head to address of last node
        head = previous
        return head
            
            