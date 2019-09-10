
# Problem: https://www.interviewbit.com/problems/rotated-array/



class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        min_index = 0
        array_size = len(A)
        # scan through the array and find the index of min element
        for index in range(1, array_size):
            if A[index] < A[min_index]:
                min_index = index
        
        min_element = A[min_index]
        return min_element
            
