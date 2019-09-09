
# Problem: https://www.interviewbit.com/problems/list-cycle/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        # create a hash table to store the address of the each visited node
        visited_node = set()
        current = A
        
        while current:
            if current in visited_node:
                return current
            visited_node.add(current)
            current = current.next
        
        return None
      
        