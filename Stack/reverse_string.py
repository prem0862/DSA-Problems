
# Problem: https://www.interviewbit.com/problems/reverse-string/



class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        rev_str = ""
        stack = []
        str_size = len(A)
        
        # add elements in stack
        for index in range(0, str_size):
            stack.append(A[index])
            
        return stack
        