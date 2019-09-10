
# Problem: https://www.interviewbit.com/problems/add-two-numbers-as-lists/

# Solution: https://leetcode.com/problems/add-two-numbers/solution/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        current_a = A
        current_b = B
        carry = 0
        while current_a is not None or current_b is not None:
            num_a = current_a.val if current_a else 0
            num_b = current_b.val if current_b else 0
            
            sum_num = num_a + num_b + carry
            if sum_num < 10:
                current_a.val = sum_num
            else:
                last_digit = sum_num %10
                current_a.val = last_digit
                carry = 1
            
            # move to next node
            current_a = current_a.next
            current_b = current_b.next
            
        # if both linked list has exhausted and carry is still left
        new_node = ListNode(carry)
        current_a = new_node
        
        return current_a
        