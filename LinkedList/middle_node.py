
# Problem: https://leetcode.com/problems/middle-of-the-linked-list/



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """
            When traversing the list with a pointer slow, make another pointer fast that 
            traverses twice as fast. When fast reaches the end of the list, slow must be 
            in the middle.
        """
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        