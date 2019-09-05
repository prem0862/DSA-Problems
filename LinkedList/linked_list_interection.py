
# Problem: https://www.interviewbit.com/problems/intersection-of-linked-lists/




class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        current_A, current_B = A, B
        len_A, len_B = 0, 0
        
        # length of linked list
        while current_A is not None:   # O(n)
            len_A += 1
            current_A = current_A.next
            
        while current_B is not None:  # O(m)
            len_B += 1
            current_B = current_B.next
            
        # resetting the pointers
        current_A, current_B = A, B
        
        if len_A > len_B:           # O(n -m)
            for i in range(0, len_A -len_B):
                current_A = current_A.next
        else:
            # when size of linked list B is grater then A
            for i in range(0, len_B -len_A):  # O(m -n)
                current_B = current_B.next
        
        # check for intersection point
        while(current_A != current_B):      # O(max(m, n))
            current_A = current_A.next
            current_B = current_B.next
    
        return current_A



        """
        
        Time Complexity : O(n) + O(m) + O(m -n) + O(n -m) + O(max(m, n)) = O(max(m, n))
        Space Complexity : O(1)

        """
        
